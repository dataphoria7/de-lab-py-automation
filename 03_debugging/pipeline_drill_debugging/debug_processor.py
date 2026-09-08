# debug_processor.py

"""
BLOCK 1 — Imports
"""
import logging
import os

"""
BLOCK 2 — Logging Configuration
"""
logging.basicConfig(
    filename="debug_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

"""
BLOCK 3 — Safe Division Example (Debugging Basics)
"""
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        return None

"""
BLOCK 4 — Assertion Example
"""
def check_math():
    try:
        assert 2 + 2 == 5, "Math assertion failed"
    except AssertionError as e:
        logging.warning(f"Assertion triggered: {e}")

"""
BLOCK 5 — Mini Project: Safe File Reader
"""
def safe_read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"File not found: {path}")
        return None
    except PermissionError:
        logging.error(f"Permission denied: {path}")
        return None

"""
BLOCK 6 — Mini Project: Transformation
"""
def transform_data(text):
    if text is None:
        return []
    lines = text.splitlines()
    clean = [line.strip().upper() for line in lines if line.strip()]
    return clean

"""
BLOCK 7 — Mini Project: Write Clean Output
"""
def write_clean_output(rows):
    with open("clean_output.csv", "w") as f:
        for row in rows:
            f.write(row + "\n")
    logging.info("Clean output written successfully.")

"""
BLOCK 8 — Pipeline Orchestration
"""
def run_pipeline():
    logging.info("Starting debugging pipeline drill.")

    # Step 1: Basic debugging examples
    safe_division(10, 5)
    safe_division(10, 0)
    check_math()

    # Step 2: Read raw data
    raw = safe_read_file("raw_data.txt")

    # Step 3: Transform
    clean_rows = transform_data(raw)

    # Step 4: Write output
    write_clean_output(clean_rows)

    logging.info("Pipeline drill complete.")

if __name__ == "__main__":
    run_pipeline()



