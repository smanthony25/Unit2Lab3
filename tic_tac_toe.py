import random as r


class TicTacToe:
    # Create the board, set the moves to zero, and set the turn to X
    def __init__(self):
        self.__board = [["." for _ in range(3)] for _ in range(3)]
        self.__moves = 0
        self.__turn = "X"

    # Create what the board looks like when printed
    def __str__(self):
        columns = ["1", "2", "3"]
        boardString = "   A   B   C\n"
        for i in range(len(self.__board)):
            boardString += columns[i] + "  "
            for j in range(len(self.__board[i])):
                boardString += self.__board[i][j]
                if j < 2:
                    boardString += " | "
            boardString += "\n"
            if i < 2:
                boardString += "  ----------"
                boardString += "\n"
        return boardString

    # Check to see who won
    def __check_win(self):
        possibleMoves = ("X", "O")
        # This code only took me 3 days and 1 whiteboard

        # Diagonal Backslash
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] in possibleMoves:
            return True
        # Diagonal Forwardslash
        elif self.__board[0][2] == self.__board[1][1] == self.__board[2][0] in possibleMoves:
            return True

        for i in range(len(self.__board)):
            # Horizontal
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] in possibleMoves:
                return True
            # Vertical
            elif self.__board[0][i] == self.__board[1][i] == self.__board[2][i] in possibleMoves:
                return True

        # You lose L bozo + ratio
        return False

    # Place the X or O in the tic-tac-toe board
    def place_token(self, location):
        rows = ["A", "B", "C"]
        pos1 = rows.index(location[0])
        pos2 = int(location[1]) - 1
        if self.__board[pos2][pos1] == ".":
            self.__board[pos2][pos1] = self.__turn
        else:
            return False

        # Change the turn
        if self.__turn == "X":
            self.__turn = "O"
        else:
            self.__turn = "X"
        self.__moves += 1
        return True

    # Check if someone has won yet
    def is_winner(self):
        if self.__check_win():
            if self.__turn == "X":
                return True, "O"
            else:
                return True, "X"
        elif self.__moves == 9:
            return True, "Tie"
        else:
            return False, ""
