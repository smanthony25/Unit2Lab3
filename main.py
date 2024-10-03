# Sean A
# Tic Tac Toe
# Using multidimensional arrays create a tictactoe game

import tic_tac_toe

import random as r
import os as s


def playerMove(game):
    nums = ["1", "2", "3"]
    chars = ["A", "B", "C"]
    print("Where would you like to play?")
    print("Please choose a column and row (ex. B3)")
    pos = input("> ").upper()
    if len(pos) == 2:
        if pos[0] not in chars or pos[1] not in nums:
            print("Invalid Input, please try again")
        else:
            if game.place_token(pos):
                return True
            else:
                print("This spot has already been taken!")
    else:
        print("Invalid Input, please try again")
    return playerMove(game)


def makeMove(game):
    chars = ["A", "B", "C"]
    nums = ["1", "2", "3"]
    pos = r.choice(chars) + r.choice(nums)
    while not game.place_token(pos):
        pos = r.choice(chars) + r.choice(nums)

    return pos


def welcome():
    s.system("clear")
    print("Welcome to Tic Tac Toe!")
    print("You will be playing against the program")
    print("Please press ENTER to continue")
    input()
    s.system("clear")


def endGame(game, winner):
    s.system("clear")
    print(game)
    if winner == "Tie":
        print("The game resulted in a draw, try again next time!")
    elif winner == "X":
        print(f"YOU WIN! Play again to keep your streak!")
    elif winner == "O":
        print(f"The computer won! Try again next time!")
    print()
    print("GAME OVER")


def main():
    game = tic_tac_toe.TicTacToe()
    gameWon = False
    welcome()
    print(game)
    while not gameWon:
        playerMove(game)
        s.system("clear")
        gameWon, winner = game.is_winner()
        if not gameWon:
            pos = makeMove(game)
            gameWon, winner = game.is_winner()
            print(game)
            print(f"Your opponent chose {pos}")
    endGame(game, winner)


if __name__ == "__main__":
    main()
