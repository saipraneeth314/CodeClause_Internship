# Tic-Tac-Toe Game with Minimax AI (AI is the Maximizer)
# This is a simple implementation of a Tic-Tac-Toe game in Python.
# The game allows a human player to play against an AI opponent.
# The AI uses the Minimax algorithm to make optimal moves.
# The game checks for a winner or a draw after each move.
# GUI library in Python.
import tkinter as tk
# tkinter for showing pop-up messages
from tkinter import messagebox
# copy: Used to create a deep copy of the game board during AI's Minimax calculations.
import copy

class TicTacToe:
    # root is the main window (Tk())
    def __init__ (self, root):
        self.root = root
        self.root.title("Tic Tac Toe with AI")
        # 3x3 board initialized with empty strings
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        # Stores the 3x3 grid of tkinter button widgets.
        # 3x3 buttons initialized with None
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create the GUI widgets
        # Calls a method to create and place the buttons on the screen.
        self.create_widgets()
    
    def create_widgets(self):
        # Create a 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                # Create a button with a command to handle player moves
                button = tk.Button(self.root, text=" ", font=("Arial", 32), width=5, height=2,
                                   command=lambda row=i, col=j: self.player_move(row, col))
                # Place the button in the grid
                button.grid(row=i, column=j)
                # Store the button in the buttons list
                self.buttons[i][j] = button
    
    def player_move(self, row, col):
        if self.board[row][col] == " ":
            #update the board with the player's move
            # Places "X" on the board (user move).
            self.board[row][col] = "X"
            # Update the button text and disable it
            self.buttons[row][col].config(text="X", state="disabled")
            # Check for a win or draw
            if self.check_winner("X"):
                # If the player wins, show a message and end the game
                self.end_game("You win!")
            elif self.is_draw():
                self.end_game("It's a draw!")
            else:
                # If no win or draw, let the AI make its move after a short delay
                self.root.after(500, self.ai_move)
    
    # this is the AI random move
    # def ai_move(self):
    #     print("AI's Move (O):")
    #     while True:
    #         row = random.randint(0, 2)
    #         col = random.randint(0, 2)
    #         if self.make_move(row, col, 'O'):
    #             print(f"AI chose: ({row}, {col})")
    #             break
    
    
    # AI move using the minimax algorithm
    def ai_move(self):
    # AI wants to maximize its score (start with lowest possible value).
        self.best_score = -float("inf")
        best_move = None
        
        # Loop through the board to find the best move
        for i in range(3):
            for j in range(3):
                # check if the cell is empty
        # Temporarily make the move, run Minimax to get the score, then undo the move.
        # Uses copy.deepcopy() to avoid changing the real board.
                if self.board[i][j] == " ":
                    # simulate the move
                    self.board[i][j] = "O"
                    # calculate the score using minimax
                    score = self.minimax(copy.deepcopy(self.board), False)
                    # undo the move
                    self.board[i][j] = " "
                    # check if the score is better than the best score
                    if score > self.best_score:
                        self.best_score = score
                        best_move = (i, j)
        # make the best move
        if best_move:
            i, j = best_move
            # update the board with AI's move
            self.board[i][j] = "O"
            # update the button text and disable it
            self.buttons[i][j].config(text="O", state = "disabled")
            
            # check for a win or draw
            if self.check_winner("O"):
                self.end_game("AI wins!")
            elif self.is_draw():
                self.end_game("It's a draw!")
    
    
    # Minimax algorithm to find the best move for the AI
    def minimax(self, board, is_ai_turn):
        # method uses recursion to simulate future moves and outcomes.
        # Check for a win or draw
        if self.check_static_winner(board, "O"):
            return 1
        elif self.check_static_winner(board, "X"):
            return -1
        elif all(cell != " " for row in board for cell in row):
            return 0
        
        # If it's AI's turn, maximize the score
        if is_ai_turn:
            best_score = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        # simulate the move
                        board[i][j] = "O"
                        # calculate the score using minimax
                        score = self.minimax(board, False)
                        # undo the move
                        board[i][j] = " "
                        # update the best score
                        best_score = max(best_score, score)
            return best_score
        # If it's player's turn, minimize the score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        # simulate the move
                        board[i][j] = "X"
                        # calculate the score using minimax
                        score = self.minimax(board, True)
                        # undo the move
                        board[i][j] = " "
                        # update the best score
                        best_score = min(best_score, score)
            return best_score
    
    def check_static_winner(self, board, player):
        # Check rows and columns for a win
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return True
        # Check diagonals for a win
        return (board[0][0] == board[1][1] == board[2][2] == player or
                board[0][2] == board[1][1] == board[2][0] == player)
        
    
    # Check if the player has won
    def check_winner(self, player):
        return self.check_static_winner(self.board, player)
    
    # Check if the game is a draw
    def is_draw(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))
    
    # End the game and show a message
    def end_game(self, message):
        # show a message box with the result
        for i in range(3):
            for  j in range(3):
                self.buttons[i][j].config(state = "disabled")
        messagebox.showinfo("Game Over", message)

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    # Create an instance of the TicTacToe class
    game = TicTacToe(root)
    # Start the main loop
    root.mainloop()    