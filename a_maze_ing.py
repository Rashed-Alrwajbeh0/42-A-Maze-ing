from print_maze import print_grid, make_output
from perfect_maze import create_maze as perfect
from non_perfect_maze import create_maze as none_perfect
import properties

try:
    properties.get_confing()
    perfect_ = properties.Perfect
    rows = properties.Rows
    cols = properties.Cols
    start = properties.Entry
    end = properties.Exit
    seed = properties.Seed
    out_file = properties.Output_file
    if perfect_:
        Cells, answer = perfect(rows, cols, start, end, seed)
    else:
        Cells = none_perfect(rows, cols, start, end, seed)
    print_grid(Cells, rows, cols)
    #make_output(Cells, answer,  start, end, cols, rows, out_file)

except (FileNotFoundError, ValueError) as e:
    print(e)
