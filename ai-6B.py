import tkinter as tk
from tkinter import messagebox
import random

class NumberPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Puzzle Game")

        
        self.tiles = list(range(1, 9)) + [0]  
        self.goal = list(range(1, 9)) + [0]
        self.create_widgets()
        self.shuffle_puzzle()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=6, height=3, command=lambda i=i, j=j: self.move_tile(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        self.update_buttons()

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                value = self.tiles[i * 3 + j]
                self.buttons[i][j].config(text="" if value == 0 else str(value))

    def find_zero(self):
        index = self.tiles.index(0)
        return index // 3, index % 3

    def move_tile(self, i, j):
        zero_i, zero_j = self.find_zero()
        if (abs(i - zero_i) == 1 and j == zero_j) or (abs(j - zero_j) == 1 and i == zero_i):
            self.tiles[zero_i * 3 + zero_j], self.tiles[i * 3 + j] = self.tiles[i * 3 + j], self.tiles[zero_i * 3 + zero_j]
            self.update_buttons()
            if self.tiles == self.goal:
                messagebox.showinfo("Congratulations!", "You have solved the puzzle!")

    def shuffle_puzzle(self):
        random.shuffle(self.tiles)
        while not self.is_solvable() or self.tiles == self.goal:
            random.shuffle(self.tiles)
        self.update_buttons()

    def is_solvable(self):
        inversions = 0
        one_d_tiles = [tile for tile in self.tiles if tile != 0]
        for i in range(len(one_d_tiles)):
            for j in range(i + 1, len(one_d_tiles)):
                if one_d_tiles[i] > one_d_tiles[j]:
                    inversions += 1
        return inversions % 2 == 0

def main():
    root = tk.Tk()
    app = NumberPuzzleGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
