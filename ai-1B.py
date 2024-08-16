import tkinter as tk
from tkinter import messagebox
from collections import deque

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DFS Visualization")

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.nodes = {}
        self.edges = []

        self.node_radius = 20
        self.node_positions = {}

        self.dfs_button = tk.Button(root, text="Start DFS", command=self.start_dfs)
        self.dfs_button.pack()

        self.setup_graph()
        self.draw_graph()

    def setup_graph(self):
        self.nodes = {
            1: (100, 100),
            2: (200, 100),
            3: (300, 100),
            4: (200, 200),
            5: (300, 200),
            6: (400, 200),
            7: (500, 200),
        }
        self.edges = [
            (1, 2),
            (1, 3),
            (2, 4),
            (2, 5),
            (3, 6),
            (3, 7),
        ]
        self.node_positions = self.nodes

    def draw_graph(self):
        self.canvas.delete("all")

        for (x, y) in self.node_positions.values():
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill='lightblue', outline='black')

        for (start, end) in self.edges:
            x1, y1 = self.node_positions[start]
            x2, y2 = self.node_positions[end]
            self.canvas.create_line(x1, y1, x2, y2, fill='black')

        for node, (x, y) in self.node_positions.items():
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 12, "bold"))

    def dfs(self, start):
        stack = [start]
        visited = set()
        traversal_order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
               
                for neighbor in reversed(self.get_neighbors(node)):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal_order

    def get_neighbors(self, node):
        neighbors = []
        for start, end in self.edges:
            if start == node:
                neighbors.append(end)
            elif end == node:
                neighbors.append(start)
        return neighbors

    def start_dfs(self):
        start_node = 1
        traversal_order = self.dfs(start_node)

        if traversal_order:
            self.highlight_nodes(traversal_order)
        else:
            messagebox.showinfo("DFS", "No nodes found.")

    def highlight_nodes(self, order):
        for node in order:
            x, y = self.node_positions[node]
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill='lightgreen', outline='black')
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 12, "bold"), fill='black')
            self.root.update()
            self.root.after(1000) 

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
