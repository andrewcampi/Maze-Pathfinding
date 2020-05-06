# Andrew Campi
# backtracking_testmouse.py
# This file creates a maze object based on the user's inputs, then solves the maze and prints the solution.




#################################################################
#            This file is testing backtracking
#
################################################################




#from mousestack import Mouse
from backtracking_mouserecursion import Mouse
from maze import Maze



mouse = Mouse()
maze = Maze()

f_name = input( "Enter the name of the maze file (\"none\" if " \
		     + " using random file): ")
print( f_name )

#if f_name != 'none':
maze.read_maze( f_name )

print( '-------- The Original Maze --------' )
print( maze )

starting_row = int( input( 'Please enter the starting row : ' ) )
print( starting_row )
starting_col = int( input( 'Please enter the starting column : ' ) )
print( starting_col )

exit_row = int( input( 'Please enter the exiting row : ' ) )
print( exit_row )
exit_col = int( input( 'Please enter the exiting column : ' ) )
print( exit_col )

mouse.find_maze_paths( maze, starting_row, starting_col, exit_row, exit_col )

print("Sucess!")
print("We found a path!")
print(maze)
