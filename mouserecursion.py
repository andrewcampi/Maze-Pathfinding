# Andrew Campi
# mouserecursion.py
# This file defines the mouse object, which contains functions to solve the maze.

from MazeUnsolveableError import *
from MazeStartExitError import *

class Mouse():
    def __init__(self):
        """
        The only attribute of Mouse is "solutions" which is a list of solved mazes.
        """
        self.solutions = []
    
    def find_maze_paths(self, maze, starting_row, starting_col, exit_row, exit_col):
        """ 
        Descrption: This function takes an unsolved maze, starting cordinates and exit cordinates.
                    It solves the maze by calling a recursive function and returns the solved maze.
        Attributes: maze, starting_row, starting_col, exit_row, exit_col
        Return:     maze
        """

        #Mark current position with !
        current_row = starting_row
        current_col = starting_col
        
        maze.set_value(current_row,current_col,"!")
        

        #Maze is unsolvable if ending (x,y) is a wall.
        if (maze.get_value(exit_row,exit_col) == "*"):
            raise MazeStartExitError
            
        #Maze is unsolvable if current position (x,y) is a wall.
        if (maze.get_value(current_row,current_col) == "*"):
            raise MazeStartExitError
            
        #Base Case: If current location is the exit location, the maze is solved.
        if ((current_row == exit_row) and (current_col == exit_col)):
            #Add the solved maze to the list of solved mazes
            print(maze)
            return maze
        
            
        #Determine where the walls are:
        #True = No wall exist in this direction. Mouse can move to this position.
        #False = A wall exist in this direction. 
        neighbors = [       None,         #Up
                     None,        None,   #Left, Right
                            None        ] #Down
        #Up
        if current_row-1 >= 0:
            neighbors[0] = maze.is_clear(current_row-1,current_col)
        else:
            neighbors[0] = False
        #Left
        if current_col-1 >= 0:
            neighbors[1] = maze.is_clear(current_row,current_col-1)
        else:
            neighbors[1] = False
        #Right
        if current_col+1 <= 11:
           neighbors[2] = maze.is_clear(current_row,current_col+1)
        else:
            neighbors[2] = False
        #Down
        if current_row+1 <= 11:
            neighbors[3] = maze.is_clear(current_row+1,current_col)
        else:
            neighbors[3] = False
        
        
        #Send mouse up from current position
        if neighbors[0] == True:
            self.find_maze_paths(maze.get_maze(),current_row-1,current_col, exit_row, exit_col)
        
        #Send mouse left from current position
        if neighbors[1] == True:
            self.find_maze_paths(maze.get_maze(),current_row,current_col-1, exit_row, exit_col)
        
        #Send mouse right from current position
        if neighbors[2] == True:
            self.find_maze_paths(maze.get_maze(),current_row,current_col+1, exit_row, exit_col)
        
        #Send mouse down from current position
        if neighbors[3] == True:
            self.find_maze_paths(maze.get_maze(),current_row+1,current_col, exit_row, exit_col)
        
        
