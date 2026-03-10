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

# On initialization
def __init__(self, root):
    self._root = root

# Insert into label
def _insert_label(text):
    dialog_label.configure(text=dialog_label.cget('text') + str(text))
    dialog_label.update()

# Change button names, used to represent inventory slots
def _insert_button(text, number):
    if number == 1: custom_button_1.config(text=text)
    elif number == 2: custom_button_2.config(text=text)
    elif number == 3: custom_button_3.config(text=text)
    elif number == 4: custom_button_4.config(text=text)

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
window.config(background='lightgray')
window.iconbitmap(r".\Sacrament\Additional Files\favicon.ico")

# Instance each required widget
dialog_label = DialogLabel(window, text="Brought to you by grand Harspek... Sacrament, the truly immersive adventure of a lifetime only for those with wits, mind and an eternity if time to waste\nThis is the next row of text\nAnd a third one, just for good measure")
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

_insert_button('a',1)
_insert_button('b',2)
_insert_button('c',3)
_insert_button('d',4)

# Main loop
window.mainloop()