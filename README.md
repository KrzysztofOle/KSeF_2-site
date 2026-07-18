# KSeF_2 project website

Public, bilingual presentation website for **KSeF_2** — a vendor-neutral
framework for communication with Poland's National e-Invoice System (KSeF).

- Website: https://krzysztofole.github.io/KSeF_2-site/
- Polish version: https://krzysztofole.github.io/KSeF_2-site/pl.html
- Hosting: GitHub Pages
- Source: static HTML, CSS and JavaScript with no external runtime dependencies

The website presents the post-migration architecture: KSeF_2 owns KSeF
communication, workflow orchestration, Public API and Port Contracts, while ERP
integrations are separate connector projects. The Comarch ERP Optima integration
is maintained in
[ksef-optima-connector](https://github.com/KrzysztofOle/ksef-optima-connector).

This repository contains presentation assets only. The KSeF_2 implementation,
credentials, certificates, test invoices and controlled test evidence are not
part of the website repository.

## Published project baseline

The content reflects the vendor-neutral KSeF_2 architecture after extraction of
the Optima connector. KSeF_2 contains no Optima runtime, SQL Server configuration
or dependency on a specific ERP.

Last synchronized: 2026-07-18.
