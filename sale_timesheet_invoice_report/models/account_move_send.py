# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
"""No report *Timesheets* of Odoo in the e-mail of an invoice.

Odoo 20 links its report *Timesheets* to the e-mail templates of invoices and
attaches it whenever the invoice bills time entries. This module prints the
time entries on the invoice itself, switched per customer, invoice and line,
so the report of Odoo would add a second time sheet that ignores these
settings.
"""

from odoo import api, models


class AccountMoveSend(models.AbstractModel):
    _inherit = "account.move.send"

    @api.model
    def _get_placeholder_mail_template_dynamic_attachments_data(
        self, move, mail_template, pdf_report=None
    ):
        placeholders = super()._get_placeholder_mail_template_dynamic_attachments_data(
            move, mail_template, pdf_report=pdf_report
        )
        report_name = self.env.ref(
            "sale_timesheet.timesheet_report_account_move"
        ).report_name
        return [
            placeholder
            for placeholder in placeholders
            if placeholder.get("dynamic_report") != report_name
        ]
