from properties import cell



def print_grid(cells: list[cell], rows: int, cols: int) -> None:
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


def make_output(cells: list[cell], ans: list[str], start: tuple[int, int],
                end: tuple[int, int], cols: int, rows: int,
                out_file: str) -> None:
    with open(out_file, "w") as file:
        for i in range(rows):
            for j in range(cols):
                idx = i * cols + j
                file.write(cells[idx].change_to_Hex())
            file.write("\n")
        file.write("\n")

        file.write(f"{start[0]}, {start[1]}\n")
        file.write(f"{end[0]}, {end[1]}\n")
        for ii in ans:
            file.write(ii)
        file.write("\n")

