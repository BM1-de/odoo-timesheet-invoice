# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    timesheet_on_invoice = fields.Selection(
        [("move", "As on the Invoice"), ("yes", "Yes"), ("no", "No")],
        string="Timesheets",
        default="move",
        help="Print the time entries billed by this line on the invoice.",
    )
