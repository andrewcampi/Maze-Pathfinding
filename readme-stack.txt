Andrew Campi
Project 2 Part 2 (stack)

#####EXTRA INFO:#######
This part of the project did not require removing the extra "!":
" Completely removing the unsuccessful trails involves saving a copy of local 
maze on a stack each time a cell is explored. We will not attempt to resolve 
this problem here in this project."

For extra work, I stored a copy of the maze in the stack, resulting in a final
maze that has not extra "!"
########################


----------------------------------------------(maze1.dat)
Enter the name of the maze file ("none" if  using random file): maze1.dat
maze1.dat
-------- The Original Maze --------
 012345678901
0*** ********
1***    *****
2*** **  ****
3***   *  ***
4***** ** ***
5***** ** ***
6***** ******
7*****   ****
8***   * ****
9*   **  ****
0* *    *****
1* **********


Please enter the starting row : 0
0

Please enter the starting column : 3
3

Please enter the exiting row : 11
11

Please enter the exiting column : 1
1
Sucess!
We found a path!
 012345678901
0***!********
1***!   *****
2***!**  ****
3***!!!*  ***
4*****!** ***
5*****!** ***
6*****!******
7*****!  ****
8***!!!* ****
9*!!!**  ****
0*!*    *****
1*!**********





----------------------------------------------(Maze2.dat)
Enter the name of the maze file ("none" if  using random file): maze2.dat
maze2.dat
-------- The Original Maze --------
 012345678901
0************
1***    *****
2*** **  ****
3***   *  ***
4***** ** ***
5***** ** ***
6***** ******
7*****   ****
8****  * ****
9*   **  ****
0* *    *****
1************


Please enter the starting row : 5
5

Please enter the starting column : 8
8

Please enter the exiting row : 10
10

Please enter the exiting column : 1
1
Sucess!
We found a path!
 012345678901
0************
1***!!!!*****
2***!**!!****
3***!!!*!!***
4*****!**!***
5*****!**!***
6*****!******
7*****!!!****
8****  *!****
9*!!!**!!****
0*!*!!!!*****
1************




---------------------------------------------- maze3.dat
Enter the name of the maze file ("none" if  using random file): maze3.dat
maze3.dat
-------- The Original Maze --------
 012345678901
0* *  * **** 
1**  **  ** *
2 ********   
3**   * *   *
4*  **     **
5****  ****  
6 *  * * *  *
7 *    ****  
8 *   ** * **
9  ** ***  * 
0 * * * *    
1 ***  ***   


Please enter the starting row : 1
1

Please enter the starting column : 10
10

Please enter the exiting row : 11
11

Please enter the exiting column : 5
5
Sucess!
We found a path!
 012345678901
0* *  * **** 
1**  **  **!*
2 ******** ! 
3**   * * !!*
4*  **!!!!!**
5**** !****  
6 *  *!* *  *
7 *  !!****  
8 *  !** * **
9  **!***  * 
0 * *!* *    
1 ***!!***   




----------------------------------------------random
Enter the name of the maze file ("none" if  using random file): none
none
-------- The Original Maze --------
 012345678901
0*  *   *** *
1 *   * ** * 
2   * ***  * 
3** **   ** *
4***       * 
5    ** ** * 
6  * *   *  *
7  **** *** *
8* *  *****  
9** ** **  * 
0** ** ** ***
1****** ** * 


Please enter the starting row : 8
8

Please enter the starting column : 1
1

Please enter the exiting row : 9
9

Please enter the exiting column : 11
11
Sucess!
We found a path!
 012345678901
0*  *   *** *
1 *   * ** * 
2   * ***  * 
3** **   ** *
4***!!!!!!!* 
5 !!!** **!* 
6!!* *   *!!*
7!!**** ***!*
8*!*  *****!!
9** ** **  *!
0** ** ** ***
1****** ** * 



----------------------------------------------random
Enter the name of the maze file ("none" if  using random file): none
none
-------- The Original Maze --------
 012345678901
0    ** * ***
1* * *    ***
2  *  ***** *
3*    *   ***
4 ***  * **  
5***   ***  *
6  **  * **  
7*  **    *  
8 ** *  * *  
9**    * *   
0 *     ** * 
1*   *   *  *


Please enter the starting row : 0
0

Please enter the starting column : 0
0

Please enter the exiting row : 11
11

Please enter the exiting column : 1
1
Sucess!
We found a path!
 012345678901
0!!  ** * ***
1*!* *    ***
2 !*  ***** *
3*!!!!*   ***
4 ***! * **  
5*** ! ***  *
6  **!!* **  
7*  **!   *  
8 ** *! * *  
9**   !* *   
0 * !!! ** * 
1*!!!*   *  *




----------------------------------------------random

Enter the name of the maze file ("none" if  using random file): none
none
-------- The Original Maze --------
 012345678901
0* *****  ***
1  *   **    
2* ** *  *  *
3  *** **** *
4*   **  ****
5 *** *   ** 
6 * *    ** *
7 *  ****   *
8 * **  *  **
9   ** *  ** 
0*    ** * * 
1  ***  *    


Please enter the starting row : 11
11

Please enter the starting column : 0
0

Please enter the exiting row : 5
5

Please enter the exiting column : 0
0
Sucess!
We found a path!
 012345678901
0* *****  ***
1  *   **    
2* ** *  *  *
3  *** **** *
4*   **  ****
5!*** *   ** 
6!* *    ** *
7!*  ****   *
8!* **  *  **
9!!!** *  ** 
0*!!  ** * * 
1!!***  *    