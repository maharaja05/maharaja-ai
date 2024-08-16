import tkinter as tk
from tkinter import messagebox
from collections import deque

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BFS Visualization")

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.nodes = {}
        self.edges = []

        self.node_radius = 20
        self.node_positions = {}

        self.bfs_button = tk.Button(root, text="Start BFS", command=self.start_bfs)
        self.bfs_button.pack()

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

    def bfs(self, start):
        queue = deque([start])
        visited = set()
        visited.add(start)
        traversal_order = []
        paths = {start: None} 

        while queue:
            node = queue.popleft()
            traversal_order.append(node)

            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    if neighbor not in paths:
                        paths[neighbor] = node 

        return traversal_order, paths

    def get_neighbors(self, node):
        neighbors = []
        for start, end in self.edges:
            if start == node:
                neighbors.append(end)
            elif end == node:
                neighbors.append(start)
        return neighbors

    def start_bfs(self):
        start_node = 1
        traversal_order, paths = self.bfs(start_node)

        if traversal_order:
            self.highlight_nodes(traversal_order, paths)
        else:
            messagebox.showinfo("BFS", "No nodes found.")

    def highlight_nodes(self, order, paths):
        for node in order:
            x, y = self.node_positions[node]
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill='yellow', outline='black')
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 12, "bold"), fill='black')
            self.root.update()
            self.root.after(1000)  

        self.draw_paths(paths)  
    def draw_paths(self, paths):
        for node, parent in paths.items():
            if parent is not None:
                x1, y1 = self.node_positions[parent]
                x2, y2 = self.node_positions[node]
                self.canvas.create_line(x1, y1, x2, y2, fill='red', dash=(4, 4))  
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
