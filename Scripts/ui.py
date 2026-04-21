"""
Filename: ui.py
Description: Includes functions for UI generation and management
Version: 1.2
Author: Harspek
Date: 27-03-2026
TODO: UI
"""

import tkinter
from tkinter import Tk
import game # Handles the backend gameplay
import data # Handles the data management

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
    """
    Handles keyboard events
    """
    if event.keysym == 'Return':
        input_text = custom_field.retrieve_input()
        try:
            # If the input is a value, we can assume it is relevant to selection of a currently available option
            option = options[int(input_text) - 1]
            if option['type'] == 'location': # If the option is defined as a location, the user is set to that location and the information is printed
                game.change_location(option['specific'])
                print_location('')

            elif option['type'] == 'item': # If the option is defined as an item, the item is added to their inventory
                game.add_item(option['specific'])
                game.world[game.player['location']]['items'].remove(option['specific'])
                print_location('')
                _insert_label(f'\n\nYou took the {option['specific']}')

            elif option['type'] == 'puzzle': # If the option is a puzzle, which is only visible if the correct item is available, the item can be exchanged for another item
                puzzle = game.world[game.player['location']] ['puzzles'] [option['specific']]
                game.remove_item(puzzle['requirement'])
                game.add_item(puzzle['reward'])
                label_text = puzzle['message'] # Has to be separated from the puzzle before its removal
                game.world[game.player['location']] ['puzzles'].pop(option['specific'])
                print_location('')
                _insert_label(f'\n\n{label_text}')

                if game.check_condition():
                    window.destroy()
                    print('Annihilation...\n - THE END -')
            
            elif option['type'] == 'menu': # WHen in the menu the save, load and exit options are available
                
                if option['specific'] == 'save': # Save the data to the "player" and "world" files, this will overwrite previous ones
                    data.save('player', game.player)
                    data.save('world', game.world)
                    print_menu('')
                    _insert_label('\n\nSaved data')

                elif option['specific'] == 'load': # Load the data from the "player" and "world" files, wont load any data if no save exists 
                    game.player = data.load('player')
                    game.world = data.load('world')
                    print_menu('')
                    _insert_label('\n\nLoaded data')
                
                elif option['specific'] == 'exit': # Close the program
                    window.destroy()

        except ValueError:
            # The input is not a value, and as such the input is passed
            pass


# Window creation
window = Tk()
window.state('zoomed') # The window is taken into focus
window.title("Sacrament") # Entitles the window with the program name
window.minsize(1440, 960) # Sets minimum size, so that the UI is not broken
window.maxsize(1920, 1920) # Sets maximum size, the program is not intended for dual monitors
window.config(background='lightgray') # Sets the basic background for the UI
window.protocol('WM_DELETE_WINDOW', _on_close) # Adds an event to when the program is closed to prevent further code execution
window.bind("<Key>", key_handler) # Handles keyboard input

# Instance each required widget
dialog_label = DialogLabel(window, text="Dialog Label")
custom_field = CustomField(window)
custom_button_1 = CustomButton(window, text="Look around") # This button will reveal actions
custom_button_2 = CustomButton(window, text="Check inventory") # Used when the user wants to use an item
custom_button_3 = CustomButton(window, text="Menu") # Used then the player wants to drop an item, to free up inventory slots 

# Pack widgets into window; Pack is not ideal but grants greatest control over positioning
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

# Replacement for Tkinter's mainloop for greater control over the program
def _update_window():
    """Updates the user interface"""
    window.update()

# Text information functionalities
options = [] # Stores all available options for actions
def print_location(nil):
    """
    Prints out all available actions within a room for the player to do (exits, items, puzzles)
    """
    _clear_label()
    _insert_label(f'{game.world[game.player['location']]['desc']}\n')
    count = 1
    options.clear()
    location = game.world[game.player['location']] # The locations information
    if 'exits' in location: # Checking for attached rooms
        for exit in location['exits']: 
            _insert_label(f'\n{count}. Exit to {exit}')
            count += 1 
            options.append({'type': 'location', 'specific': exit})

    if 'items' in location: # Checking for items within the location
        for item in location['items']:
            _insert_label(f'\n{count}. Pick up {item}')
            count += 1
            options.append({'type': 'item', 'specific': item})

    if 'puzzles' in location: # Checking for puzzles available for completion
        i = 0
        for puzzle in location['puzzles']:
            if puzzle['requirement'] in game.player['inv']:
                _insert_label(f'\n{count}. {puzzle['desc']}')
                count += 1
                options.append({'type': 'puzzle', 'specific': i})
                i += 1 # This value is used to match the puzzle from the list of puzzles
    
def print_inventory(nil):
    """
    Prints the contents of the inventory; Pass an empty value to the nil variable
    """
    _clear_label()
    _insert_label(f'You check inside your bag and find...\n\n')
    options.clear()
    for item in game.player['inv']:
        _insert_label(f'{item}\n')

def print_menu(nil):
    """
    Prints the menu options; Pass an empty value to the nil variable
    """
    _clear_label()
    _insert_label('Sacrament\nA text adventure made by Lassi & Lauri\n\n1. Save\n 2. Load\n3. Exit')
    options.clear()
    options.append({'type': 'menu', 'specific': 'save'})
    options.append({'type': 'menu', 'specific': 'load'})
    options.append({'type': 'menu', 'specific': 'exit'})

# Binding to UI
custom_button_1._bind_action(print_location)
custom_button_2._bind_action(print_inventory)
custom_button_3._bind_action(print_menu)