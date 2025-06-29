# python-automation-scripts

This repository contains useful automation scripts developed in Python.

All of them are designed for real-world tasks that can be useful in system administration, data scraping, or basic cybersecurity contexts.

## Included Scripts:

| Script                | Description |
|----------------------|-------------|
| scrape_news.py       | Scraper that extracts headlines from El País |
| auto_log_cleaner.py  | Deletes old logs in `/var/log` based on age |
| disk_usage_report.py | Displays disk usage by directory (analyzes how much space each folder within a given path occupies), useful for sysadmins |
| check_open_ports.py  | Scans open TCP ports on a given IP (with progress bar) |

## Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
