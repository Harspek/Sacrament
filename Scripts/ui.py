"""
Filename: ui.py
Description: Includes functions for UI generation and management
Version: 1.1
Author: Harspek
Date: 27-03-2026
TODO: UI
"""

import tkinter
import game
from tkinter import Tk

active = True # When active is set to false, the loop within __init__ ends, terminating the program

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
            width=12
        )
        # Bind events
        self.bind('<Enter>', self.on_hover)
        self.bind('<Leave>', self.on_leave)
        Tk.update(self)

    def on_hover(self, event):
        """Event for when button is hovered"""
        self.config(background='gray')  # Change color on hover

    def on_leave(self, event):
        """Event for when the button is unhovered"""
        self.config(background='darkgray')  # Restore original color

    def _bind_action(self, action):
        """Binds an action to the button : Be noted that an 'Event' is passed to the function, so an argument for it is required"""
        self.bind('<ButtonPress>', action)

# Additional smaller button
class AdditionButton(tkinter.Button):
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
            height=1,
            width=2
        )
        # Bind events
        self.bind('<Enter>', self.on_hover)
        self.bind('<Leave>', self.on_leave)
        Tk.update(self)

    def on_hover(self, event):
        """Event for when button is hovered"""
        self.config(background='gray')  # Change color on hover

    def on_leave(self, event):
        """Event for when the button is unhovered"""
        self.config(background='darkgray')  # Restore original color

    def _bind_action(self, action):
        """Binds an action to the button : Be noted that an 'Event' is passed to the function, so an argument for it is required"""
        self.bind('<ButtonPress>', action)

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
            width=62,    
        )
        Tk.update(self)
    def retrieve_input(self):
        return self.get()

#class init():
def __init__(self, root):
    self._root = root
    Tk.update(self)

def _on_close(): # Tkinter handles closing the window, but certain additional functionalities have to cease alongside it so the handling is moved to our code
    global active
    active = False
    print('Window has closed')

def key_handler(event): 
    """Handles keyboard events"""
    #print(event.char, event.keysym, event.keycode)
    if event.keysym == 'Return':
        input_text = custom_field.retrieve_input()
        try:
            # If the input is a value, we can assume it is relevant to selection of a currently available option
            cast_to_val = int(input_text)
            print(cast_to_val)
            pass
        except:
            # The input is not a value, so it is an answer
            print('Unable to cast to integer')
            pass

# Window creation
window = Tk()
window.state('zoomed')
window.title("Sacrament")
window.minsize(1440, 960)
window.maxsize(1920, 1920)
window.config(background='lightgray')
window.protocol('WM_DELETE_WINDOW', _on_close)
window.bind("<Key>", key_handler) # Handles keyboard input

# Instance each required widget
dialog_label = DialogLabel(window, text="Dialog Label")
custom_field = CustomField(window)
custom_button_1 = CustomButton(window, text="Look around") # This button will reveal actions
custom_button_2 = CustomButton(window, text="Check inventory") # Used when the user wants to use an item
custom_button_3 = CustomButton(window, text="Menu") # Used then the player wants to drop an item, to free up inventory slots 

# Pack widgets into window
dialog_label.place(relx=0, relheight=0.8, relwidth=1)
custom_button_1.place(relx=0.35, rely=0.9)
custom_button_2.place(relx=0.45, rely=0.9)
custom_button_3.place(relx=0.55, rely=0.9)
custom_field.place(relx=0.3, rely=0.8425)

# Clear text label
def _clear_label():
    """Clears the front textfield of all text"""
    dialog_label.configure(text='')

# Insert into label
def _insert_label(text):
    """Adds text to the front textfield"""
    dialog_label.configure(text=dialog_label.cget('text') + str(text))

# Replacement for mainloop
def _update_window():
    """Updates the user interface"""
    window.update()
