"""
Filename: __init__.py
Description: Entrance script for Sacrament.
Version: 1.2
Author: Harspek
Date: 08-03-2026
"""

import ui # User interface management

ui.print_location('')
while ui.active: # Main loop
    ui._update_window() # Refreshes the UI, has to happen every frame, or the screen freezes / the application shuts down
    