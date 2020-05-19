import sys
import os
from MaxConnect4Game import *
import time


def oneMoveGame(gamePlan,depth,algo):
    start = time.time()
    if gamePlan.pieceCount == 42:    # Is the board full already?
        print("BOARD FULL\n\nGame Over!\n")
        sys.exit(0)

    gamePlan.aiPlay(int(depth),algo) # Make a move (only random is implemented)

    print("Game state after move:")
    gamePlan.printGameBoard()

    gamePlan.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (gamePlan.player1Score, gamePlan.player2Score))

    gamePlan.printGameBoardToFile()
    gamePlan.gameFile.close()
    print("Time take for the computers decision is")
    print(time.time() - start)


def __computer_next(gamePlan,depth,inFile,algo):
    gamePlan.aiPlay(int(depth),algo)
    gamePlan.gameFile = open("computer.txt", 'w')
    print("Computer has made a move at column " + str(gamePlan.computer_column + 1))
    gamePlan.printGameBoardToFile()
    gamePlan.gameFile.close()
    gamePlan.printGameBoard()
    gamePlan.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (gamePlan.player1Score, gamePlan.player2Score))
    interactiveGame(gamePlan, "human-next", depth, inFile,algo)


def __human_next(gamePlan,depth,inFile,algo):
    while gamePlan.checkPieceCountForInteractive() != 42:
        print("Its humans turn now")
        userMove = int(input("Enter the column number [1-7] where you would like to play : "))  # dsx
        if not 0 < userMove < 8:
            print("Invalid column number!")
            continue
        if not gamePlan.playPiece(userMove - 1):
            print("This column is full!")
            continue

        if os.path.exists("input.txt"):
            gamePlan.gameFile = open(inFile, 'r')
        else:
            game_state = "0000000\n0000000\n0000000\n0000000\n0000000\n0000000\n1"
            text_file = open("input.txt", "w")
            text_file.write(game_state)
            text_file.close()
        try:
            gamePlan.gameFile = open("human.txt", 'w')
            print("You have made a move at column ", str(userMove))
            gamePlan.printGameBoardToFile()
            gamePlan.printGameBoard()
            gamePlan.gameFile.close()
            if (gamePlan.checkPieceCountForInteractive() == 42):
                print("Game Over")
                break
            else:
                print("Computer will think " + str(depth) + " steps ahead and make a move")
                if gamePlan.currentTurn == 1:
                    gamePlan.currentTurn = 2
                elif gamePlan.currentTurn == 2:
                    gamePlan.currentTurn = 1
                gamePlan.aiPlay(int(depth),algo)
                gamePlan.gameFile = open("computer.txt", 'w')
                print("Computer has made a move at column " + str(gamePlan.computer_column + 1))
                gamePlan.printGameBoardToFile()
                gamePlan.printGameBoard()
                gamePlan.countScore()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (gamePlan.player1Score, gamePlan.player2Score))
                gamePlan.gameFile.close()
        except Exception:
            print("Exception", sys.exc_info()[0])


def __who_wins(gamePlan):
    if gamePlan.player1Score > gamePlan.player2Score:
        print("Player 1 WINS")
    elif gamePlan.player2Score > gamePlan.player1Score:
        print("Player 2 WINS")
    elif gamePlan.player1Score == gamePlan.player2Score:
        print("Its a TIE")


def interactiveGame(gamePlan,next_chance,depth,inFile,algo):
    if next_chance == "human-next":
        __human_next(gamePlan,depth,inFile,algo)
    elif next_chance == "computer-next":
        __computer_next(gamePlan,depth,inFile,algo)

    if gamePlan.checkPieceCountForInteractive() == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')

    print('Game state after move:')
    gamePlan.printGameBoard()
    gamePlan.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (gamePlan.player1Score, gamePlan.player2Score))
    __who_wins(gamePlan)


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    next_chance = argv[3]
    depth = argv[4]
    if len(argv) == 6:
         algo = argv[5]
    else:
        algo = "depth-limited"

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    gamePlan = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        gamePlan.gameFile = open(inFile, 'r')
    except IOError:
        #sys.exit("\nError opening input file.\nCheck file name.\n")
        print("Probably you do not have input file, creating game state to play")
        game_state = "0000000\n0000000\n0000000\n0000000\n0000000\n0000000\n1"
        text_file = open(inFile, "w")
        text_file.write(game_state)
        text_file.close()

    # Read the initial game state from the file and save in a 2D list
    file_lines = gamePlan.gameFile.readlines()
    gamePlan.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    gamePlan.currentTurn = int(file_lines[-1][0])
    gamePlan.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    gamePlan.printGameBoard()

    # Update a few game variables based on initial state and print the score
    gamePlan.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (gamePlan.player1Score, gamePlan.player2Score))

    if game_mode == 'interactive':
        if gamePlan.currentTurn == 1:
            print("You are playing as : "+str(gamePlan.currentTurn))
            print("COMPUTER as : "+str(2))
        elif gamePlan.currentTurn == 2:
            print("You are playing as : "+str(gamePlan.currentTurn))
            print("COMPUTER as : "+str(1))
        interactiveGame(gamePlan,next_chance,depth,inFile,algo) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            gamePlan.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(gamePlan,depth,algo) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)


