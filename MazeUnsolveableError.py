#Andrew Campi
# MazeStartExitError.py
# This file defines the MazeStartExitError Exception, which is raised when the maze has no solution.

class MazeUnsolveableError(Exception):
    def __int__(self):
        pass
    def __str__(self):
        return "Maze has no solution."
