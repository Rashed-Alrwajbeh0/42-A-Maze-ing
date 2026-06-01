"""MazeGenerator package for maze generation algorithms."""

from .Generator import MazeGenerator
from .non_perfect_maze import create_maze as imperfect_maze
from .perfect_maze import create_maze as perfect_maze
from .properties import cell, get_confing

__all__ = ['MazeGenerator', 'imperfect_maze', 'perfect_maze', 'cell', 'get_confing']
