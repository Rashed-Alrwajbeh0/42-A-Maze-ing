def print_grid(cells, rows, cols):
    for i in range (0,rows*cols, cols):
        string = ""
        for z in range(4):
            if z == 0:
                print("#", end="")
                for j in range(cols):
                    n = i + j
                    if cells[n].North:
                        print("##", end="")
                    else:
                        print(" #", end="")
                print()
            elif z == 1:
                for j in range(cols):
                    n = i + j
                    if cells[n].has_mid:
                        string += "#0"
                    elif cells[n].West:
                        string +="# "
                    else:
                        string += "  "
            elif z == 2:
                if cells[i + cols - 1].East:
                    string += "#"
                    print(string)
                else:
                    string += " "
                    print(string)
        if i == rows*cols - cols:
            for z in range(cols):
                if cells[n].South:
                    print("##", end="")
                else:
                    print(" #", end="")
            print("#")
