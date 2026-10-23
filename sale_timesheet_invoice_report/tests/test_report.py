# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
"""Time entries on the invoice, switched per customer, invoice and line."""

from odoo.tests import tagged

from odoo.addons.sale_timesheet.tests.common import TestCommonSaleTimesheet


@tagged("post_install", "-at_install")
class TestTimesheetInvoiceReport(TestCommonSaleTimesheet):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.order = cls.env["sale.order"].create(
            {
                "partner_id": cls.partner_a.id,
                "partner_invoice_id": cls.partner_a.id,
                "partner_shipping_id": cls.partner_a.id,
            }
        )
        cls.line_task = cls.env["sale.order.line"].create(
            {
                "product_id": cls.product_delivery_timesheet2.id,
                "product_uom_qty": 10,
                "order_id": cls.order.id,
            }
        )
        cls.line_project = cls.env["sale.order.line"].create(
            {
                "product_id": cls.product_delivery_timesheet3.id,
                "product_uom_qty": 10,
                "order_id": cls.order.id,
            }
        )
        cls.order.action_confirm()
        cls.task_1 = cls.env["project.task"].search(
            [("sale_line_id", "=", cls.line_task.id)]
        )
        cls.task_2 = cls.env["project.task"].search(
            [("sale_line_id", "=", cls.line_project.id)]
        )
        Line = cls.env["account.analytic.line"]
        cls.timesheets = Line
        for task, name, hours in (
            (cls.task_1, "Concept", 1.5),
            (cls.task_1, "Layout", 2.25),
            (cls.task_2, "Programming", 4.0),
        ):
            cls.timesheets |= Line.create(
                {
                    "name": name,
                    "project_id": task.project_id.id,
                    "task_id": task.id,
                    "unit_amount": hours,
                    "employee_id": cls.employee_user.id,
                }
            )
        cls.invoice = cls.order._create_invoices()

    def html(self, invoice=None):
        return str(
            self.env["ir.actions.report"]._render_qweb_html(
                "account.report_invoice", (invoice or self.invoice).ids
            )[0]
        )

    def invoice_line(self, sale_line):
        return sale_line.invoice_lines.filtered(
            lambda line: line.move_id == self.invoice
        )

    def test_all_time_entries_by_task(self):
        self.assertEqual(self.invoice._get_report_timesheets(), self.timesheets)
        html = self.html()
        for text in (
            "Timesheets",
            self.task_1.name,
            self.task_2.name,
            "Concept",
            "Programming",
            "Subtotal",
            "03:45",
            "Total (hours)",
            "07:45",
        ):
            self.assertIn(text, html)

    def test_customer_without_timesheets(self):
        self.partner_a.timesheet_on_invoice = "no"
        self.assertFalse(self.invoice._get_report_timesheets())
        self.assertNotIn("Total (hours)", self.html())

    def test_invoice_overrides_customer(self):
        self.partner_a.timesheet_on_invoice = "no"
        self.invoice.timesheet_on_invoice = "yes"
        self.assertEqual(self.invoice._get_report_timesheets(), self.timesheets)
        self.partner_a.timesheet_on_invoice = "yes"
        self.invoice.timesheet_on_invoice = "no"
        self.assertFalse(self.invoice._get_report_timesheets())

    def test_line_overrides_invoice(self):
        self.invoice_line(self.line_project).timesheet_on_invoice = "no"
        shown = self.invoice._get_report_timesheets()
        self.assertEqual(shown.mapped("name"), ["Layout", "Concept"])
        self.invoice.timesheet_on_invoice = "no"
        self.invoice_line(self.line_project).timesheet_on_invoice = "yes"
        self.assertEqual(
            self.invoice._get_report_timesheets().mapped("name"), ["Programming"]
        )
        self.assertNotIn("Concept", self.html())

    def test_time_entries_without_task(self):
        # invoiced time entries cannot be changed: invoice again without the task
        self.invoice.unlink()
        self.timesheets[-1].write({"task_id": False})
        invoice = self.order._create_invoices()
        self.assertEqual(invoice._get_report_timesheets(), self.timesheets)
        self.assertIn("Other services", self.html(invoice))

    def test_not_on_vendor_bills(self):
        bill = self.env["account.move"].create(
            {"move_type": "in_invoice", "partner_id": self.partner_a.id}
        )
        self.assertFalse(bill._get_report_timesheets())

    def test_setting_of_the_company_applies_to_its_contacts(self):
        contact = self.env["res.partner"].create(
            {
                "name": "Accounts Payable",
                "parent_id": self.partner_a.id,
                "type": "invoice",
            }
        )
        self.partner_a.timesheet_on_invoice = "no"
        self.assertEqual(contact.timesheet_on_invoice, "no")
