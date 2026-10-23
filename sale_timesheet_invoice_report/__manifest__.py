# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Timesheets on Invoices",
    "summary": "Print the billed time entries on the invoice, grouped by task, "
    "switchable per customer, invoice and invoice line",
    "version": "19.0.1.0.0",
    "category": "Accounting/Accounting",
    "website": "https://github.com/BM1-de/odoo-timesheet-invoice",
    "author": "Baumgärtner Marketing GmbH",
    "maintainers": ["bm1-phillip"],
    "license": "AGPL-3",
    "development_status": "Alpha",
    "depends": ["sale_timesheet"],
    "data": [
        "views/res_partner_views.xml",
        "views/account_move_views.xml",
        "report/report_invoice.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
}
