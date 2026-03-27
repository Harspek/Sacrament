"""
Filename: ui.py
Description: Includes functions for UI generation and management
Version: 1.0
Author: Harspek
Date: 27-03-2026
TODO: UI
"""

import tkinter
from tkinter import Tk

# Button
class CustomButton(tkinter.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='solid',
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
        Tk.update(self)

    def on_hover(self, event):
        self.config(background='gray')  # Change color on hover

    def on_leave(self, event):
        self.config(background='darkgray')  # Restore original color

# Label utilized as console replacement
class DialogLabel(tkinter.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='solid',
            bd=1,
            highlightthickness=0,  # Remove highlight
            padx=10,  # Add horizontal padding
            pady=5,  # Add vertical padding
            font=('Roboto Slab', 16),  # Set font
            foreground='black',  # Text color
            background='darkgray',  # Background color
        )
        Tk.update(self)

# Label utilized for instucting on UI elements
class InstructionLabel(tkinter.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='solid',
            bd=0,
            highlightthickness=0,  # Remove highlight
            padx=10,  # Add horizontal padding
            pady=5,  # Add vertical padding
            font=('Roboto Slab', 16),  # Set font
            foreground='black',  # Text color
            background='lightgray',  # Background color
        )
        Tk.update(self)

# Text field
class CustomField(tkinter.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief='solid',
            bd=1,
            highlightthickness=0,  # Remove highlight
            font=('Roboto Slab', 16),  # Set font
            foreground='black',  # Text color
            background='darkgray',  # Background color
            width=50,    
        )
        Tk.update(self)

#class init():
def __init__(self, root):
    self._root = root
    Tk.update(self)

# Window creation
window = Tk()
window.state('zoomed')
window.title("Sacrament")
window.minsize(1440, 960)
window.maxsize(1920, 1920)
window.config(background='lightgray')

def _as_updated(part):
    Tk.update(part)
    return part

# Instance each required widget
dialog_label = _as_updated(DialogLabel(window, text="Dialog Label"))
custom_field = _as_updated(CustomField(window))
custom_button_1 = _as_updated(CustomButton(window, text="1"))
custom_button_2 = _as_updated(CustomButton(window, text="2"))
custom_button_3 = _as_updated(CustomButton(window, text="3"))
custom_button_4 = _as_updated(CustomButton(window, text="4"))
instruct_label_1 = _as_updated(InstructionLabel(window, text='Inventory'))
instruct_label_2 = _as_updated(InstructionLabel(window, text='Dialog Box'))

# Pack widgets into window
dialog_label.place(relx=0, relheight=0.8, relwidth=1)
custom_button_1.place(relx=0.3925, rely=0.9)
custom_button_2.place(relx=0.4475, rely=0.9)
custom_button_3.place(relx=0.5025, rely=0.9)
custom_button_4.place(relx=0.5575, rely=0.9)
custom_field.place(relx=0.35, rely=0.8425)

#custom_field.pack(padx=10, pady=50, anchor='s', side='right')
#custom_button_4.pack(padx=10, pady=10, anchor='s', side='right')
#instruct_label_2.pack(padx=10, pady=10, anchor='s', side='right')

# Clear text label
def _clear_label():
    dialog_label.configure(text='')

# Insert into label
def _insert_label(text):
    dialog_label.configure(text=dialog_label.cget('text') + str(text))

# Replacement for mainloop
def _update_window():
    window.update()