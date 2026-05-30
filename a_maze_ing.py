from print_maze import print_grid, make_output
from perfect_maze import create_maze as perfect
from non_perfect_maze import create_maze as none_perfect
import properties


try:
    properties.get_confing()
    perfect_ = properties.Perfect
    rows = properties.Rows if properties.Rows is not None else 0
    cols = properties.Cols if properties.Cols is not None else 0
    start = properties.Entry if properties.Entry is not None else (0, 0)
    end = properties.Exit if properties.Exit is not None else (0, 0)
    seed = properties.Seed
    if properties.Output_file is None:
        OutFile = "NO_Please"
    else:
        OutFile = properties.Output_file
    if perfect_:
        Cells, answer = perfect(rows, cols, start, end, seed)
    else:
        Cells, answer = none_perfect(rows, cols, start, end, seed)
    print_grid(Cells, rows, cols)
    make_output(Cells, answer,  start, end, cols, rows, OutFile)

except (FileNotFoundError, ValueError) as e:
    print(e)
