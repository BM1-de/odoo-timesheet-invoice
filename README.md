

# Stundennachweis auf der Rechnung für Odoo
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/BM1-de/odoo-timesheet-invoice/actions/workflows/pre-commit.yml/badge.svg?branch=20.0)](https://github.com/BM1-de/odoo-timesheet-invoice/actions/workflows/pre-commit.yml?query=branch%3A20.0)
[![Build Status](https://github.com/BM1-de/odoo-timesheet-invoice/actions/workflows/test.yml/badge.svg?branch=20.0)](https://github.com/BM1-de/odoo-timesheet-invoice/actions/workflows/test.yml?query=branch%3A20.0)
[![codecov](https://codecov.io/gh/BM1-de/odoo-timesheet-invoice/branch/20.0/graph/badge.svg)](https://codecov.io/gh/BM1-de/odoo-timesheet-invoice)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

Die abgerechneten Zeiteinträge stehen auf der Rechnung selbst, nach Aufgabe gegliedert und
mit Zwischensummen – statt nur „7,50 Stunden Entwicklung“ in einer Position. Ob sie
gedruckt werden, lässt sich je Kunde, je Rechnung und je Rechnungsposition einstellen.

> **Alpha:** So druckt die Baumgärtner Marketing GmbH ihre Rechnungen seit August 2026, als
> Modul ist es neu. Die Software wird ohne Gewährleistung bereitgestellt (AGPL-3.0,
> Abschnitte 15 und 16).

![Rechnung mit Stundennachweis](docs/screenshots/rechnung.png)

## Was das Modul tut

- Eine eigene Seite hinter Positionen und Summen, gegliedert nach Aufgabe: Datum,
  Beschreibung und aufgewendete Zeit, eine Zwischensumme je Aufgabe und die Gesamtsumme.
- Keine Spalte für den Mitarbeiter.
- Zeiteinträge ohne Aufgabe stehen unter „Sonstige Leistungen“.
- Drei Ebenen, jede übersteuert die darüber: der Kunde (Ja/Nein), die Rechnung (wie beim
  Kunden/Ja/Nein) und die Rechnungsposition (wie auf der Rechnung/Ja/Nein). Kontakte einer
  Firma folgen der Firma.

## Einrichtung und Nutzung

1. Unter *Apps* „Timesheets on Invoices“ installieren; das Modul braucht Verkauf und
   Zeiterfassung (`sale_timesheet`).
2. Am Kunden, Reiter *Verkauf & Einkauf*, Gruppe *Abrechnung von Zeiten*: „Stundennachweis
   auf Rechnungen“ – Vorgabe ist Ja.
3. Abweichungen an der Rechnung (Reiter *Weitere Informationen*) oder an einer Position
   (Spalte *Stundennachweis*, über die Spaltenauswahl einblenden).
4. Die Rechnung wie gewohnt aus dem Auftrag erstellen; Vorschau, Druck und Versand
   enthalten den Stundennachweis.

![Einstellung an der Rechnung](docs/screenshots/einstellung.png)

## Mehr Dokumentation

Die Beschreibung des Moduls (englisch) steht in
[sale_timesheet_invoice_report/README.rst](sale_timesheet_invoice_report/README.rst).

*English: The billed time entries on the invoice itself, grouped by task with subtotals,
switchable per customer, invoice and invoice line. Alpha, no warranty.*

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[sale_timesheet_invoice_report](sale_timesheet_invoice_report/) | 20.0.1.0.0 | <a href='https://github.com/bm1-phillip'><img src='https://github.com/bm1-phillip.png' width='32' height='32' style='border-radius:50%;' alt='bm1-phillip'/></a> | Print the billed time entries on the invoice, grouped by task, switchable per customer, invoice and invoice line

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Baumgärtner Marketing GmbH
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->

<!-- bm1-verweise:start (scripts/readme-bm1.py, nicht von Hand ändern) -->

## Weitere Odoo-Projekte von BM1

| Projekt | Zweck |
| ------- | ----- |
| [Cc und Bcc](https://github.com/BM1-de/odoo-mail-cc-bcc) | Cc und Bcc beim Mailversand, eine einzige E-Mail an alle Empfänger |
| [Briefanrede](https://github.com/BM1-de/odoo-partner-salutation) | Anrede am Kontakt und die passende Grußzeile in Rechnungsmails |
| [Namenszusatz](https://github.com/BM1-de/odoo-partner-name-addition) | Zweite Namenszeile am Kontakt, gedruckt in jeder Anschrift |
| [Arbeitszeitgesetz](https://github.com/BM1-de/odoo-l10n-germany-arbzg) | Gesetzliche Pausen und Höchstarbeitszeit bei Anwesenheiten, Arbeitszeitkonto ab Odoo 20 |
| [Deutsche EÜR](https://github.com/BM1-de/odoo-l10n-germany-euer) | Einnahmenüberschussrechnung mit Anlage EÜR, AVEÜR und Anlagenverzeichnis |
| [Papierkram-Import](https://github.com/BM1-de/odoo-papierkram-import) | Kontakte, Rechnungen, Belege, Zahlungen und Zeiten aus Papierkram übernehmen |
| [Zeiterfassung für Odoo (macOS)](https://github.com/BM1-de/timesheets-for-odoo) | Menüleisten-App für Zeiten und Anwesenheit |
| [Zeiterfassung für Odoo (Windows)](https://github.com/BM1-de/timesheets-for-odoo-windows) | App im Infobereich für Zeiten und Anwesenheit |

## Über BM1

<a href="https://bm1.de"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/bm1/logo-bm1-negativ.svg"><img src="docs/bm1/logo-bm1.svg" alt="BM1" width="180"></picture></a>

Entwickelt und gepflegt von [BM1](https://bm1.de), der Baumgärtner Marketing GmbH aus
Bayreuth: Agentur für [Websites](https://bm1.de/websites/),
[Webentwicklung](https://bm1.de/webentwicklung/), [SEO](https://bm1.de/seo/) und
[individuelle digitale Lösungen](https://bm1.de/digitale-spezial-themen/). Wir arbeiten selbst
jeden Tag mit Odoo und bauen, was uns dort fehlt. Wenn Sie Unterstützung bei Odoo, einer
Website oder einer Anbindung brauchen, die es nicht von der Stange gibt:
[sprechen Sie uns an](https://bm1.de/kontakt/).

<!-- bm1-verweise:end -->
