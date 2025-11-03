# Smart-City-Traffic-Flow-Optimizer

🧠 A DAA-based Project using Dijkstra’s, Greedy, and Backtracking Algorithms

This project simulates a smart traffic management system that optimizes routes, manages congestion, and allocates traffic signal timings intelligently using core Design and Analysis of Algorithms (DAA) concepts.

It features a Tkinter-based GUI, where users can:

Define intersections and roads (graph structure)

Input multiple vehicles with start & end routes

Automatically compute shortest paths

Assign routes efficiently to reduce congestion

Generate non-conflicting traffic signal schedules

🧩 Table of Contents

Project Overview

Algorithms Used

Features

How It Works

Tech Stack

Installation & Usage

Example Input & Output

Screenshots

Future Enhancements

Credits

🚀 Project Overview

Urban traffic congestion is a major problem in modern cities.
This project aims to optimize urban traffic flow by combining three powerful algorithmic paradigms:

Dynamic Programming → shortest route computation (Dijkstra)

Greedy Optimization → vehicle-to-route assignment

Backtracking → signal timing conflict resolution (Graph Coloring)

The GUI allows users to visualize, simulate, and analyze how these algorithms can work together to minimize congestion and make intersections smarter.

🧮 Algorithms Used
1️⃣ Dijkstra’s Algorithm (Shortest Path)

Type: Dynamic Programming / Greedy hybrid

Purpose: Finds the shortest distance between intersections.

Complexity: O(V + E log V) using a min-heap

Used in: dijkstra()

Example: Vehicle route from A → E = 11 units

2️⃣ Greedy Vehicle Assignment

Type: Greedy Optimization

Purpose: Assigns vehicles to paths in a way that minimizes congestion.

Used in: assign_routes_greedy()

Approach:

Choose the best (least congested) route locally

Do not backtrack → ensures fast real-time scheduling

3️⃣ Graph Coloring with Backtracking

Type: Backtracking

Purpose: Assigns traffic light colors (🟢 🟡 🔴) so adjacent intersections don’t have green simultaneously.

Used in: color_signals() and is_safe()

Complexity: O(N^M) (for M colors and N nodes)

Significance: Prevents conflicting signals at connected roads.

🌟 Features

✅ Interactive GUI using Tkinter

Add intersections and roads dynamically

Input or edit vehicle routes

Clear and re-run simulations instantly

✅ Real-time Optimization

Automatic route assignment and congestion calculation

Calculates total travel distance

✅ Smart Signal Scheduling

No two adjacent nodes (roads) share the same green light

Uses backtracking-based coloring algorithm

✅ Pretty Output Formatting

Color-coded sections: routes, signals, congestion

Emojis and dividers for a professional, readable display

✅ Error Handling

Detects invalid inputs (e.g., unknown nodes, bad edge format)

Graceful fallbacks for unreachable routes

🧠 How It Works
Step 1 — Input Configuration

User defines:

Intersections (e.g., A,B,C,D,E)

Roads (e.g., A-B-4, A-C-2, B-C-5, C-D-3, D-E-6)

Vehicle start and end routes (e.g., A → E, B → C)

Step 2 — Shortest Path Calculation (Dijkstra)

Each vehicle’s shortest route is computed based on weighted edges.

Step 3 — Greedy Route Assignment

Vehicles are greedily assigned routes to minimize traffic congestion at intersections.

Step 4 — Traffic Signal Coloring (Backtracking)

Each intersection gets a signal color ensuring that no connected intersections share the same green phase.

Step 5 — Output Visualization

Results are displayed in the Tkinter text area with colored sections for:

Vehicle route summary

Route distances

Signal colors

Congestion overview
