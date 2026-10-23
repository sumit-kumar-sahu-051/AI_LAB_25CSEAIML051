# Artificial Intelligence Laboratory (AI Lab) 🤖

**Student Name:** Sumit Kumar Sahu  
**Roll / Registration Number:** `25CSEAIML051`  
**Branch / Specialization:** Computer Science & Engineering (AI & ML)  
**Repository:** [AI_LAB_25CSEAIML051](https://github.com/sumit-kumar-sahu-051/AI_LAB_25CSEAIML051)  

---

## 📌 Repository Overview

This repository contains all completed laboratory experiments for the **Artificial Intelligence (AI) Laboratory** course. Each experiment includes clean, structured Python source code, detailed problem formulation, algorithmic explanations, sample test cases, and captured terminal execution outputs.

---

## 📋 Table of Experiments

| Exp No. | Experiment Title | Category / Paradigm | Source Code | Output Log |
| :---: | :--- | :--- | :---: | :---: |
| **01** | Breadth First Search (BFS) with Target Search | Uninformed Search | [BFS.py](BFS.py) | [01_BFS_output.txt](outputs/01_BFS_output.txt) |
| **02** | Depth First Search (DFS) with Target Search | Uninformed Search | [DFS.py](DFS.py) | [02_DFS_output.txt](outputs/02_DFS_output.txt) |
| **03** | Depth Limited Search (DLS) Algorithm | Uninformed Search | [DLS.py](DLS.py) | [03_DLS_output.txt](outputs/03_DLS_output.txt) |
| **04** | Uniform Cost Search (UCS) Algorithm | Uninformed / Cost Search | [UCS.py](UCS.py) | [04_UCS_output.txt](outputs/04_UCS_output.txt) |
| **05** | A* Search Algorithm (Heuristic Search) | Informed Search | [A_Star_Search_Algorithm.py](A_Star_Search_Algorithm.py) | [05_A_Star_Search_output.txt](outputs/05_A_Star_Search_output.txt) |
| **06** | Hill Climbing Algorithm (Function Optimization) | Local Search / Optimization | [Hill_Climbing_Algorithm.py](Hill_Climbing_Algorithm.py) | [06_Hill_Climbing_output.txt](outputs/06_Hill_Climbing_output.txt) |
| **07** | Water Jug Problem Solver using BFS | State Space Search | [Water_Jug.py](Water_Jug.py) | [07_Water_Jug_output.txt](outputs/07_Water_Jug_output.txt) |
| **08** | 8-Queens Problem using Backtracking | Constraint Satisfaction | [Eight_Queen.py](Eight_Queen.py) | [08_Eight_Queen_output.txt](outputs/08_Eight_Queen_output.txt) |
| **09** | Traveling Salesman Problem (TSP) | Combinatorial Optimization | [TSP.py](TSP.py) | [09_TSP_output.txt](outputs/09_TSP_output.txt) |
| **10** | Two-Player Tic-Tac-Toe Game | Game Playing | [Tic_Tac_Toe.py](Tic_Tac_Toe.py) | [10_Tic_Tac_Toe_output.txt](outputs/10_Tic_Tac_Toe_output.txt) |
| **11** | Block World Planning Problem Solver | Classical Planning / BFS | [Block_World.py](Block_World.py) | [11_Block_World_output.txt](outputs/11_Block_World_output.txt) |
| **12** | Minimax Algorithm for Game Trees | Adversarial Search | [Minimax_Algorithm.py](Minimax_Algorithm.py) | [12_Minimax_output.txt](outputs/12_Minimax_output.txt) |
| **13** | Alpha-Beta Pruning Algorithm | Adversarial Search Optimization | [Alpha_Beta_Pruning.py](Alpha_Beta_Pruning.py) | [13_Alpha_Beta_Pruning_output.txt](outputs/13_Alpha_Beta_Pruning_output.txt) |

---

## 🔬 Detailed Experiment Descriptions & Execution Outputs

### Experiment 01: Breadth First Search (BFS) with Target Search
- **Source File:** [`BFS.py`](BFS.py)
- **Aim:** To implement Breadth First Search traversal on a user-defined graph and search for a specified target node using a queue (FIFO) data structure.
- **Algorithm Overview:**
  1. Initialize an empty visited list and a queue initialized with the starting node.
  2. Dequeue a vertex from the queue, inspect it, and check if it is the target node.
  3. If not, add all unvisited and unqueued adjacent neighbors to the queue.
  4. Repeat until the target is found or the queue is exhausted.
- **Input:**
  - Graph Edges: `4` (`A B`, `A C`, `B D`, `C E`)
  - Start Node: `A`, Target Node: `D`
- **Output:**
  ```text
  ------------BFS Graph Traversal with Target Search Program---------

  --------Build your graph--------

  How many edges (connections) does your graph have : 4

  Enter each edge separated by a space (e.g., A B) : 
  Edge 1 : A B
  Edge 2 : A C
  Edge 3 : B D
  Edge 4 : C E

  Enter the starting node for BFS : A
  Enter the target node : D

  Your graph dictionary : {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C']}

  Starting BFS traversal.......

  Exploring node : A
  Exploring node : B
  Exploring node : C
  Exploring node : D

  Target node 'D' found!

  Visited Nodes : ['A', 'B', 'C', 'D']
  ```

---

### Experiment 02: Depth First Search (DFS) with Target Search
- **Source File:** [`DFS.py`](DFS.py)
- **Aim:** To implement Depth First Search traversal on a graph and search for a given target node using a stack (LIFO) data structure.
- **Algorithm Overview:**
  1. Push the starting node onto a stack.
  2. While the stack is not empty, pop the top node.
  3. If the node has not been visited, mark it visited and check if it matches the target node.
  4. If not, push all unvisited adjacent neighbors onto the stack.
  5. Repeat until target is discovered or all reachable nodes are traversed.
- **Input:**
  - Graph Edges: `4` (`A B`, `A C`, `B D`, `C E`)
  - Start Node: `A`, Target Node: `E`
- **Output:**
  ```text
  ---------DFS Graph Traversal with Target Search Program---------

  -------Build your graph-------

  How many edges (connections) does your graph have : 4

  Enter each edge separated by a space (e.g., A B) : 
  Edge 1 : A B
  Edge 2 : A C
  Edge 3 : B D
  Edge 4 : C E

  Enter the starting node for DFS : A
  Enter the target node : E

  Your graph dictionary : {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C']}

  Starting DFS traversal.......

  Exploring node : A
  Exploring node : C
  Exploring node : E

  Target node 'E' found!

  Visited Nodes : ['A', 'C', 'E']
  ```

---

### Experiment 03: Depth Limited Search (DLS) Algorithm
- **Source File:** [`DLS.py`](DLS.py)
- **Aim:** To implement Depth Limited Search (DLS) to prevent infinite loops in infinite state spaces by setting a predefined depth cut-off limit.
- **Algorithm Overview:**
  1. Recursively traverse the graph using depth-first strategy while decrementing the depth limit.
  2. If the goal node is encountered, return `True` with the path.
  3. If the depth limit reaches 0 before finding the goal, cut off exploration on that branch and backtrack.
- **Input:**
  - Nodes: `5`, Edges: `4` (`0 1`, `0 2`, `1 3`, `2 4`)
  - Start Node: `0`, Goal Node: `3`, Depth Limit: `2`
- **Output:**
  ```text
  ===== DEPTH LIMITED SEARCH =====
  Enter number of nodes: 5
  Enter number of edges: 4
  Enter edges (source destination):
  0 1
  0 2
  1 3
  2 4
  Enter starting node: 0
  Enter goal node: 3
  Enter depth limit: 2

  Goal Found!
  Path: 0 -> 1 -> 3
  Depth: 2
  ```

---

### Experiment 04: Uniform Cost Search (UCS) Algorithm
- **Source File:** [`UCS.py`](UCS.py)
- **Aim:** To find the lowest cumulative-cost path from start node to goal node in a weighted graph using Dijkstra's / Uniform Cost Search algorithm.
- **Algorithm Overview:**
  1. Maintain a min-priority queue storing tuples of `(path_cost, current_node, path)`.
  2. At each step, pop the element with the lowest cumulative path cost g(n).
  3. If the popped node is the goal node, terminate and return the optimal path and minimum cost.
  4. Otherwise, expand neighbors, compute updated path costs, and push them to the priority queue.
- **Input:**
  - Nodes: `4`, Edges: `5` (`0 1 2`, `0 2 5`, `1 2 1`, `1 3 4`, `2 3 2`)
  - Start Node: `0`, Goal Node: `3`
- **Output:**
  ```text
  ===== UNIFORM COST SEARCH =====
  Enter number of nodes: 4
  Enter number of edges: 5
  Enter edges as:
  source destination cost
  0 1 2
  0 2 5
  1 2 1
  1 3 4
  2 3 2
  Enter starting node: 0
  Enter goal node: 3

  Goal Found!
  Optimal Path: 0 -> 1 -> 2 -> 3
  Minimum Cost: 5
  ```

---

### Experiment 05: A* Search Algorithm
- **Source File:** [`A_Star_Search_Algorithm.py`](A_Star_Search_Algorithm.py)
- **Aim:** To implement the informed A* Search algorithm using evaluation function f(n) = g(n) + h(n) to find the optimal path in a weighted graph.
- **Algorithm Overview:**
  1. Maintain an open list of candidate nodes ordered by f(n) = g(n) + h(n), where g(n) is the exact cost from start to n, and h(n) is the heuristic estimate to the goal.
  2. Select the node with the lowest f(n) value.
  3. If goal reached, reconstruct the path through parent pointers.
  4. Otherwise, relax edges to all adjacent neighbors and update lowest known g(n) costs.
- **Input:**
  - Nodes: `4` (`A` with h=3, `B` with h=2, `C` with h=1, `D` with h=0)
  - Directed Edges: `A B 1`, `A C 2`, `B D 5`, `C D 1`
  - Start: `A`, Goal: `D`
- **Output:**
  ```text
  Enter total number of nodes: 4

  Enter Heuristic values h(n) for each node: 
     Node name: A
     Heuristic value for A: 3
     Node name: B
     Heuristic value for B: 2
     Node name: C
     Heuristic value for C: 1
     Node name: D
     Heuristic value for D: 0

  Enter total number of directed edges: 4

  Enter each edge in the format:
     from_node to_node weight
     Edge 1: A B 1
     Edge 2: A C 2
     Edge 3: B D 5
     Edge 4: C D 1

  Enter start node: A
  Enter goal node: D

  Optimal path: A -> C -> D
  Total cost:  3.0
  ```

---

### Experiment 06: Hill Climbing Algorithm (Function Optimization)
- **Source File:** [`Hill_Climbing_Algorithm.py`](Hill_Climbing_Algorithm.py)
- **Aim:** To solve a continuous optimization problem using Simple Hill Climbing to maximize an objective function f(x) = -(x^2) + 10.
- **Algorithm Overview:**
  1. Start with an initial position x.
  2. Evaluate neighbors at x - step_size and x + step_size.
  3. If a neighbor yields a higher objective value than the current state, transition to that neighbor.
  4. Terminate when neither neighbor improves the objective value (local/global optimum reached) or maximum iterations are exceeded.
- **Input:**
  - Starting value: `10`, Step size: `0.5`, Maximum iterations: `50`
- **Output:**
  ```text
  Enter the starting value: 10
  Enter the step size: 0.5
  Enter maximum iterations: 50

  Best position found:  0.0
  Maximum Value =  10.0
  ```

---

### Experiment 07: Water Jug Problem Solver using BFS
- **Source File:** [`Water_Jug.py`](Water_Jug.py)
- **Aim:** To find the optimal sequence of actions to measure a target amount of water using two jugs of capacities 4L and 3L reaching state (2, 3).
- **Algorithm Overview:**
  1. Define states as tuples (j1, j2) representing current water volumes in Jug 1 and Jug 2.
  2. Enqueue the initial state (0, 0) into a queue with history tracking.
  3. At each step, generate valid transition rules: fill, empty, and pour between jugs.
  4. Perform BFS to guarantee the shortest path solution to the target state.
- **Output:**
  ```text
  Steps to reach the target state (2, 3):
  (0, 0)
  (4, 0)
  (1, 3)
  (1, 0)
  (0, 1)
  (4, 1)
  (2, 3)
  ```

---

### Experiment 08: 8-Queens Problem Solver using Backtracking
- **Source File:** [`Eight_Queen.py`](Eight_Queen.py)
- **Aim:** To place 8 non-attacking queens on an 8x8 chessboard using recursive backtracking so that no two queens share the same row, column, or diagonal.
- **Algorithm Overview:**
  1. Place queens row by row starting from row 0.
  2. For the current row, iterate across columns 0 to 7.
  3. Check if position (row, col) is safe against existing queen placements.
  4. If safe, place queen 'Q' and recursively solve for row + 1.
  5. If recursive call fails, backtrack (remove queen) and attempt subsequent columns.
- **Output:**
  ```text
  Solution for 8-Queens Problem:

  Q . . . . . . .
  . . . . Q . . .
  . . . . . . . Q
  . . . . . Q . .
  . . Q . . . . .
  . . . . . . Q .
  . Q . . . . . .
  . . . Q . . . .
  ```

---

### Experiment 09: Traveling Salesman Problem (TSP)
- **Source File:** [`TSP.py`](TSP.py)
- **Aim:** To find the minimum-cost Hamiltonian cycle visiting every city exactly once and returning to the starting city.
- **Algorithm Overview:**
  1. Take the adjacency matrix of city-to-city travel costs.
  2. Enumerate all distinct permutations of visiting intermediate cities.
  3. Compute cumulative cycle cost for each permutation including return to origin.
  4. Record and return the global minimum cost and corresponding optimal tour.
- **Input:**
  - Cities: `4`, Cost Matrix:
    ```text
    0 10 15 20
    10 0 35 25
    15 35 0 30
    20 25 30 0
    ```
  - Starting city: `0`
- **Output:**
  ```text
  Enter the number of cities: 4
  Enter the cost matrix (space-separated values for each row):
  0 10 15 20
  10 0 35 25
  15 35 0 30
  20 25 30 0
  Enter the starting city (0 to 3): 0

  Optimal path: 0 -> 1 -> 3 -> 2 -> 0
  Minimum cost: 80
  ```

---

### Experiment 10: Two-Player Tic-Tac-Toe Game
- **Source File:** [`Tic_Tac_Toe.py`](Tic_Tac_Toe.py)
- **Aim:** To implement a terminal-based two-player interactive Tic-Tac-Toe game with grid state representation and winning/draw condition evaluations.
- **Algorithm Overview:**
  1. Maintain a 3x3 grid initialized with blank characters.
  2. Alternate turns between player 'X' and player 'O'.
  3. On each valid turn, update grid and verify whether the current player achieved three in a row horizontally, vertically, or diagonally.
  4. If 9 turns elapse without a winner, terminate with a draw.
- **Sample Run Output:**
  ```text
  Player X's turn:
    |   |  
  ---------
    |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 0
  Enter column (0-2): 0

  Player O's turn:
  X |   |  
  ---------
    |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 1
  Enter column (0-2): 0

  Player X's turn:
  X |   |  
  ---------
  O |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 0
  Enter column (0-2): 1

  Player O's turn:
  X | X |  
  ---------
  O |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 1
  Enter column (0-2): 1

  Player X's turn:
  X | X |  
  ---------
  O | O |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 0
  Enter column (0-2): 2
  X | X | X
  ---------
  O | O |  
  ---------
    |   |  
  ---------

  Player X wins!
  ```

---

### Experiment 11: Block World Problem Solver
- **Source File:** [`Block_World.py`](Block_World.py)
- **Aim:** To solve the classical Block World planning problem from an arbitrary initial configuration to a target configuration using Breadth First Search state space planning.
- **Algorithm Overview:**
  1. Model states as sets of relations `(Block, Support)`, where support is another block or `"Table"`.
  2. Implement `is_clear()` predicate ensuring only unobstructed blocks can be moved.
  3. Generate valid actions: moving a clear block to the table or onto another clear block.
  4. Employ BFS on states to discover the minimal move sequence to reach the goal state.
- **Input:**
  - Blocks: `3` (`A`, `B`, `C`)
  - Initial State: `A -> Table`, `B -> A`, `C -> Table`
  - Goal State: `A -> B`, `B -> C`, `C -> Table`
- **Output:**
  ```text
  ======== BLOCK WORLD PROBLEM ========
  Enter the number of blocks: 3

  Enter block names:
  Block 1: A
  Block 2: B
  Block 3: C

  ===== INITIAL STATE =====
  Enter the position of each block.
  Enter 'Table' if the block is on the table.
  Where is A initially ? Table
  Where is B initially ? A
  Where is C initially ? Table

  ===== GOAL STATE =====
  Enter the desired position of each block.
  Where should A be in the goal state ? B
  Where should B be in the goal state ? C
  Where should C be in the goal state ? Table

  Initial State:
  C -> Table
  B -> A
  A -> Table

  Goal State:
  A -> B
  B -> C
  C -> Table

  ===== SOLUTION =====
  Step 1: Move B from A to C
  Step 2: Move A from Table to B

  Total moves: 2
  ```

---

### Experiment 12: Minimax Algorithm for Game Trees
- **Source File:** [`Minimax_Algorithm.py`](Minimax_Algorithm.py)
- **Aim:** To compute the optimal strategy and backed-up value for a two-player zero-sum game tree of height 3 using the Minimax decision rule.
- **Algorithm Overview:**
  1. Recursively evaluate nodes down to terminal leaf nodes.
  2. Maximizer layers choose the maximum value from the child evaluations.
  3. Minimizer layers choose the minimum value from the child evaluations.
  4. Backpropagate the optimal evaluation to the root.
- **Input:**
  - 8 Leaf values: `3 5 2 9 12 5 23 23`
- **Output:**
  ```text
  Enter 8 leaf node values: 3 5 2 9 12 5 23 23

  The optimal value is:  12
  ```

---

### Experiment 13: Alpha-Beta Pruning Algorithm
- **Source File:** [`Alpha_Beta_Pruning.py`](Alpha_Beta_Pruning.py)
- **Aim:** To implement the Alpha-Beta Pruning optimization on a game tree to eliminate suboptimal subtrees without altering the final minimax decision.
- **Algorithm Overview:**
  1. Maintain parameters alpha (best alternative for Maximizer) and beta (best alternative for Minimizer).
  2. At a Maximizing node, update alpha = max(alpha, child_val). If beta <= alpha, execute a beta-cutoff.
  3. At a Minimizing node, update beta = min(beta, child_val). If beta <= alpha, execute an alpha-cutoff.
- **Input:**
  - 8 Leaf values: `3 5 6 9 1 2 0 -1`
- **Output:**
  ```text
  Enter 8 leaf node values: 3 5 6 9 1 2 0 -1
  The optimal value is:  5
  ```

---

## 🚀 How to Run the Experiments

### Prerequisites
- Python 3.8 or higher installed on your system.
- Standard libraries used: `heapq`, `collections`, `itertools`, `math`. No external third-party pip dependencies required.

### Setup & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/sumit-kumar-sahu-051/AI_LAB_25CSEAIML051.git
   cd AI_LAB_25CSEAIML051
   ```

2. Run any experiment script using Python:
   ```bash
   # Example: Run Breadth First Search
   python BFS.py

   # Example: Run A* Search Algorithm
   python A_Star_Search_Algorithm.py

   # Example: Run 8-Queens Problem
   python Eight_Queen.py
   ```

---

## 👨‍💻 Author
**Sumit Kumar Sahu**  
- **Roll Number:** `25CSEAIML051`  
- **GitHub:** [@sumit-kumar-sahu-051](https://github.com/sumit-kumar-sahu-051)  
