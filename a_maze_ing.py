from print_maze import print_grid, make_output
from perfect_maze import create_maze as perfect
from non_perfect_maze import create_maze as none_perfect
import properties



try:
    properties.get_confing()
    perfect_ = properties.Perfect
    rows = properties.Rows if properties.Rows != None else 0
    cols = properties.Cols if properties.Cols != None else 0
    start = properties.Entry if properties.Entry != None else (0, 0)
    end = properties.Exit if properties.Exit != None else (0, 0)
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
