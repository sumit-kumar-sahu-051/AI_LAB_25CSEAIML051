# AI_LAB_25CSEAIML051

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)](https://github.com/sumit-kumar-sahu-051/AI_LAB_25CSEAIML051)
[![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-0969da?style=for-the-badge)](https://github.com/sumit-kumar-sahu-051/AI_LAB_25CSEAIML051)

---

## 📌 About

This repository serves as an engineering portfolio and coursework repository for the **Artificial Intelligence & Machine Learning Laboratory**. It features modular, idiomatic Python implementations of classical AI search strategies, combinatorial optimization, state-space exploration, constraint satisfaction, classical planning, and adversarial game-tree algorithms.

All implementations prioritize architectural clarity, algorithmic correctness, and strict adherence to formal computational principles without relying on monolithic black-box frameworks.

---

## 📋 Lab Index

| # | Experiment / Topic | Algorithm Paradigm | Source Code | Verified Output |
| :---: | :--- | :--- | :---: | :---: |
| **01** | Breadth-First Search (BFS) | Uninformed Graph Search | [`BFS.py`](BFS.py) | [`outputs/01_BFS_output.txt`](outputs/01_BFS_output.txt) |
| **02** | Depth-First Search (DFS) | Uninformed Graph Search | [`DFS.py`](DFS.py) | [`outputs/02_DFS_output.txt`](outputs/02_DFS_output.txt) |
| **03** | Depth-Limited Search (DLS) | Constrained Uninformed Search | [`DLS.py`](DLS.py) | [`outputs/03_DLS_output.txt`](outputs/03_DLS_output.txt) |
| **04** | Uniform Cost Search (UCS) | Priority-Queue Optimal Search | [`UCS.py`](UCS.py) | [`outputs/04_UCS_output.txt`](outputs/04_UCS_output.txt) |
| **05** | A* Search Algorithm | Informed / Heuristic Search | [`A_Star_Search_Algorithm.py`](A_Star_Search_Algorithm.py) | [`outputs/05_A_Star_Search_output.txt`](outputs/05_A_Star_Search_output.txt) |
| **06** | Hill Climbing Algorithm | Local Optimization | [`Hill_Climbing_Algorithm.py`](Hill_Climbing_Algorithm.py) | [`outputs/06_Hill_Climbing_output.txt`](outputs/06_Hill_Climbing_output.txt) |
| **07** | Water Jug Problem | State-Space Transition (BFS) | [`Water_Jug.py`](Water_Jug.py) | [`outputs/07_Water_Jug_output.txt`](outputs/07_Water_Jug_output.txt) |
| **08** | Eight Queens Problem | Constraint Satisfaction (Backtracking) | [`Eight_Queen.py`](Eight_Queen.py) | [`outputs/08_Eight_Queen_output.txt`](outputs/08_Eight_Queen_output.txt) |
| **09** | Traveling Salesperson Problem (TSP) | Combinatorial Optimization (Permutations) | [`TSP.py`](TSP.py) | [`outputs/09_TSP_output.txt`](outputs/09_TSP_output.txt) |
| **10** | Interactive Tic-Tac-Toe | State Evaluation & Game Loops | [`Tic_Tac_Toe.py`](Tic_Tac_Toe.py) | [`outputs/10_Tic_Tac_Toe_output.txt`](outputs/10_Tic_Tac_Toe_output.txt) |
| **11** | Block World Planning Problem | STRIPS-style Planning / State Space | [`Block_World.py`](Block_World.py) | [`outputs/11_Block_World_output.txt`](outputs/11_Block_World_output.txt) |
| **12** | Minimax Algorithm | Adversarial Decision Trees | [`Minimax_Algorithm.py`](Minimax_Algorithm.py) | [`outputs/12_Minimax_output.txt`](outputs/12_Minimax_output.txt) |
| **13** | Alpha-Beta Pruning | Adversarial Search Optimization | [`Alpha_Beta_Pruning.py`](Alpha_Beta_Pruning.py) | [`outputs/13_Alpha_Beta_Pruning_output.txt`](outputs/13_Alpha_Beta_Pruning_output.txt) |

---

## 🛠️ Prerequisites

- **Python Runtime:** Python `3.8` or higher
- **Core Standard Libraries:**
  - `collections` (`deque` for $O(1)$ state queues)
  - `heapq` (Binary min-heap for optimal cost node selection)
  - `itertools` (`permutations` for brute-force combinatorial search)
  - `math` (Mathematical bounds, infinity limits)
- **Zero Third-Party Dependencies:** No external `pip` packages required for core algorithm execution.

---

## 🚀 Installation & Execution

### 1. Clone the Repository
```bash
git clone https://github.com/sumit-kumar-sahu-051/AI_LAB_25CSEAIML051.git
cd AI_LAB_25CSEAIML051
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Execute Experiments
Run scripts directly through the Python interpreter:
```bash
# Execute Breadth-First Search
python BFS.py

# Execute A* Search Algorithm
python A_Star_Search_Algorithm.py

# Execute 8-Queens Problem
python Eight_Queen.py
```

### 4. Inspect Verified Execution Logs
Pre-recorded terminal traces with standard test vectors are accessible under the [`outputs/`](outputs/) directory:
```bash
# Windows
type outputs\01_BFS_output.txt

# Linux / macOS
cat outputs/01_BFS_output.txt
```

---

## ⚠️ Common Pitfalls to Avoid

1. **State Mutation & Visited Hashability:**
   In state-space problems (e.g., *Block World*, *Water Jug*), states must be immutable (`tuple`, `frozenset`) before hashing into `visited` lookups. Mutating states in-place corrupts graph traversal cycles and leads to non-termination.

2. **Heuristic Admissibility in A\*:**
   For guaranteed optimality in $A^*$, ensure the heuristic satisfies $h(n) \le h^*(n)$ (admissibility) and $h(n) \le c(n, a, n') + h(n')$ (consistency). An overestimating heuristic forfeits optimal path guarantees.

3. **Exponential Branching in Search Trees:**
   Unbounded search spaces (such as brute-force TSP or deep minimax game trees) scale at $O(b^d)$ or $O(n!)$. Always enforce depth limits (`DLS.py`), evaluate memoization/visited pruning, and apply branch-and-bound cutoffs (`Alpha_Beta_Pruning.py`).

4. **Terminal Evaluation Bounds in Minimax:**
   Failing to set correct infinite upper and lower bounds ($-\infty, +\infty$) on $\alpha$ and $\beta$ initialization causes premature pruning and suboptimal decision trajectories.

---

## 📄 License

This repository is distributed under the [MIT License](LICENSE).
