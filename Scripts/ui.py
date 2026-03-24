"""
Filename: ui.py
Description: Includes functions for generation and management of the UI
Version: 1.0
Author: Harspek
Date: 08-03-2026
TODO: UI
"""

import tkinter
from tkinter import Tk
import asyncio

# Button
class CustomButton(tkinter.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='groove',
            bd=1,  # Remove border
            highlightthickness=0,  # Remove highlight
            padx=10,  # Add horizontal padding
            pady=5,  # Add vertical padding
            font=('Roboto Slab', 16),  # Set font
            foreground='black',  # Text color
            background='darkgray',  # Background color
            activeforeground='white',
            activebackground='black',
            height=3,
            width=6
        )
        # Bind events
        self.bind('<Enter>', self.on_hover)
        self.bind('<Leave>', self.on_leave)

    def on_hover(self, event):
        self.config(background='gray')  # Change color on hover

    def on_leave(self, event):
        self.config(background='darkgray')  # Restore original color

# Label utilized as console replacement
class DialogLabel(tkinter.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='groove',
            bd=1,
            highlightthickness=0,  # Remove highlight
            padx=10,  # Add horizontal padding
            pady=5,  # Add vertical padding
            font=('Roboto Slab', 16),  # Set font
            foreground='black',  # Text color
            background='darkgray',  # Background color
        )

# Label utilized for instucting on UI elements
class InstructionLabel(tkinter.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='flat',
            bd=0,
            highlightthickness=0,  # Remove highlight
            padx=10,  # Add horizontal padding
            pady=5,  # Add vertical padding
            font=('Roboto Slab', 16),  # Set font
            foreground='black',  # Text color
            background='lightgray',  # Background color
        )

# Text field
class CustomField(tkinter.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='groove',
            bd=1,
            highlightthickness=0,  # Remove highlight
            font=('Roboto Slab', 16),  # Set font
            foreground='black',  # Text color
            background='darkgray',  # Background color
            width=50,    
        )

# Window creation
window = Tk()
window.state('zoomed')
window.title("Sacrament")
window.minsize(1440, 960)
window.maxsize(1920, 1920)
window.config(background='lightgray')

# Instance each required widget
dialog_label = DialogLabel(window, text="Dialog Label")
custom_button_1 = CustomButton(window, text="1")
custom_button_2 = CustomButton(window, text="2")
custom_button_3 = CustomButton(window, text="3")
instruct_label_1 = InstructionLabel(window, text='Inventory')
instruct_label_2 = InstructionLabel(window, text='Dialog Box')
custom_button_4 = CustomButton(window, text="4")
custom_field = CustomField(window)

# Pack widgets into window
dialog_label.pack(fill='both', side='top', expand=1)
custom_button_1.pack(padx=10, pady=10, anchor='s', side='left')
custom_button_2.pack(padx=10, pady=10, anchor='s', side='left')
custom_button_3.pack(padx=10, pady=10, anchor='s', side='left')
instruct_label_1.pack(padx=10, pady=10, anchor='s', side='left')
custom_field.pack(padx=10, pady=50, anchor='s', side='right')
custom_button_4.pack(padx=10, pady=10, anchor='s', side='right')
instruct_label_2.pack(padx=10, pady=10, anchor='s', side='right')

# On initialization
def __init__(self, root):
    self._root = root

# Insert into label
async def _insert_label(text):
    for letter in text:
        await asyncio.sleep(0.01)
        dialog_label.configure(text=dialog_label.cget('text') + str(letter))
        window.update_idletasks()
        window.update()
    dialog_label.configure(text=dialog_label.cget('text') + '\n')

# Clear text label
def _clear_label():
    dialog_label.configure(text='')

# Replacement for mainloop
async def _update_window():
    window.update_idletasks()
    window.update()

_clear_label()
while True:
    try: # A patchwerk fix for the error caused by the termination of a program in the middle of an async functions execution
        asyncio.run(_update_window())
        asyncio.run(_insert_label('Argus is my well fed child, his name comes from a game known to no child, for its story is endless in the wild'))
        asyncio.run(_insert_label('Potato'))
    except:
        print('The program has been terminated...')
        break