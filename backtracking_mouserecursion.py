# Andrew Campi
# backtracking_mouserecursion.py
# This file defines the mouse object, which contains functions to solve the maze.



#################################################################
#            This file is uses backtracking
#
################################################################







from MazeUnsolveableError import *
from MazeStartExitError import *

class Mouse():
    def __init__(self):
        """
        init the mouse but do not create any attributes
        """
        pass
    
    def find_maze_paths(self, maze, starting_row, starting_col, exit_row, exit_col):
        """ 
        Descrption: This function takes an unsolved maze, starting cordinates and exit cordinates.
                    It solves the maze by calling a recursive function and returns the solved maze.
        Attributes: maze, starting_row, starting_col, exit_row, exit_col
        Return:     maze
        """
        
        #Make a deep copy of the maze
        maze_local_copy = maze.get_maze()
        
        
        #Maze is unsolvable if starting (x,y) is a wall.
        if (maze.get_value(starting_row,starting_col) == "*"):
            raise MazeStartExitError
        #Maze is unsolvable if ending (x,y) is a wall.
        if (maze.get_value(exit_row,exit_col) == "*"):
            raise MazeStartExitError
        
        
        #If maze is solvable, solve the maze.
        def find_path(maze, current_row, current_col, exit_row, exit_col):
            """ 
            Descrption: This recursive function solves a maze by analyzing neighbors, relative exit direction,
                        and by using a recursive backtracking function to escape dead-ends.
            Attributes: maze, starting_row, starting_col, exit_row, exit_col
            Return:     maze
            """
            #Base Case: If current location is the exit location, the maze is solved.
            if ((current_row == exit_row) and (current_col == exit_col)):
                maze.set_value(current_row,current_col,"!")
                return maze
            
            #Determine where the walls are:
                #True = No wall exist in this direction. Mouse can move to this position.
                #False = A wall exist in this direction. 
            neighbors = [       None,         #Up
                         None,        None,   #Left, Right
                                None        ] #Down
            #Up
            neighbors[0] = maze.is_clear(current_row-1,current_col)
            #Left
            neighbors[1] = maze.is_clear(current_row,current_col-1)
            #Right
            neighbors[2] = maze.is_clear(current_row,current_col+1)
            #Down
            neighbors[3] = maze.is_clear(current_row+1,current_col)

            
            #Determine direction of the goal
            exit_direction = []
            if current_row > exit_row:
                exit_direction.append('up')
            if current_row < exit_row:
                exit_direction.append('down')
            if current_col > exit_col:
                exit_direction.append('left')
            if current_col < exit_col:
                exit_direction.append('right')
            
            #Count number of move choices (spaces)
            spaces = 0
            for x in range(len(neighbors)):
                if neighbors[x] == True:
                    spaces +=1
                    
            
            #Mark current position with !
            maze.set_value(current_row,current_col,"!")
            
            
            
            #If no spaces, backtrack to last location where there is more than one space, and choose a different direction,
            if (spaces == 0):
                def backtrack(maze, current_row, current_col, prev_direction):
                    """ 
                    Descrption: This recursive function escapes dead ends by backtracking until a alternative route
                                is found. 
                    Attributes: maze, current_row, starting_col, prev_direction
                    Return:     maze
                    """
                    #Determine surroundings
                    neighbors = [       None,         #Up
                                 None,        None,   #Left, Right
                                        None        ] #Down
                    #Up
                    neighbors[0] = maze.get_value(current_row-1,current_col)
                    #Left
                    neighbors[1] = maze.get_value(current_row,current_col-1)
                    #Right
                    neighbors[2] = maze.get_value(current_row,current_col+1)
                    #Down 
                    neighbors[3] = maze.get_value(current_row+1,current_col)
                    
                    backward_direction = None
                    for x in range(len(neighbors)):
                        if neighbors[x] == "!":
                            if x == 0:
                                backward_direction = "up"
                            elif x == 1:
                                backward_direction = "left"
                            elif x == 2:
                                backward_direction = "right"
                            elif x == 3:
                                backward_direction = "down"
                    
                    
                    #Insert "p" into neighbors list (prev_direction). Moved from ...
                    if prev_direction == "up":
                        neighbors[0] = "p"
                    elif prev_direction == "left":
                        neighbors[1] = "p"
                    elif prev_direction == "right":
                        neighbors[2] = "p"
                    elif prev_direction == "down":
                        neighbors[3] = "p"
                    
                    
                    # If current position not intersection, backtrack to backward location
                    if (" " not in neighbors):
                        #Reset current positon "!" to " ".
                        maze.set_value(current_row,current_col," ")
                        #Move to backward direction
                        if backward_direction == "up":
                            current_row-=1
                            return backtrack(maze,current_row,current_col,"down")
                        if backward_direction == "left":
                            current_col-=1
                            return backtrack(maze,current_row,current_col,"right")
                        if backward_direction == "right":
                            current_col +=1
                            return backtrack(maze,current_row,current_col,"left")
                        if backward_direction == "down":
                            current_row +=1
                            return backtrack(maze,current_row,current_col,"up")
                    
                    # Current position is an intersection (choices)
                    else:
                        #Count number of choices
                        number_of_choices = 0
                        for x in range(len(neighbors)):
                            if neighbors[x] == " ":
                                number_of_choices += 1
                        
                        #if only 1 choice, move to that location and stop backtracking.
                        if number_of_choices == 1:
                            #Determine where the choice is
                            choice_index = 0
                            for x in range(len(neighbors)):
                                if neighbors[x] == " ":
                                    choice_index = x
                            #Move in the choice_index direction
                            #Up
                            if choice_index == 0:
                                current_row -=1
                                return maze,current_row,current_col
                            #Left
                            if choice_index == 1:
                                current_col -= 1
                                return maze,current_row,current_col
                            #Right
                            if choice_index == 2:
                                current_col += 1
                                return maze,current_row,current_col
                            #Down
                            if choice_index == 3:
                                current_row += 1
                                return maze,current_row,current_col
                
                
                
                #Determine surroundings
                neighbors = [       None,         #Up
                             None,        None,   #Left, Right
                                    None        ] #Down
                #Up
                neighbors[0] = maze.get_value(current_row-1,current_col)
                #Left
                neighbors[1] = maze.get_value(current_row,current_col-1)
                #Right
                neighbors[2] = maze.get_value(current_row,current_col+1)
                #Down 
                neighbors[3] = maze.get_value(current_row+1,current_col)
                
                #Determine prev_direction.
                prev_direction_index = 0
                for x in range(len(neighbors)):
                    if neighbors[x] == "!":
                        prev_direction_index = x
                if prev_direction_index == 0:
                    prev_direction = "up"
                elif prev_direction_index == 1:
                    prev_direction = "left"
                elif prev_direction_index == 2:
                    prev_direction = "right"
                elif prev_direction_index == 3:
                    prev_direction = "down"
                
                
                maze,current_row,current_col = backtrack(maze,current_row,current_col,prev_direction)
                
                return find_path(maze, current_row, current_col, exit_row, exit_col)
            
                
                
            
            
            #if only once choice, move there
            if (spaces == 1):
                #Determine which direction is the space
                for x in range(len(neighbors)):
                    if neighbors[x] == True:
                        space_index = x
                #Go up
                if space_index == 0:
                    current_row -= 1
                #Go left
                if space_index == 1:
                    current_col -=1
                #Go right
                if space_index == 2:
                    current_col +=1
                #Go down
                if space_index == 3:
                    current_row += 1
                    
                return find_path(maze, current_row, current_col, exit_row, exit_col)
            
            
            #There is now a choice of direction (intersection). Determine direction choice based on direction of goal.
            if (spaces > 1):
                space_directions = []
                for x in range(len(neighbors)):
                    if neighbors[x] == True:
                        if x == 0:
                            space_directions.append("up")
                        elif x == 1:
                            space_directions.append("left")
                        elif x == 2:
                            space_directions.append("right")
                        elif x == 3:
                            space_directions.append("down")
                #Determine matches between the direction of the exit and the path directions open.
                direction_matches = []
                for x in range(len(exit_direction)):
                    if exit_direction[x] in space_directions:
                        direction_matches.append(exit_direction[x])
                
                #Choose the first direction in the "direction_matches" list and move to it.
                try:
                    choosen_direction = direction_matches[0]
                except:
                    raise MazeUnsolveableError
                #Go up
                if choosen_direction == "up":
                    current_row -= 1
                #Go left
                if choosen_direction == "left":
                    current_col -=1
                #Go right
                if choosen_direction == "right":
                    current_col +=1
                #Go down
                if choosen_direction == "down":
                    current_row += 1
                    
                return find_path(maze, current_row, current_col, exit_row, exit_col)
            
        
        
        
        maze = find_path(maze, starting_row, starting_col, exit_row, exit_col)
        
        return maze
