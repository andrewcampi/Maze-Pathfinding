# Andrew Campi
# maze.py
# This file defines the maze object.

"""
  Class Maze defines a general structure of a maze
  which consists of a two-dimensional array of characters.
  Each symbol on the maze represents eiehter a possible path
  or a blocker.
 
  Students need to complete this class
"""
import os
import random     # random number generator
import copy
from MazeUnsolveableError import *
current_directory = os.path.dirname(os.path.abspath(__file__))

class Maze:

    def __init__( self, maze=None,max_row = 12, max_sol = 12 ):
        """Create a maze"""
        self.MAXROW = max_row
        self.MAXCOL = max_sol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '!'

        self.PATH_BLOCKER_RATIO = 0.5
        
        if maze != None:
            self.maze = maze
        else:
            self.maze = self._gen_maze()


    def _gen_maze( self ):
        """Generate a random maze based on probability"""
        local_maze = [['*' for i in range( self.MAXROW )] \
                         for j in range( self.MAXCOL )]

        for row in range( self.MAXROW ):
            for col in range( self.MAXCOL ):
                threshold = random.random()
                if threshold > self.PATH_BLOCKER_RATIO:
                    local_maze[ row ][ col ] = self.POSSIBLEPATH
                else:
                    local_maze[ row ][ col ] = self.BLOCKER

        return local_maze


    def __str__( self ):
        """Generate a string representation of the maze"""
        s = " "
        #print col index numbers on top
        for x in range(len(self.maze)):
            s+=(str(x))[-1]
        s+="\n"
        #Print row index number and row content
        for x in range(len(self.maze)):
            s += (str(x))[-1]
            for y in range(len(self.maze[x])):
                s += self.maze[x][y]
            s += "\n"
        return s
        

    def get_col_size( self ):
        """Return column count"""
        return len(self.maze[0])


    def get_row_size( self ):
        """Return row count"""
        return len(self.maze)


    def read_maze( self, file_name ):
        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
        file_name = current_directory + "/" + file_name
        try:
            with open(file_name,'r') as file:
                maze_list = file.readlines()
                #Remove "\n" from each row
                #for x in range(len(maze_list)):
                #    maze_list[x] = maze_list[x][1:-1]
                #split each row into individual elements
                maze = []
                for x in range(len(maze_list)):
                    maze.append([])
                    for y in range(len(maze_list[x])):
                        if (maze_list[x][y] == " ") or (maze_list[x][y] == "*"):
                            maze[x].append(maze_list[x][y])
        except(FileNotFoundError):
            maze = self._gen_maze()
                
        self.maze = maze
        return self.maze
    

    def get_maze( self ):
        """Return a copy of the maze"""
        local_copy = copy.deepcopy(self.maze)
        maze = Maze(local_copy)
        return maze


    def is_clear( self, row, col ):
        """Return True if this cell is clear (pathway)."""
        try:
            if self.maze[row][col] == self.POSSIBLEPATH:
                return True
            else:
                return False
        except(IndexError):
            return False


    def is_in_maze( self, row, col ):
        """Return True if a cell is inside the maze."""
        if (row < len(self.maze)):
            if (col < len(self.maze[row])):
                return True
        return False
                

    def set_value( self, row, col, value ):
        """Set the value to a cell in the maze."""
        try:
            self.maze[row][col] = value
        except(IndexError):
            raise MazeUnsolveableError


    def get_value( self, row, col ):
        """Return the value of the current cell."""
        try:
            value = self.maze[row][col]
            return value
        except(IndexError):
            raise MazeUnsolveableError

