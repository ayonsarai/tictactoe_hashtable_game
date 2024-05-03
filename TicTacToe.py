# Sarai Ayon
# 5/3/2024
# CS 2302  Lab 5 B
# Chapter 5 : Hash Tables

# This code creates a `TicTacToe` class with methods for displaying the board, 
# placing marks, switching players, checking for a winner, and checking for a draw. 
# The game is played until a player wins or it's a draw.

class TicTacToe:
    def __init__(self):
        self.board = {}
        self.current_player = 'X'
        self.winner = None

        # Initialize the board with empty spaces
        for row in range(3):
            for col in range(3):
                self.board[(row, col)] = ' '

    def display_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[(row, col)], end=' ')
                if col < 2:
                    print('|', end=' ')
            print()
            if row < 2:
                print('-' * 5)

    def place_mark(self, row, col):
        if self.board[(row, col)] == ' ':
            self.board[(row, col)] = self.current_player
            self.check_winner(row, col)
            if not self.winner:
                self.switch_player()
        else:
            print("That position is already taken. Try again.")

    def switch_player(self):
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def check_winner(self, last_row, last_col):
        # Check row
        if self.board[(last_row, 0)] == self.board[(last_row, 1)] == self.board[(last_row, 2)] != ' ':
            self.winner = self.current_player
        # Check column
        elif self.board[(0, last_col)] == self.board[(1, last_col)] == self.board[(2, last_col)] != ' ':
            self.winner = self.current_player
        # Check diagonal
        elif (last_row, last_col) in [(0, 0), (1, 1), (2, 2)] and \
             self.board[(0, 0)] == self.board[(1, 1)] == self.board[(2, 2)] != ' ':
            self.winner = self.current_player
        elif (last_row, last_col) in [(0, 2), (1, 1), (2, 0)] and \
             self.board[(0, 2)] == self.board[(1, 1)] == self.board[(2, 0)] != ' ':
            self.winner = self.current_player

    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[(row, col)] == ' ':
                    return False
        return True

    def play(self):
        while not self.winner and not self.check_draw():
            self.display_board()
            print(f"Player {self.current_player}'s turn:")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            self.place_mark(row, col)

        self.display_board()
        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a draw!")


# Test the TicTacToe class
game = TicTacToe()
game.play()
