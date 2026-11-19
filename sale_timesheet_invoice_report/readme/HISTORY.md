## 20.0.1.0.0

- Migration to Odoo 20. The module itself is unchanged: the invoice report,
  the forms of the customer and the invoice and the link between a time
  entry and its invoice (now `reinvoice_move_id` behind the unchanged
  `timesheet_ids` of the invoice) still fit.
- New in Odoo 20, not part of this module: the e-mail of an invoice that
  bills time entries gets the report *Timesheets* of Odoo as a second
  attachment. The settings of this module do not apply to it, see the
  known issues.

## 19.0.1.0.0

- First version for Odoo 19, built on the time sheet that Baumgärtner
  Marketing GmbH has printed on its invoices since August 2026.
