Prints the billed time entries on the customer invoice itself, on a page of
their own after the totals, instead of only the summed line ("7.50 hours of
development"):

- grouped by task, with the date, the description and the time spent, a
  subtotal per task and the total;
- without a column for the employee;
- time entries without a task under "Other services".

Three levels decide whether they are printed, each one overriding the one
above: the customer, the invoice and the invoice line that billed them.
