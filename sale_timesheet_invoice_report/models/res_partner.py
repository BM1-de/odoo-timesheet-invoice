# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    timesheet_on_invoice = fields.Selection(
        [("yes", "Yes"), ("no", "No")],
        string="Timesheets on Invoices",
        default="yes",
        help="Print the billed time entries on the invoices of this customer. Each "
        "invoice and each invoice line can deviate from it.",
    )

    @api.model
    def _commercial_fields(self):
        return super()._commercial_fields() + ["timesheet_on_invoice"]
