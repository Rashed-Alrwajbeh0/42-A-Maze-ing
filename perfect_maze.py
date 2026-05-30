import random
from properties import cell


def make_42(Cells: list[cell], visited: set[int],
            rows: int, cols: int) -> None:
    n = cols // 2 - 1
    m = rows // 2 - 1
    idx = cols * m + n
    Cells[idx - 2].has_mid = True
    visited.add(idx - 2)
    Cells[idx - 2 - cols].has_mid = True
    visited.add(idx - 2 - cols)
    Cells[idx - 2 + cols].has_mid = True
    visited.add(idx - 2 + cols)
    Cells[idx - 1 + cols].has_mid = True
    visited.add(idx - 1 + cols)
    Cells[idx + cols].has_mid = True
    visited.add(idx + cols)
    Cells[idx + 2 * cols].has_mid = True
    visited.add(idx + 2 * cols)
    Cells[idx + 3 * cols].has_mid = True
    visited.add(idx + 3 * cols)
    idx += 1
    Cells[idx + 1 + cols].has_mid = True
    visited.add(idx + 1 + cols)
    Cells[idx + 2 + cols].has_mid = True
    visited.add(idx + 2 + cols)
    Cells[idx + 3 + cols].has_mid = True
    visited.add(idx + 3 + cols)
    Cells[idx + 3].has_mid = True
    visited.add(idx + 3)
    Cells[idx + 3 - cols].has_mid = True
    visited.add(idx + 3 - cols)
    Cells[idx + 2 - cols].has_mid = True
    visited.add(idx + 2 - cols)
    Cells[idx + 1 - cols].has_mid = True
    visited.add(idx + 1 - cols)
    Cells[idx + 1 + 2 * cols].has_mid = True
    visited.add(idx + 1 + 2 * cols)
    Cells[idx + 1 + 3 * cols].has_mid = True
    visited.add(idx + 1 + 3 * cols)
    Cells[idx + 2 + 3 * cols].has_mid = True
    visited.add(idx + 2 + 3 * cols)
    Cells[idx + 3 + 3 * cols].has_mid = True
    visited.add(idx + 3 + 3 * cols)


def create_maze(rows: int, cols: int, start_point: tuple[int, int],
                end_point: tuple[int, int],
                seed: int | None = None) -> tuple[list[cell], list[str]]:
    if seed is None:
        random.seed(seed)
    Cells = []
    Ans = []
    visited = set()
    find_end = False
    for i in range(rows):
        for j in range(cols):
            Cells.append(cell(1, 1, 1, 1, (i, j)))

    idx1 = cols * (start_point[0] - 1) + (start_point[1] - 1)
    idx2 = cols * (end_point[0] - 1) + (end_point[1] - 1)
    visited.add(idx1)
    if cols > 7 and rows > 5:
        make_42(Cells, visited, rows, cols)
    else:
        print("ERROR: The 42 patern cannot printed in "
              "the middle of the maze, because the maze is to small")
    path = [idx1]
    while path:
        temp = ['E', 'W', 'N', 'S']
        pos1, pos2 = Cells[idx1].Point
        if pos1 == 0:
            temp.remove('N')
        if pos1 == rows - 1:
            temp.remove('S')
        if pos2 == 0:
            temp.remove('W')
        if pos2 == cols - 1:
            temp.remove('E')

        valid_moves = []
        for move in temp:
            if move == 'E' and (idx1 + 1) not in visited:
                valid_moves.append('E')
            elif move == 'W' and (idx1 - 1) not in visited:
                valid_moves.append('W')
            elif move == 'S' and (idx1 + cols) not in visited:
                valid_moves.append('S')
            elif move == 'N' and (idx1 - cols) not in visited:
                valid_moves.append('N')
        if idx1 == idx2:
            valid_moves = []
        if valid_moves:
            go = random.choice(valid_moves)
            if not find_end:
                Ans.append(go)

            if go == 'E':
                Cells[idx1].East = 0
                Cells[idx1 + 1].West = 0
                idx1 += 1
            elif go == 'W':
                Cells[idx1].West = 0
                Cells[idx1 - 1].East = 0
                idx1 -= 1
            elif go == 'S':
                Cells[idx1].South = 0
                Cells[idx1 + cols].North = 0
                idx1 += cols
            elif go == 'N':
                Cells[idx1].North = 0
                Cells[idx1 - cols].South = 0
                idx1 -= cols
            visited.add(idx1)
            path.append(idx1)
            if idx1 == idx2:
                find_end = True
                for i in path:
                    Cells[i].is_answer = True
        else:
            path.pop()
            if path:
                idx1 = path[-1]
                if Ans and not find_end:
                    Ans.pop(-1)

    return Cells, Ans
