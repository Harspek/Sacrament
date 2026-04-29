"""
Filename: game.py
Description: Various functions for the in-game experience
Version: 1.2
Author: Harspek
Date: 08-03-2026
"""

from data import load

player = load("data/player.json")

world = load("data/world.json")

def check_condition(): # Check for victory condition
    if 'Erebus' in player['inv']:
        player['inv'].remove('Erebus')
        player['end'] += 1
        if player['end'] >= 3:
            return True

def change_location(to_move: str):
    player['location'] = to_move

def add_item(item: str):
    """
    Add an item to the player inventory based on the passed string
    """
    player['inv'].append(item)
    
def remove_item(item: str):
    """
    Remove an item from the player inventory based on the passed string
    """
    try:
        player['inv'].remove(item)
    except IndexError:
        print('The item does not exist')
