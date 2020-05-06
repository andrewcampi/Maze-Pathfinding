# Andrew Campi
# mousestack.py
# This file defines the mouse object, which contains functions to solve the maze.

from MazeUnsolveableError import *
from MazeStartExitError import *
from pyliststack import *

class Mouse():
    def __init__(self):
        pass
    
    def find_maze_paths(self, maze, starting_row, starting_col, exit_row, exit_col):
        """ 
        Descrption: This function takes an unsolved maze, starting cordinates and exit cordinates.
        Attributes: maze, starting_row, starting_col, exit_row, exit_col
        Return:     maze
        """
        #Locations are a list in the format [row,col,copy_of_maze]
        
        #Set the starting and exit_locations
        start_location = [starting_row,starting_col,maze.get_maze()]
        exit_location = [exit_row,exit_col]
        
        #Create an empty stack
        stack = Stack()
        
        #Push the start location onto the stack
        stack.push(start_location)
        
        #Solve maze with while loop
        while stack.is_empty() == False:
            current = stack.pop()
            current_row = current[0]
            current_col = current[1]
            
            #Set maze as the current copy of the maze
            maze = current[2]
            
            
            #Mark current location as vistied
            maze.set_value(current_row,current_col,"!")
            
            
            current_location = [current_row,current_col]
            if current_location == exit_location:
                maze.set_value(current_row,current_col,"!")
                print("Sucess!")
                print("We found a path!")
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
            
            
            #send mouse up from current position
            if neighbors[0] == True:
                next_location = [current_row-1,current_col,maze.get_maze()]
                stack.push(next_location)
            
            #send mouse left from current position
            if neighbors[1] == True:
                next_location = [current_row,current_col-1,maze.get_maze()]
                stack.push(next_location)
            
            #send mouse right from current position
            if neighbors[2] == True:
                next_location = [current_row,current_col+1,maze.get_maze()]
                stack.push(next_location)
            
            #send mouse down from current position
            if neighbors[3] == True:
                next_location = [current_row+1,current_col,maze.get_maze()]
                stack.push(next_location)
    
