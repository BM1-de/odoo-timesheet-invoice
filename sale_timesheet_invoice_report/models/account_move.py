# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
"""Time entries printed on a customer invoice.

Three levels decide, each one overriding the one above: the customer, the
invoice and the invoice line that billed the time entry.
"""

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    timesheet_on_invoice = fields.Selection(
        [("partner", "As on the Customer"), ("yes", "Yes"), ("no", "No")],
        string="Timesheets on the Invoice",
        default="partner",
        help="Print the billed time entries on this invoice. Each invoice line can "
        "deviate from it.",
    )

    def _get_report_timesheets(self):
        """Time entries to print on this invoice, in the order of Odoo."""
        self.ensure_one()
        timesheets = self.env["account.analytic.line"]
        if self.move_type not in ("out_invoice", "out_refund"):
            return timesheets
        move = self.sudo()
        if move.timesheet_on_invoice in ("yes", "no"):
            default = move.timesheet_on_invoice
        else:
            default = move.partner_id.timesheet_on_invoice or "yes"
        for timesheet in move.timesheet_ids:
            line = timesheet.so_line.invoice_lines.filtered(
                lambda invoice_line: invoice_line.move_id == move
            )[:1]
            value = line.timesheet_on_invoice
            if (value if value in ("yes", "no") else default) == "yes":
                timesheets |= timesheet
        return timesheets
