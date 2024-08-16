import tkinter as tk
from tkinter import messagebox

class TowerOfHanoiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower of Hanoi")

        self.num_disks = 3
        self.pegs = {'A': list(range(self.num_disks, 0, -1)), 'B': [], 'C': []}
        self.peg_positions = {'A': (100, 300), 'B': (300, 300), 'C': (500, 300)}
        self.selected_disk = None
        self.canvas = tk.Canvas(root, width=700, height=400, bg='white')
        self.canvas.pack()

        self.setup_ui()

    def setup_ui(self):
        self.draw_pegs()
        self.draw_disks()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_pegs(self):
        self.canvas.delete("all")
        for peg, pos in self.peg_positions.items():
            x, y = pos
            self.canvas.create_rectangle(x - 10, y - 100, x + 10, y, fill='black')
            self.canvas.create_text(x, y + 20, text=f"Peg {peg}", font=("Arial", 12))

    def draw_disks(self):
        self.canvas.delete("disks")
        for peg, disks in self.pegs.items():
            x, y = self.peg_positions[peg]
            for i, disk in enumerate(disks):
                self.canvas.create_rectangle(x - disk * 10, y - (i + 1) * 20,
                                             x + disk * 10, y - i * 20,
                                             fill='lightblue', outline='black', tags="disks")
                self.canvas.create_text(x, y - (i + 1) * 20 + 10, text=str(disk), font=("Arial", 10), tags="disks")

    def handle_click(self, event):
        x, y = event.x, event.y
        clicked_peg = self.get_clicked_peg(x, y)

        if not clicked_peg:
            return

        if self.selected_disk is None:
            self.select_disk(clicked_peg)
        else:
            self.move_disk(clicked_peg)

    def select_disk(self, peg):
        if self.pegs[peg]:
            self.selected_disk = self.pegs[peg][-1]
            self.canvas.create_oval(self.peg_positions[peg][0] - 20, self.peg_positions[peg][1] - 20,
                                    self.peg_positions[peg][0] + 20, self.peg_positions[peg][1] + 20,
                                    fill='red', outline='black', tags="moving")

    def move_disk(self, target_peg):
        if self.is_valid_move(self.selected_disk, target_peg):
            source_peg = self.get_current_peg(self.selected_disk)
            self.pegs[target_peg].append(self.pegs[source_peg].pop())
            self.canvas.delete("moving")
            self.selected_disk = None
            self.draw_disks()
        else:
            messagebox.showerror("Invalid Move", "Cannot move disk to the selected peg.")

    def get_clicked_peg(self, x, y):
        for peg, pos in self.peg_positions.items():
            peg_x, peg_y = pos
            if peg_x - 10 < x < peg_x + 10 and peg_y - 100 < y < peg_y:
                return peg
        return None

    def get_current_peg(self, disk):
        for peg, disks in self.pegs.items():
            if disk in disks:
                return peg
        return None

    def is_valid_move(self, disk, target_peg):
        source_peg = self.get_current_peg(disk)
        if not self.pegs[target_peg] or self.pegs[target_peg][-1] > disk:
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = TowerOfHanoiApp(root)
    root.mainloop()
