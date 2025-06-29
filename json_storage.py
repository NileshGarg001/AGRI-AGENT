# json_storage.py
import json
import os

DATA_FILE = os.path.join("data", "farm_data.json")

def read_logs():
    """Reads all logs from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def write_log(entry: dict):
    """Appends a new log entry to the JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    logs = read_logs()
    logs.append(entry)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False) 