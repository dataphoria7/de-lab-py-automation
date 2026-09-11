import os
import csv
import json
# ↑ os: for safe file paths
#   csv: to read CSV files
#   json: to write JSON files


# ---------------------------------------------------------
# BASE_DIR: the folder where THIS script lives.
# Ensures the pipeline writes files INSIDE pipeline_drill_json
# even if you run the script from VS Code or a parent folder.
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------
# INGESTION STEP
# Reads CSV file and returns a list of dictionaries.
# Each row becomes: {"MONTH": "...", "SALES": "...", "REGION": "..."}
# ---------------------------------------------------------
def read_csv(path):
    rows = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        # ↑ DictReader converts each CSV row → dictionary
        for row in reader:
            rows.append(row)
    return rows


# ---------------------------------------------------------
# TRANSFORMATION STEP
# Cleans or modifies the CSV rows before converting to JSON.
# You can add business logic here.
# ---------------------------------------------------------
def transform_sales(rows):
    transformed = []
    for row in rows:
        transformed.append({
            "month": row["MONTH"],          # string
            "sales": int(row["SALES"]),     # convert to integer
            "region": row["REGION"]         # string
        })
    return transformed


# ---------------------------------------------------------
# OUTPUT STEP
# Writes the final JSON file.
# This is the "skeleton" receiving the transformed data.
# ---------------------------------------------------------
def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        # ↑ indent=4 makes JSON readable for humans.


# ---------------------------------------------------------
# ORCHESTRATOR STEP
# This function runs the entire pipeline in order.
# It defines:
#   - where the CSV file is
#   - where the JSON file will be created
#   - calls ingestion → transformation → output
# ---------------------------------------------------------
def run_json_pipeline():
    csv_path = os.path.join(BASE_DIR, "sales.csv")
    # ↑ YOU create sales.csv manually.

    json_path = os.path.join(BASE_DIR, "sales.json")
    # ↑ PIPELINE creates sales.json automatically.

    raw_rows = read_csv(csv_path)
    # ↑ Step 1: Ingest CSV

    transformed = transform_sales(raw_rows)
    # ↑ Step 2: Transform data

    write_json(json_path, transformed)
    # ↑ Step 3: Write JSON output


# ---------------------------------------------------------
# ENTRY POINT
# This runs the pipeline when you execute the file.
# ---------------------------------------------------------
if __name__ == "__main__":
    run_json_pipeline()
