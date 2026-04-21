"""
Filename: __init__.py
Description: Entrance script for Sacrament.
Version: 1.2
Author: Harspek
Date: 08-03-2026
"""

import ui # Handles the frontend actions

ui.print_location('')
ui._insert_label('\n\nEnter a value into the field below and press the "Enter/Return" key to submit the command\nPress one of the buttons below the text field to switch between various informative screens')
while ui.active: # The replacement for Tkinter's mainloop
    ui._update_window() # Refreshes the UI, has to happen every frame or the screen freezes / the application shuts down
    