#Andrew Campi
# CSCI 204 Project 2
# MazeStartExitError.py
# This file defines the MazeStartExitError Exception, which is raised when the given starting or exit location is a wall.

class MazeStartExitError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "The provided starting point or exit point cannot be a wall"

