# Pipeline Drill 03 — Debugging & Logging

## Purpose
Practice debugging, assertions, safe file operations, and logging while building a small ETL-style pipeline.

## Workflow
1. Read raw data from `raw_data.txt`
2. Handle errors (missing file, permissions)
3. Log all events to `debug_log.log`
4. Transform data (uppercase normalization)
5. Write clean output to `clean_output.csv`

## Files
- debug_processor.py — main pipeline script
- raw_data.txt — input data
- clean_output.csv — cleaned output
- debug_log.log — logged events

## How to Run
python debug_processor.py
