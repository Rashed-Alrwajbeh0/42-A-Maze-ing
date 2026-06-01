import MazeGenerator as mg
import os
import random as ran


def solve() -> None:
    """Main function.
    main loop.
    """
    try:
        mg.get_confing()
        perfect_ = mg.properties.Perfect
        rows = mg.properties.Rows if mg.properties.Rows is not None else 0
        cols = mg.properties.Cols if mg.properties.Cols is not None else 0
        if mg.properties.Entry is not None:
            start = mg.properties.Entry
        else:
            start = (0, 0)

        end = mg.properties.Exit if mg.properties.Exit is not None else (0, 0)
        if mg.properties.Seed is not None:
            seed = mg.properties.Seed
        else:
            seed = ran.randint(1, 1000000)
        if mg.properties.Output_file is None:
            OutFile = "NO_Please"
        else:
            OutFile = mg.properties.Output_file
        generater = mg.MazeGenerator()
        finish = False
        colors = ["\033[32m", "\033[33m", "\033[34m", "\033[36m"]
        color = 0
        if perfect_ is None:
            return
        generater.Creatre_Maze(rows, cols, start, end, seed, perfect_)
        generater.print_the_maze(colors[color % len(colors)], "\033[30m")
        generater.make_output(OutFile)
        path = False
        path_color = "\033[0m"
        while not finish:
            print("=== A-Maze-ing ===")
            print("1. Re-generate a new maze")
            print("2. Show/Hide path from entry to exit")
            print("3. Rotate maze colors")
            print("4. Quit")
            num = input("Choice?  (1-4): ")
            if num.strip() == "1":
                os.system('clear')
                solve()
            elif num.strip() == "2":
                if not path:
                    path_color = "\033[0m"
                else:
                    path_color = "\033[30m"
                path = not path
                os.system('clear')
                generater.print_the_maze(colors[color % len(colors)],
                                         path_color)
            elif num.strip() == "3":
                os.system('clear')
                color += 1
                generater.print_the_maze(colors[color % len(colors)],
                                         path_color)
            elif num == "4":
                os._exit(0)
            else:
                print("Please enter a number in range (1-4)")
    except (FileNotFoundError, ValueError) as e:
        print(e)
        os._exit(0)


if __name__ == "__main__":
    solve()
