"""
Filename: __init__.py
Description: Entrance script for Sacrament.
Version: 1.1
Author: Harspek
Date: 08-03-2026
"""

import data # Savefile and parsing management
import game # Gameplay management
import ui # User interface management

ui._clear_label()
ui._insert_label('Did you know...\nThis textfield breaks a little bit if you make the window too small\nThis means i am forced to make the screen a certain size to that it does not shatter the entire thing')

while ui.active: # Main loop
    ui._update_window() # Refreshes the UI, has to happen every frame, or the screen freezes / the application shuts down
    # game.logic()