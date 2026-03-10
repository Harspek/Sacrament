"""
Filename: game.py
Description: Various functions for the in-game experience
Version: 1.0
Author: Harspek
Date: 08-03-2026
TODO: Wander, Combat
"""

import quiz as _quiz

location = {'room', 'chest', 'thingamabob'} # A location is a collection of interactable objects only known by name, the rest of the data is taken from the template file

def interact(to_interact): # Interact always returns an item, whether its through combat, a puzzle or found 
    if (to_interact == 'combat'): # A combat scenario
        return 'room'
    elif (to_interact == 'puzzle'): # A puzzle will initiate in the quiz.py, if solved, returns the reward
        if(_quiz.math_quiz()):
            return 'puzzle'
    elif(to_interact == 'object'): # Returns the object
        return 'object'
    print('Illegal object in interact found') # Printed when to_interact is not within defined possibilities
