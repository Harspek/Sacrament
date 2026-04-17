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
    'location': 'graveyard', 
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
                'desc': 'Dig with shovel',
                'requirement': 'shovel', 
                'message': 'You dig the ground in the middle of the clearing, discovering a buried chest', 
                'reward': 'Mark of Secrets'
            }
        ]
    },
}

# Information printing functions

def has_in_inv(to_find: str):
    for item in player['inv']:
        if item == to_find:
            return True
    return False

options = []
def print_location(nil):
    """
    Prints out all available actions within a room for the player to do (exits, items, puzzles)
    """
    ui._clear_label()
    ui._insert_label(f'{world[player['location']]['desc']}\n')
    count = 1
    options.clear
    location = world[player['location']] # The locations information
    if 'exits' in location:
        for exit in location['exits']: 
            ui._insert_label(f'\n{count}. Exit to {exit}')
            count += 1 
            options.append({'type': 'location', 'specific': exit})

    if 'items' in location:
        for item in location['items']:
            ui._insert_label(f'\n{count}. Pick up {item}')
            count += 1
            options.append({'type': 'item', 'specific': item})

    if 'puzzles' in location:
        for puzzle in location['puzzles']:
            if has_in_inv(puzzle['requirement']):
                ui._insert_label(f'\n{count}. {puzzle['desc']}')
                count += 1
                options.append({'type': 'puzzle', 'specific': puzzle['requirement']})
    
def print_inventory(nil):
    ui._clear_label()
    ui._insert_label(f'You check inside your bag and find...\n\n')
    options.clear()
    for item in player['inv']:
        ui._insert_label(f'{item}\n')

def print_menu(nil):
    ui._clear_label()
    ui._insert_label('Sacrament\nA text adventure made by Lassi & Lauri\n\n1. Save\n 2. Load\n3. Exit')


ui.custom_button_1._bind_action(print_location)
ui.custom_button_2._bind_action(print_inventory)
ui.custom_button_3._bind_action(print_menu)