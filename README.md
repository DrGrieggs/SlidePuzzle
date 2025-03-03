# Slide Puzzle Solver Assignment

## Overview
In this assignment, you will implement a search algorithm to solve an image-based slide puzzle. The starter code provides a functional slide puzzle game with a GUI, but the solving mechanism currently uses a random search strategy which is inefficient and often fails to find a solution.

Your task is to replace the random search in the `solve_game()` method with an intelligent search algorithm that we've discussed in class (e.g., BFS, DFS, A*, etc.).

## Assignment Goals
- Apply search algorithms to solve a practical problem
- Understand state space representation in puzzles
- Implement heuristic functions for informed search
- Analyze and compare algorithm performance

## Getting Started
1. Download the starter code (`slide_puzzle.py`)
2. Make sure you have the required dependencies installed:
   ```
   pip install pillow numpy
   ```
3. Run the program to familiarize yourself with the game:
   ```
   python slide_puzzle.py
   ```
4. The game uses a 3x3 grid with a black tile representing the empty space
5. You can manually solve the puzzle by clicking adjacent tiles to move them into the empty space
6. The "Shuffle" button randomizes the puzzle
7. The "Solve Game" button currently uses a random search (your job is to improve this)

## Requirements

### Core Requirements (70%)
1. Implement a working search algorithm in the `solve_game()` method that reliably solves the puzzle
2. Your solution should handle the 3x3 puzzle size and find a solution in a reasonable amount of time (under 1 minute)
3. Include clear comments explaining your approach and algorithm choice

### Implementation Options (Choose One)
- **Breadth-First Search (BFS)** - Guaranteed to find the shortest path but may use significant memory
- **Depth-First Search (DFS)** - Memory efficient but may not find the optimal solution 
- **A* Search** - Combines BFS with heuristics to search more efficiently
- **Iterative Deepening** - Combines advantages of BFS and DFS
- **Other algorithms** discussed in class (with instructor approval)

### Technical Details
Your implementation must:
- Create a proper state representation of the puzzle
- Track visited states to avoid cycles
- Implement a state transition model that only allows valid moves
- Reconstruct and execute the solution path once found
- Display the solution on the GUI by making the actual moves

## Bonus Challenge (30%)
- **Efficiency Bonus**: The student whose solution solves the puzzle in the fewest average moves will receive a bonus of 15%
- **Algorithm Comparison**: For an additional 15% bonus, implement two different search algorithms and include a written analysis (1-2 pages) comparing their performance across 10 different puzzle configurations, including:
  - Number of nodes expanded
  - Solution path length
  - Execution time
  - Memory usage (if possible)

## Heuristic Functions
If implementing an informed search algorithm like A*, consider using one of these heuristics:
1. **Manhattan Distance**: Sum of horizontal and vertical distances from each tile to its goal position
2. **Misplaced Tiles**: Number of tiles not in their goal position
3. **Linear Conflict**: Extension of Manhattan distance that accounts for tiles in the correct row/column but in the wrong order

## Tips for Success
- Start by designing your state representation carefully
- Test with simple puzzle configurations first
- Optimize your visited states tracking (consider using frozenset or tuple representations)
- For A* search, the heuristic function quality significantly impacts performance
- The 8-puzzle (3x3) has 9!/2 ≈ 181,440 possible states, making complete exploration feasible
- Track your algorithm's metrics to compare with classmates

## Submission Guidelines
1. Submit your completed Python file on the course platform
2. Include a written report (PDF, 2-3 pages) that:
   - Explains your solution approach in detail
   - Justifies your algorithm choice with reasoning
   - Describes any optimizations or special techniques you implemented
   - Discusses challenges you encountered and how you addressed them
   - Analyzes the performance of your algorithm (time complexity, space complexity)
   - Includes example runs with statistics (nodes expanded, solution length, time taken)
   - For bonus: comparison data and analysis of different algorithms

## Grading Criteria
- **Correctness (35%)**: Solution correctly solves puzzles
- **Implementation Quality (25%)**: Code is well-structured and commented
- **Efficiency (20%)**: Solution finds answers in reasonable time with minimal unnecessary exploration
- **Written Report (20%)**: Clear explanation of your approach, algorithm choice, and analysis
- **Bonus (up to 30%)**: As described in the Bonus Challenge section

## Deadline
The assignment is due **[INSTRUCTOR: INSERT DATE HERE]** at 11:59 PM.

Good luck, and happy searching!
