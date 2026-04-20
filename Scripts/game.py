"""
Filename: game.py
Description: Various functions for the in-game experience
Version: 1.2
Author: Harspek
Date: 08-03-2026
"""

player = { # Received items and current location
    'location': 'graveyard', 
    'inv': ['key'],
    'end': 0
}

world = { # The entire world, which this file could be transferred to a JSON
    'graveyard': { # Location
        'desc': 'The air is thick with the scent of decay, and the moon casts eerie shadows on the tombstones.\nYou see a path leading north.', # Description of location
        'exits': ['pathway'], # Locations you can access from this one
        'items': [], # Items you can find in this location
        'puzzles': [ # Puzzle if any in the current location
            {
                'desc': 'Give unto the icon the Mark of Madness', # Description of the puzzle
                'requirement': 'Mark of Madness', # Requirements you need to complete the puzzle
                'message': 'One mark has been returned, the dread icon is closer to awakening', # Message you get from completing the puzzle
                'reward': 'Erebus' # Reward of the puzzle completion - Item / Victory condition
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
    },
    'pathway': { 
        'desc': 'You are on a narrow path winding through the graveyard.\nTo the west you notice a tall church, its bells silent.\nTowards north a lack of anything fills you with a strange feeling', 
        'exits': ['graveyard', 'church', 'clearing', 'forest'], 
        'items': [], 
        'puzzles': []
    },
    'clearing': { 
        'desc': 'You enter a clearing, strangely in the middle of a graveyard...',
        'exits': ['pathway'],
        'items': [],
        'puzzles': [ 
            {
                'desc': 'Dig with shovel', 
                'requirement': 'shovel', 
                'message': 'You dig the ground in the middle of the clearing, discovering a buried chest', 
                'reward': 'Mark of Secrets' 
            }
        ]
    },
    'forest': {
        'desc': 'You exit the graveyards grounds and enter a vast forest, you get a sense of dread...',
        'exits': ['pathway', 'cabin', 'river'],
        'items': ['shovel'],
        'puzzles': []
    },
    'river': {
        'desc': 'You move towards a strange sound and discover... a flowing river',
        'exits': ['forest'],
        'items': [],
        'puzzles': [ 
            {
                'desc': 'Take water with the bucket',
                'requirement': 'bucket', 
                'message': 'You take some water from the river into the bucket', 
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
        'desc': 'You enter a grand structure, the church...\nYou notice a locked chest upon the altar',
        'exits': ['pathway'],
        'items': [],
        'puzzles':[
            {
                'desc': 'Approach the altar... open the locked chest',
                'requirement': 'key',
                'message': 'You open the chest and discover the Mark of Whispers, one of three required to awaken the dread icon',
                'reward': 'Mark of Whispers'
            }
        ]
    }
}
def check_condition(): # Check for victory condition
    if 'Erebus' in player['inv']:
        player['inv'].remove('Erebus')
        player['end'] += 1
        if player['end'] >= 3:
            return True
