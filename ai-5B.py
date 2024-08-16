import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = 'X'
        self.board = [[None] * 3 for _ in range(3)]

        self.buttons = [[None] * 3 for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] is None and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.end_game(f"Player {self.current_player} wins!")
            elif all(self.board[row][col] is not None for row in range(3) for col in range(3)):
                self.end_game("It's a tie!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] is not None:
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True

        return False

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.current_player = 'X'
        self.board = [[None] * 3 for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
