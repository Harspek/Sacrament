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
        'exits': ['graveyard', 'church', 'clearing', 'forest'],
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
    'forest':
    {
        'desc': 'You exit the graveyards grounds and enter a vast forest, you get a sense of dread...',
        'exits': ['pathway', 'cabin', 'river'],
        'items': ['shovel']
    },
    'river':
    {
        'desc': 'You move towards a strange sound and discover... a flowing river',
        'exits': ['forest'],
        'puzzles': [ 
            {
                'desc': 'Take water with the bucket',
                'requirement': 'shovel', 
                'message': 'You dig the ground in the middle of the clearing, discovering a buried chest', 
                'reward': 'water'
            }
        ]
    },
    'cabin': {
        'desc': 'You enter the cabin in the woods, within it a simple bed, a chair and a burning fireplace',
        'exits': ['forest'],
        'items': ['bucket'],
        'puzzles': [
            {
                'desc': 'Put out the fireplace',
                'requirement': 'water',
                'message': 'You use the bucket of water to put out the fireplace and discover the Mark of Madness',
                'reward': 'Mark of Madness'

            }
        ]
    },
    'church': {
        'desc': 'You enter a grand structure, the church...\nWithin its center stands a dread icon, its form marred by empty marks',
        'exits': ['pathway'],
        'items': ['Mark of Whispers'],
        'puzzles': [
            {
                'desc': 'Give unto the icon the Mark of Madness',
                'requirement': 'Mark of Madness',
                'message': 'One mark has been returned, the dread icon is closer to awakening',
                'reward': 'Erebus'
            },
            {
                'desc': 'Give unto the icon the Mark of Whispers',
                'requirement': 'Mark of Whispers',
                'message': 'One mark has been returned, the dread icon is closer to awakening',
                'reward': 'Erebus'
            },
            {
                'desc': 'Give unto the icon the Mark of Secrets',
                'requirement': 'Mark of Secrets',
                'message': 'One mark has been returned, the dread icon is closer to awakening',
                'reward': 'Erebus'
            }
        ]
    }
}

# Information printing functions

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
            if puzzle['requirement'] in player['inv']:
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