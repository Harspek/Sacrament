"""
Filename: game.py
Description: Various functions for the in-game experience
Version: 1.1
Author: Harspek
Date: 08-03-2026
TODO: Wander
"""

import data

player = { # Received items and current location
    'location': 'graveyard', 
    'inv': []
}

world = { # The entire world, which this file could be transferred to a JSON
    'graveyard': {
        'desc': 'You awaken in a dreadful graveyard.\nThe air is thick with the scent of decay, and the moon casts eerie shadows on the tombstones.\nYou see a path leading north.',
        'exits': {
            'north': 'pathway'
        },
        'items': ['key']
    },
    'pathway': {
        'desc': 'You are on a narrow path winding through the graveyard.\nTo the west you notice a tall church, its bells silent.\nTowards north a lack of anything fills you with a strange feeling',
        'exits': {
            'south': 'graveyard',
            'west': 'church',
            'north': 'clearing'
        },
        'items': []
    },
    'clearing': {
        'desc': 'You enter a clearing, strangely in the middle of a graveyard...',
        'exits': {
            'east': 'pathway'
        },
        'puzzle': {
            'type': 'item',
            'requirement': 'shovel',
            'message': 'You dig the ground in the middle of the clearing, discovering a buried chest',
            'reward': 'Mark of Secrets'
        }
    },
}

def __init__(self):
    #world = data.load('somefilename.json') # example
    pass
def item(): # Require an item to pass
    return True
def answer(): # Require the correct answer
    return True