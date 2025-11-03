import tkinter as tk
from tkinter import ttk, messagebox
import heapq
import random

# ------------------------------
# Algorithm Section (Unchanged - uses Dijkstra and Graph Coloring)
# ------------------------------
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > dist[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist


def assign_routes_greedy(vehicles, graph):
    assignments = {}
    congestion = {node: 0 for node in graph}

    for vehicle_id, (start, end) in vehicles.items():
        # If start or end missing in graph, mark unreachable
        if start not in graph or end not in graph:
            assignments[vehicle_id] = (start, end, float('inf'))
            continue

        distances = dijkstra(graph, start)
        route_length = distances.get(end, float('inf'))

        assignments[vehicle_id] = (start, end, route_length)
        # Count congestion only if reachable
        if route_length != float('inf'):
            # NOTE: For simplicity, we only count congestion at the destination node in this greedy assignment.
            congestion[end] += 1 

    return assignments, congestion


def is_safe(node, color, graph, colors):
    # neighbor list contains tuples (neighbor, weight)
    for neighbor, _ in graph[node]:
        if neighbor in colors and colors[neighbor] == color:
            return False
    return True


def color_signals(graph, nodes, colors, node_index=0, max_colors=3):
    if node_index == len(nodes):
        return True
    node = nodes[node_index]
    for color in range(1, max_colors + 1):
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if color_signals(graph, nodes, colors, node_index + 1, max_colors):
                return True
            colors.pop(node)
    return False


# ------------------------------
# Tkinter Frontend Section (Modified)
# ------------------------------
class TrafficApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🚦 Smart City Traffic Flow Optimizer")
        self.root.geometry("900x750") # Increased height
        self.root.config(bg="#0D1117")

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#0D1117", foreground="#F0F6FC", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        style.configure("TEntry", padding=4)

        # Title
        title = ttk.Label(root, text="🚗 SMART CITY TRAFFIC FLOW OPTIMIZER", font=("Segoe UI", 18, "bold"), foreground="#58A6FF", background="#0D1117")
        title.pack(pady=12)

        # Main Frame
        main_frame = ttk.Frame(root)
        main_frame.pack(pady=8, padx=12, fill="x")

        # --- Graph Input Frame ---
        graph_frame = ttk.LabelFrame(main_frame, text="🗺️ Map Configuration")
        graph_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(graph_frame, text="🛣️ Intersections (A,B,C...):").grid(row=0, column=0, sticky="w", padx=6, pady=6)
        self.nodes_entry = ttk.Entry(graph_frame, width=30)
        self.nodes_entry.grid(row=0, column=1, padx=6, pady=6)
        self.nodes_entry.insert(0, "A,B,C,D,E") 

        ttk.Label(graph_frame, text="🧭 Roads (A-B-5, B-C-2...):").grid(row=1, column=0, sticky="w", padx=6, pady=6)
        self.edges_entry = ttk.Entry(graph_frame, width=30)
        self.edges_entry.grid(row=1, column=1, padx=6, pady=6)
        self.edges_entry.insert(0, "A-B-4, A-C-2, B-C-5, C-D-3, D-E-6")

        # --- Vehicle Input Frame ---
        vehicle_frame = ttk.LabelFrame(main_frame, text="🚕 Vehicle Routes (User Input)")
        vehicle_frame.pack(fill="x", padx=10, pady=10)
        
        self.create_vehicle_input(vehicle_frame)
        
        # --- Run Button ---
        ttk.Button(root, text="⚙️ Run Optimization", command=self.run_optimizer).pack(pady=12)

        # --- Output Box ---
        self.output_box = tk.Text(root, width=105, height=25, bg="#161B22", fg="#C9D1D9", font=("Consolas", 10), bd=0, padx=10, pady=10)
        self.output_box.pack(padx=12, pady=10)

        # Define text tag styles
        self.output_box.tag_configure("header", foreground="#58A6FF", font=("Consolas", 11, "bold"))
        self.output_box.tag_configure("divider", foreground="#6E7681")
        self.output_box.tag_configure("vehicle", foreground="#39D353")
        self.output_box.tag_configure("route", foreground="#FFB86C")
        self.output_box.tag_configure("signal", foreground="#FF6B81")
        self.output_box.tag_configure("congestion", foreground="#8BE9FD")
        self.output_box.tag_configure("error", foreground="#FF5555", font=("Consolas", 10, "bold"))

    def create_vehicle_input(self, parent_frame):
        # Frame for new entry inputs
        entry_frame = ttk.Frame(parent_frame)
        entry_frame.pack(pady=5, padx=5, fill="x")

        ttk.Label(entry_frame, text="Start Node:").pack(side=tk.LEFT, padx=5)
        self.start_node_entry = ttk.Entry(entry_frame, width=10)
        self.start_node_entry.pack(side=tk.LEFT, padx=5)
        self.start_node_entry.insert(0, "A")

        ttk.Label(entry_frame, text="End Node:").pack(side=tk.LEFT, padx=5)
        self.end_node_entry = ttk.Entry(entry_frame, width=10)
        self.end_node_entry.pack(side=tk.LEFT, padx=5)
        self.end_node_entry.insert(0, "E")

        ttk.Button(entry_frame, text="Add Route ➕", command=self.add_route).pack(side=tk.LEFT, padx=15)
        ttk.Button(entry_frame, text="Clear All Routes 🗑️", command=self.clear_routes).pack(side=tk.LEFT, padx=5)

        # Treeview for displaying and managing routes
        cols = ("Vehicle ID", "Start Node", "End Node")
        self.route_tree = ttk.Treeview(parent_frame, columns=cols, show="headings", height=5)
        
        for col in cols:
            self.route_tree.heading(col, text=col)
            self.route_tree.column(col, anchor=tk.CENTER, width=100)
        
        self.route_tree.pack(fill="x", padx=10, pady=5)
        
        # Add a default example route
        self.route_tree.insert("", tk.END, values=(f"V1", "A", "E"))
        self.route_tree.insert("", tk.END, values=(f"V2", "C", "D"))
        self.route_tree.insert("", tk.END, values=(f"V3", "B", "E"))


    def add_route(self):
        start = self.start_node_entry.get().strip().upper()
        end = self.end_node_entry.get().strip().upper()
        
        if not start or not end:
            messagebox.showwarning("Input Warning", "Start and End nodes cannot be empty.")
            return

        # Simple validation: Nodes should be single characters for a clear graph
        if len(start) > 1 or len(end) > 1:
            messagebox.showwarning("Input Warning", "Please use single characters for Start/End nodes (e.g., A, B, C).")
            return
            
        # Determine the next vehicle ID
        current_routes = self.route_tree.get_children()
        next_id = len(current_routes) + 1
        vehicle_id = f"V{next_id}"
        
        self.route_tree.insert("", tk.END, values=(vehicle_id, start, end))
        self.start_node_entry.delete(0, tk.END)
        self.end_node_entry.delete(0, tk.END)
        self.start_node_entry.insert(0, start) # Keep last start node for convenience

    def clear_routes(self):
        for item in self.route_tree.get_children():
            self.route_tree.delete(item)

    def parse_vehicle_routes(self):
        vehicles = {}
        for item in self.route_tree.get_children():
            vehicle_id, start_node, end_node = self.route_tree.item(item, 'values')
            vehicles[vehicle_id] = (start_node, end_node)
        return vehicles

    def run_optimizer(self):
        # Parse nodes and graph (same as original)
        raw_nodes = self.nodes_entry.get().strip()
        if not raw_nodes:
            messagebox.showerror("Input Error", "Please enter at least one intersection.")
            return
        nodes = [n.strip() for n in raw_nodes.split(',') if n.strip()]
        if len(nodes) == 0:
            messagebox.showerror("Input Error", "Please enter valid intersection names.")
            return

        raw_edges = self.edges_entry.get().strip()
        edge_list = [e.strip() for e in raw_edges.split(',') if e.strip()]
        graph = {n: [] for n in nodes}

        for e in edge_list:
            try:
                a, b, w = e.split('-')
                a = a.strip(); b = b.strip(); w = int(w.strip())
                if a not in graph or b not in graph:
                    messagebox.showerror("Input Error", f"Edge references unknown node: {e}")
                    return
                # Since this is undirected; add both ways
                graph[a].append((b, w))
                graph[b].append((a, w))
            except ValueError:
                messagebox.showerror("Input Error", f"Invalid edge format: {e}\nUse A-B-5")
                return

        # Parse user-defined vehicles (NEW: calls the parser function)
        vehicles = self.parse_vehicle_routes()
        if not vehicles:
            messagebox.showerror("Input Error", "Please add at least one vehicle route.")
            return

        # Run algorithms (same as original)
        assignments, congestion = assign_routes_greedy(vehicles, graph)
        colors = {}
        # Note: Graph coloring should check that all nodes in the graph are considered.
        success = color_signals(graph, nodes, colors, 0, max_colors=3) 
        if not success:
            colors = {n: 1 for n in nodes}

        # Output formatting (same as original)
        self.output_box.delete("1.0", tk.END)

        # VEHICLE REQUESTS
        self.output_box.insert(tk.END, "\n🚗 VEHICLE ROUTE REQUESTS (User-Defined)\n", "header")
        self.output_box.insert(tk.END, "────────────────────────────────────────\n", "divider")
        for v, (s, e) in vehicles.items():
            self.output_box.insert(tk.END, f"{v}: {s} → {e}\n", "vehicle")

        # ROUTE ASSIGNMENTS
        self.output_box.insert(tk.END, "\n📍 OPTIMAL ROUTE ASSIGNMENTS (Dijkstra + Greedy)\n", "header")
        self.output_box.insert(tk.END, "──────────────────────────────────────────────\n", "divider")
        total_distance = 0
        
        for v, (s, e, l) in assignments.items():
            if l == float('inf'):
                self.output_box.insert(tk.END, f"{v}: {s} → {e}, Distance = unreachable\n", "error")
            else:
                self.output_box.insert(tk.END, f"{v}: {s} → {e}, Distance = {l}\n", "route")
                total_distance += l

        self.output_box.insert(tk.END, f"\nTotal Network Distance: {total_distance}\n", "header")

        # TRAFFIC SIGNALS
        self.output_box.insert(tk.END, "\n🚦 TRAFFIC SIGNAL COLORS (Graph Coloring)\n", "header")
        self.output_box.insert(tk.END, "──────────────────────────────────────────────\n", "divider")
        color_names = {1: "🟢 Green", 2: "🟡 Yellow", 3: "🔴 Red"}
        for node in nodes:
            c = colors.get(node, 1)
            self.output_box.insert(tk.END, f"Intersection {node}: {color_names.get(c, '🔴 Red')}\n", "signal")

        # CONGESTION SUMMARY
        self.output_box.insert(tk.END, "\n📊 CONGESTION SUMMARY\n", "header")
        self.output_box.insert(tk.END, "───────────────────────\n", "divider")
        for node in nodes:
            count = congestion.get(node, 0)
            self.output_box.insert(tk.END, f"{node}: {count} vehicles incoming\n", "congestion")


# ------------------------------
# Run App
# ------------------------------
def main():
    root = tk.Tk()
    app = TrafficApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()