"""
Filename: __init__.py
Description: Entrance script for Sacrament.
Version: 1.0
Author: Harspek
Date: 08-03-2026
"""

import data
import game
import ui

player = {
    'location': 'start',
    'inv': []
}

while True: # Main loop
    ui._update_window() # Refreshes the UI, has to happen every frame, or the screen freezes / the application shuts down
    # game.logic()