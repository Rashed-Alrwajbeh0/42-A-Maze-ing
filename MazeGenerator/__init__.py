"""MazeGenerator package for maze generation algorithms.

A comprehensive Python package for generating
perfect and non-perfect mazes using
depth-first search (recursive backtracker) and breadth-first search algorithms.

This package provides both low-level functions for direct maze generation and a
high-level MazeGenerator class for convenient maze creation and manipulation.

Modules:
    - Generator: Main MazeGenerator class for maze creation and output
    - perfect_maze: Functions for generating
    perfect mazes (single solution path)
    - non_perfect_maze: Functions for
    generating non-perfect mazes with BFS solving
    - properties: Cell class representing individual maze cells
    - print_maze: Terminal rendering functions for maze visualization

Key Features:
    - Generate mazes of arbitrary dimensions
    - Support for both perfect and non-perfect maze types
    - Deterministic generation using optional seeds
    - Automatic shortest path calculation using BFS
    - Hexadecimal wall encoding for compact storage
    - ASCII terminal renderer with color support
    - Special 42 pattern drawing in maze center
    - Configurable entry and exit points

Usage Examples:
    Basic maze generation with MazeGenerator class:
        >>> from MazeGenerator import MazeGenerator
        >>>
        >>> generator = MazeGenerator()
        >>> generator.Creatre_Maze(
        ...     Rows=20,
        ...     Cols=20,
        ...     Start=(1, 1),
        ...     End=(20, 20),
        ...     Seed=42,
        ...     Perfect=True
        ... )
        >>> generator.print_the_maze("green", "yellow")
        >>> generator.make_output("maze_output.txt")

Maze Types:
    Perfect Maze:
        - Has exactly one solution path between entry and exit
        - Generated using recursive backtracker (depth-first search)
        - Creates long, interesting corridors
        - Guaranteed to have a valid path from start to end

    Non-Perfect Maze:
        - Can have multiple solution paths (loops allowed)
        - Generated using modified DFS with solution via BFS
        - More complex and varied maze structures
        - Shortest path automatically calculated

Wall Encoding:
    Each cell is represented as a hexadecimal digit encoding its walls:
        - Bit 0: North wall (1 = wall, 0 = open)
        - Bit 1: East wall
        - Bit 2: South wall
        - Bit 3: West wall

    Example: 0xF = 1111 (all walls closed), 0x5 = 0101 (open East and South)

Requirements:
    - Python 3.10 or higher
    - No external dependencies

Installation:
    pip install mazegen

For more information, see the project repository:
    https://github.com/Rashed-Alrwajbeh0/42-A-Maze-ing
"""

from .Generator import MazeGenerator
from .non_perfect_maze import create_maze as imperfect_maze
from .perfect_maze import create_maze as perfect_maze
from .properties import cell, get_confing

__all__ = ['MazeGenerator',
           'imperfect_maze', 'perfect_maze', 'cell', 'get_confing']
