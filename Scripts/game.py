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
    'inv': []
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

options = [] # Kept outside of def for usage outside of the functions loop
def print_available():
    """
    Prints out all available actions within a room for the player to do (exits, items, puzzles)
    """
    options.clear() # Reset options for the new available set
    ui._insert_label('\n')
    count = 1
    try:
        for exit in world[player['location']]['exits']: 
            ui._insert_label(f'\n{count}. Exit to {exit}')
            options.append(exit)
            count += 1 
    except KeyError:
        # Location lacks exits, which is very unlikely
        pass

    try:
        for item in world[player['location']]['items']:
            ui._insert_label(f'\n{count}. Pick up {item}')
            options.append(item)
            count += 1
    except KeyError:
        # Location lacks items
        pass

    try:
        for puzzle in world[player['location']]['puzzles']:
            if puzzle['type'] != 'hidden':
                ui._insert_label(f'\n{count}. {puzzle['desc']}')
                options.append(puzzle)
                count += 1
    except KeyError:
        # Location lacks puzzles
        pass
    
def item(): # Require an item to pass
    return True
def answer(): # Require the correct answer
    return True