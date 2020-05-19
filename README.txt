NAME : Divya Saxena
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

UTA ID : 1001773376
------------------------------------------------------------------------------------------------------------------------------------------------------------------

LANUGUAGE : Python
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

INTRODUCTION
-------------
I have implemented minimax, alpha beta pruning  and depth limited minimax for prediciting the next best move in connect4 game while playing against a human or a computer.
I have implemented the game in two modes which are interactive mode and one-move mode.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

STRUCTURE OF THE CODE
---------------------
The game uses two python files called maxconnect4.py and MaxConnect4Game.py.

maxconnect4.py has all the functions related to setting up of the game like taking inputs from the user and setting up the board and calling the ai algorithms.
MaxConnect4Game.py has all the functions which involves implementing the above ai game algorithms and implementation of the evaluation function.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GAME MODES
----------
Interactive Mode Syntax : 

$python maxconnect4.py interactive input.txt computer-next/human-next depth
Example:
python maxconnect4.py interactive input.txt human-next 1
		OR
python maxconnect4.py interactive input.txt computer-next 1

The above code will allow user to give his input and simulate the connect 4 game till all 42 moves are made and it will tell the final result as to who won and who lost.
Two files will be created as human.txt and computer.txt to represent all the moves involved in the game.


One-move Mode Syntax : 

$python maxconnect4.py one-move input_file output_file depth
Example:
python maxconnect4.py one-move input.txt output.txt 1

The above code will predict the best possible next move and make the move given an input state(input.txt). Here output.txt will be generated representing all the moves involved in the game.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Algorithm Usage Instructions 
---------------------------- 
All algorithm implementation is done in a method called aiPlay() .Default it is using Depth limited minimax with alpha beta pruning.
We can implement Plain Minimax algorithm or Minimax with alpha beta pruning by passing one extra argument in command line as follows :

By default : Depth limited minimax with alpha beta pruning
python maxconnect4.py one-move input.txt output.txt 1
		OR
python maxconnect4.py one-move input.txt output.txt 1 depth_limited

Plain Minimax algorithm(It's taking time):
python maxconnect4.py one-move input.txt output.txt 1 minimax

Minimax with alpha beta pruning(It's taking time):
python maxconnect4.py one-move input.txt output.txt 1 alpha_beta
------------------------------------------------------------------------------------------------------------------------------
Sr No | Method                                | Operation                                                                    |
1.    | self.__minimax()                        | Plain Minimax algorithm implemented                                        |
2.    | self.__alpha_beta_decision              | Minimax with alpha beta pruning implemented                                | 
3.    | self.__depth_limited_alpha_beta_pruning | Depth limited minimax with alpha beta pruning impemented                   |
------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Evaluation Function(Refer eval_explanation.txt)
-------------------
Evaluation function for depth limited minimax is implemented to calculate the utility value.
Calculation of Utility Value from the evaluation function : 
The higher the utility value then better is the decision of the computer in selecting the respective column.
First it checks for whether it can make a four, then it checks subsequently for threes and then twos. Similarly it checks for the highest possible four of the opponent and the formuala is given below :-
utility_value = (my_fours * 10 + my_threes * 5 + my_twos * 2)- (opp_fours *10 + opp_threes * 5 + opp_twos * 2).
After calculating all utility values, the highest value and the corresponding column mapped to it is selected and then the move is predicted.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DEPTH VS TIME(Refer DepthVsTime.xlsx)
-------------
An excel sheet named DepthVsTime.xlsx has a table containing the time taken and the corresponding depth level.
Time is calculated for the corresponding depth till time reaches 1 minute and then it is stopped.

After conducting the above experiment, I have observed that time will cross 1 minute at depth 8 and beyond.



