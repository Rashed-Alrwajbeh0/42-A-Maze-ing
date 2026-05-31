from properties import cell


def print_grid(
    cells: list[cell],
    rows: int,
    cols: int,
    maze_color: str,
    answer_color: str
) -> None:

    mid_color: str = "\033[31m"
    RESET = "\033[0m"

    def idx(r: int, c: int) -> int:
        return r * cols + c

    print(maze_color, end="")

    # Top border
    print("█", end="")
    for c in range(cols):
        cur = cells[idx(0, c)]
        print("██" if cur.North else " █", end="")
    print()

    for r in range(rows):

        line = ""

        for c in range(cols):

            cur = cells[idx(r, c)]

            # West wall / corridor
            if cur.West:
                line += maze_color + "█"
            else:
                if c > 0:
                    left = cells[idx(r, c - 1)]

                    if (cur.is_answer and left.is_answer
                            and answer_color != "\033[30m"):
                        line += answer_color + "█"
                    else:
                        line += " "
                else:
                    line += " "

            # Cell interior
            if cur.special_point:
                line += mid_color + "█"
            elif cur.is_answer and answer_color != "\033[30m":
                line += answer_color + "█"

            elif cur.has_mid:
                line += mid_color + "█"

            else:
                line += maze_color + " "

        # East border
        last = cells[idx(r, cols - 1)]

        if last.East:
            line += maze_color + "█"
        else:
            line += " "

        print(line)

        # Draw vertical connections
        if r < rows - 1:

            line = ""

            for c in range(cols):

                cur = cells[idx(r, c)]
                below = cells[idx(r + 1, c)]

                line += maze_color + "█"

                if cur.South:
                    line += maze_color + "█"
                else:
                    if (cur.is_answer and below.is_answer and
                            answer_color != "\033[30m"):
                        line += answer_color + "█"
                    else:
                        line += " "

            line += maze_color + "█"

            print(line)

    # Bottom border
    print("█", end="")
    for c in range(cols):
        cur = cells[idx(rows - 1, c)]
        print("██" if cur.South else " █", end="")
    print()

    print(RESET, end="")
