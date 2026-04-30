"""
Filename: game.py
Description: Various functions for the in-game experience
Version: 1.2
Author: Harspek, lauriaalt
Date: 08-03-2026
"""

import data as dt

world = dt.load("world")
player = dt.load("player")
if world or player:
    world = dt.load("data/world.json")
    player = dt.load("data/player.json")


def check_condition():
    """
    Checks for the victory condition item 'Erebus', with 3 items completing the game
    """
    if 'Erebus' in player['inv']:
        player['inv'].remove('Erebus')
        player['end'] += 1
        if player['end'] >= 3:
            dt.save('player', dt.load('data/player.json'))
            dt.save('world', dt.load('data/world.json'))
            return True

def change_location(to_move: str):
    """
    Change the location of the player to a string name
    """
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
