🚦 Smart City Traffic Flow Optimizer

A Smart Traffic Management Simulation System that optimizes vehicle routing, reduces congestion, and generates intelligent traffic signal schedules using classic algorithms from Design and Analysis of Algorithms (DAA).

This project simulates how a modern smart city traffic system can efficiently manage vehicles and intersections using graph-based optimization techniques.

The application provides an interactive graphical interface where users can configure intersections, define roads, add vehicles, and run optimization to visualize traffic flow.

🧠 Algorithms Implemented
1️⃣ Shortest Path Optimization

Using Dijkstra's Algorithm

Purpose:

Computes the shortest route between intersections.

Complexity:

O(V + E log V)

Implementation:

def dijkstra(graph, start)

Used to determine the minimum travel distance for each vehicle.

2️⃣ Greedy Traffic Assignment

Using Greedy Algorithm

Purpose:

Assigns vehicles to routes efficiently.
Minimizes congestion at intersections.

Implementation:

def assign_routes_greedy(vehicles, graph)

The algorithm prioritizes local optimal decisions for real-time traffic management.

3️⃣ Traffic Signal Scheduling

Using Graph Coloring with Backtracking.

Purpose:

Assign traffic signal colors so that adjacent intersections do not receive green lights simultaneously.

Implementation:

def color_signals(graph, nodes, colors)

Signal colors:

🟢 Green
🟡 Yellow
🔴 Red

This prevents signal conflicts and collisions.

🖥 Application Interface

The system is built using Tkinter to provide an interactive GUI.

Users can:

✔ Define intersections (nodes)
✔ Configure roads with weights
✔ Add multiple vehicles
✔ Run traffic optimization
✔ View route distances and congestion analysis

⚙ Features

🚗 Interactive traffic simulation

🗺 Dynamic graph configuration

📍 Shortest route calculation

🚦 Intelligent traffic signal scheduling

📊 Congestion monitoring

⚡ Real-time optimization results

🧩 Clean GUI with structured output

🏙 Example Simulation
Input

Intersections

A, B, C, D, E

Roads

A-B-4
A-C-2
B-C-5
C-D-3
D-E-6

Vehicle Routes

V1: A → E
V2: C → D
V3: B → E
Output

Optimal routes

V1: A → E Distance = 11
V2: C → D Distance = 3
V3: B → E Distance = 14

Traffic signal schedule

Intersection A → Green
Intersection B → Yellow
Intersection C → Red

Congestion summary

E : 2 vehicles incoming
D : 1 vehicle incoming
🛠 Tech Stack

Programming Language

Python

Libraries

Tkinter
heapq
random

Concepts

Graph Theory
Shortest Path Algorithms
Greedy Optimization
Backtracking
Traffic Flow Simulation
📂 Project Structure
smart-city-traffic-flow-optimizer
│
├── main.py
├── README.md
⚙ Installation

Clone the repository

git clone https://github.com/yourusername/smart-city-traffic-flow-optimizer.git

Navigate to the project directory

cd smart-city-traffic-flow-optimizer

Run the application

python main.py📊 Learning Outcomes

This project demonstrates practical applications of:

Graph algorithms
Traffic optimization techniques
Algorithm design strategies
GUI-based simulation systems
🚀 Future Improvements

Add AI-based traffic prediction

Integrate real-time traffic datasets

Convert GUI to web application

Add map visualization

Implement machine learning for congestion forecasting

👨‍💻 Author

Laghima Kejariwal

Computer Science Student
Aspiring Software Engineer
Interested in AI, Algorithms, and Smart City Systems
