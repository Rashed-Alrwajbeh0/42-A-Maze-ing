from print_maze import print_grid
from perfect_maze import create_maze as perfect
import properties

try:
    properties.get_confing()
    perfect_ = properties.Perfect
    rows = properties.Rows
    cols = properties.Cols
    start = properties.Entry
    end = properties.Exit
    seed = properties.Seed
    if perfect_:
        Cells, answer = perfect(rows, cols, start, end, seed)
        print_grid(Cells, rows, cols)
        print(answer)
except (FileNotFoundError, ValueError) as e:
    print(e)
