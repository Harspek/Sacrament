"""
Filename: data.py
Description: Handles saving and loading JSON files.
Version: 1.1
Author: Harspek
Date: 08-03-2026
"""

import json
from typing import Any

filename = "data.json" # The name of the file where data will be saved and loaded from

def save(information: Any) -> None: # Save data to a JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(information, f, ensure_ascii=False, indent=2)

def load() -> Any: # Load data from a JSON file
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)