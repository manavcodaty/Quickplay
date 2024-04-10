#main menu
import sys
import tictactoe
import connectfour
import chess
import monopoly
import battleship
import tictactoe_multiplayer


def tictactoe_menu():
    print("Welcome to Tic Tac Toe!")
    print("1. Play single player")
    print("2. Play multiplayer")
    print("2. Quit")
    choice = int(input("Enter the number of the option you would like to select: "))
    if choice == 1:
        tictactoe.main()
    elif choice == 2:
        tictactoe_multiplayer.main()
    else:
        print("Invalid choice. Please enter a number between 1 and 2.")
        tictactoe_menu()

def main():
    print("welcome to Quickplay")
    print("1. Tic Tac Toe")
    print("2. Connect Four")
    print("3. Chess")
    print("4. Monopoly")
    print("5. Battleship")
    print("6. Quit")
    choice = int(input("Enter the number of the game you would like to play: "))
    if choice == 1:
        tictactoe_menu()
    elif choice == 2:
        connectfour.main()
    elif choice == 3:
        chess.main()
    elif choice == 4:
        monopoly.main()
    elif choice == 5:
        battleship.main()
    elif choice == 6:
        sys.exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        main()