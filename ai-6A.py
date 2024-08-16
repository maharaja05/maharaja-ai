import tkinter as tk
from tkinter import messagebox

class MissionariesAndCannibals:
    def __init__(self, root):
        self.root = root
        self.root.title("Missionaries and Cannibals")

      
        self.missionaries_left = 3
        self.cannibals_left = 3
        self.missionaries_right = 0
        self.cannibals_right = 0
        self.boat_position = 'left' 
      
        self.canvas = tk.Canvas(root, width=600, height=400, bg='lightblue')
        self.canvas.pack()

       
        self.create_widgets()
        self.update_display()

    def create_widgets(self):
      
        tk.Label(self.root, text="Missionaries Left").pack(side='left', padx=10)
        self.missionaries_left_var = tk.IntVar(value=self.missionaries_left)
        self.missionaries_left_spinbox = tk.Spinbox(self.root, from_=0, to=self.missionaries_left, textvariable=self.missionaries_left_var, width=5)
        self.missionaries_left_spinbox.pack(side='left', padx=10)

        tk.Label(self.root, text="Cannibals Left").pack(side='left', padx=10)
        self.cannibals_left_var = tk.IntVar(value=self.cannibals_left)
        self.cannibals_left_spinbox = tk.Spinbox(self.root, from_=0, to=self.cannibals_left, textvariable=self.cannibals_left_var, width=5)
        self.cannibals_left_spinbox.pack(side='left', padx=10)

        tk.Label(self.root, text="Missionaries Right").pack(side='left', padx=10)
        self.missionaries_right_var = tk.IntVar(value=self.missionaries_right)
        self.missionaries_right_spinbox = tk.Spinbox(self.root, from_=0, to=self.missionaries_right, textvariable=self.missionaries_right_var, width=5)
        self.missionaries_right_spinbox.pack(side='left', padx=10)

        tk.Label(self.root, text="Cannibals Right").pack(side='left', padx=10)
        self.cannibals_right_var = tk.IntVar(value=self.cannibals_right)
        self.cannibals_right_spinbox = tk.Spinbox(self.root, from_=0, to=self.cannibals_right, textvariable=self.cannibals_right_var, width=5)
        self.cannibals_right_spinbox.pack(side='left', padx=10)

       
        self.move_button = tk.Button(self.root, text="Move Boat", command=self.move_boat)
        self.move_button.pack(side='left', padx=10, pady=10)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack(side='right', padx=10, pady=10)

    def update_display(self):
        self.canvas.delete("all") 
        self.draw_river()
        self.draw_boat()
        self.draw_people()
        self.check_win_condition()

    def draw_river(self):
      
        self.canvas.create_rectangle(50, 150, 550, 250, fill='blue', outline='blue')

    def draw_boat(self):
       
        boat_x = 250 if self.boat_position == 'left' else 450
        self.canvas.create_rectangle(boat_x - 30, 180, boat_x + 30, 220, fill='brown', outline='black')
        self.canvas.create_text(boat_x, 200, text="Boat", fill='white')

    def draw_people(self):
       
        self.canvas.create_text(100, 100, text=f"Left: {self.missionaries_left} Missionaries, {self.cannibals_left} Cannibals", fill='black')
      
        self.canvas.create_text(500, 100, text=f"Right: {self.missionaries_right} Missionaries, {self.cannibals_right} Cannibals", fill='black')

    def move_boat(self):
        m_left = self.missionaries_left_var.get()
        c_left = self.cannibals_left_var.get()
        m_right = self.missionaries_right_var.get()
        c_right = self.cannibals_right_var.get()

        if self.boat_position == 'left':
            self.boat_position = 'right'
          
            if m_left > 0:
                self.missionaries_left -= 1
                self.missionaries_right += 1
            if c_left > 0:
                self.cannibals_left -= 1
                self.cannibals_right += 1
        else:
            self.boat_position = 'left'
          
            if m_right > 0:
                self.missionaries_right -= 1
                self.missionaries_left += 1
            if c_right > 0:
                self.cannibals_right -= 1
                self.cannibals_left += 1
       
        self.update_display()

    def check_win_condition(self):
        if self.missionaries_left == 0 and self.cannibals_left == 0:
            messagebox.showinfo("Congratulations!", "You have solved the puzzle!")
            self.restart_game()

    def restart_game(self):
        self.missionaries_left = 3
        self.cannibals_left = 3
        self.missionaries_right = 0
        self.cannibals_right = 0
        self.boat_position = 'left'
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = MissionariesAndCannibals(root)
    root.mainloop()
