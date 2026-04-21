"""
Filename: data.py
Description: Handles saving and loading JSON files.
Version: 1.2
Author: Harspek
Date: 08-03-2026
"""

import json
from typing import Any

def save(filename: str, information: Any) -> None: # Save data to a JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(information, f, ensure_ascii=False, indent=2)

def load(filename: str) -> Any: # Load data from a JSON file
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'"{filename}" does not exist; Save once before attempting to load')