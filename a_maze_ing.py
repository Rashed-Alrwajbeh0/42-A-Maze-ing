from print_maze import print_grid
from perfect_maze import create_maze as perfect
from properties import *

Cells, answer = perfect(rows, cols, (1, 1), (rows, cols))
print_grid(Cells, rows, cols)
print(answer)
