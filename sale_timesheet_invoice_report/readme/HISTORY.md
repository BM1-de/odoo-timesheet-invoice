## 20.0.1.0.0

- Migration to Odoo 20. The invoice report, the forms of the customer and
  the invoice and the link between a time entry and its invoice (now
  `reinvoice_move_id` behind the unchanged `timesheet_ids` of the invoice)
  work unchanged.
- The e-mail of an invoice no longer gets the report *Timesheets* that
  Odoo 20 attaches to invoices that bill time entries. It listed every
  billed time entry with the employee, whatever was set for the customer,
  the invoice or the line. The time entries are on the invoice itself, as
  set with this module.

## 19.0.1.0.0

- First version for Odoo 19, built on the time sheet that Baumgärtner
  Marketing GmbH has printed on its invoices since August 2026.
