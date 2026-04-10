"""
Filename: game.py
Description: Various functions for the in-game experience
Version: 1.1
Author: Harspek
Date: 08-03-2026
TODO: Wander
"""

import data
import ui

player = { # Received items and current location
    'location': 'clearing', 
    'inv': ['sword']
}

world = { # The entire world, which this file could be transferred to a JSON
    'graveyard': {
        'desc': 'The air is thick with the scent of decay, and the moon casts eerie shadows on the tombstones.\nYou see a path leading north.',
        'exits': ['pathway'],
        'items': ['key']
    },
    'pathway': {
        'desc': 'You are on a narrow path winding through the graveyard.\nTo the west you notice a tall church, its bells silent.\nTowards north a lack of anything fills you with a strange feeling',
        'exits': ['graveyard', 'church', 'clearing'],
        'items': []
    },
    'clearing': {
        'desc': 'You enter a clearing, strangely in the middle of a graveyard...',
        'exits': ['pathway'],
        'items': ['flower'],
        'puzzles': [
            {
                'type': 'item', 
                'desc': 'Dig with shovel',
                'requirement': 'shovel', 
                'message': 'You dig the ground in the middle of the clearing, discovering a buried chest', 
                'reward': 'Mark of Secrets'
            }
        ]
    },
}

# Information printing functions

options = [] # Kept outside of def for usage outside of the functions loop
def print_available(nil):
    """
    Prints out all available actions within a room for the player to do (exits, items, puzzles)
    """
    ui._clear_label()
    ui._insert_label(f'{world[player['location']]['desc']}\n')
    options.clear() # Reset options for the new available set
    count = 1
    location = world[player['location']] # The locations information
    if location['exits'] != []:
        for exit in location['exits']: 
            ui._insert_label(f'\n{count}. Exit to {exit}')
            options.append(exit)
            count += 1 

    if location['items'] != []:
        for item in location['items']:
            ui._insert_label(f'\n{count}. Pick up {item}')
            options.append(item)
            count += 1

    if location['puzzles']:
        for puzzle in location['puzzles']:
            if puzzle['type'] != 'hidden':
                ui._insert_label(f'\n{count}. {puzzle['desc']}')
                options.append(puzzle)
                count += 1
    
def print_inventory(nil):
    ui._clear_label()
    count = 1
    ui._insert_label(f'You check inside your bag and find...\n\n')
    for item in player['inv']:
        ui._insert_label(f'{count}. {item}\n')
        count += 1

# Puzzle functions
def _puzzle_item(): # Require an item to pass
    return True
def _puzzle_answer(): # Require the correct answer
    return True

ui.custom_button_1._bind_action(print_available)
ui.custom_button_2._bind_action(print_inventory)