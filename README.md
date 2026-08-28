# IDS Alert Parser

## Description

A Python script that parses IDS alerts in JSON format and exports structured data to both CSV and JSON for easier analysis and reporting in SOC environments. Demonstrates practical log parsing, data extraction, and error handling — core skills for tier 1 incident response workflows.

Use case: Ingest raw alert feeds, clean and aggregate by severity/category, export for further analysis or SIEM integration.

## Prerequisites

- Python 3.10 or higher
- No external dependencies required (uses built-in `json` and `csv` modules)

## Usage

1. Clone or download the repository
2. Run the script:
```bash
python3 ids_alert_parser.py
```
3. Output files will be generated in the same directory:
   - alerts_parsed.csv
   - alerts_parsed.json

## Input / Output

### Input

alerts-only.json: IDS alerts containing fields: timestamp, event_type, src_ip, dest_ip, proto, alert (with action, gid, signature_id, signature, category, severity), and more.

### Output

- alerts_parsed.csv: Flattened alert records (one per row) with fields: timestamp, src_ip, src_port, dest_ip, dest_port, proto, app_proto, signature_id, signature, category, severity.
- alerts_parsed.json: Structured output containing the same records as .csv but in JSON format for programmatic access and further aggregation.
- Console display: Summary tables printed to stdout showing alert counts grouped by severity and category.

## Skills Demonstrated

- JSON parsing: Nested dictionary extraction using .get() for safe field access
- CSV export: Writing tabular data with csv.DictWriter
- Error handling: Three try-except blocks for file I/O, JSON decoding, and data extraction robustness
- Data aggregation: In-memory summaries by severity and category
- Log normalization: Flattening nested JSON into actionable fields for SOC workflows

## Data Source
This project uses sample alerts from:
https://github.com/FrankHassanabad/suricata-sample-data/tree/master/samples/wrccdc-2018

License: MIT

File: alerts-only.json


