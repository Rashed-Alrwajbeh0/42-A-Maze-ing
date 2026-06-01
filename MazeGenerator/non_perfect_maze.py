import random
from properties import cell


cell_map: dict[tuple[int, int], cell] = dict()


def get_neighbors(c: cell | None) -> list[tuple[cell, str]]:
    """Return neighbors of a cell"""

    if c is None:
        return []
    row, col = c.Point
    neighbors = []

    if c.East == 0:
        neighbors.append((cell_map[(row, col + 1)], "E"))

    if c.West == 0:
        neighbors.append((cell_map[(row, col - 1)], "W"))

    if c.North == 0:
        neighbors.append((cell_map[(row - 1, col)], "N"))

    if c.South == 0:
        neighbors.append((cell_map[(row + 1, col)], "S"))

    return neighbors


def solve(cells: list[cell], start: cell,
          end: cell) -> list[str]:
    """BFS Algorithm"""

    queue: list[cell] = []
    visited: set[cell] = set()
    path: list[str] = []
    parent: dict[cell | None, cell | None] = {
        start: None
    }
    where_from: dict[cell | None, str] = dict()
    global cell_map
    cell_map = {cell.Point: cell for cell in cells}

    queue.append(start)
    visited.add(start)

    while queue:
        current: cell | None = queue.pop(0)

        if current is end:
            break

        neighbors = get_neighbors(current)
        for n in neighbors:
            if n[0] not in visited:
                parent[n[0]] = current
                queue.append(n[0])
                visited.add(n[0])
                where_from[n[0]] = n[1]

    current = end
    current.is_answer = True
    while current != start:
        path.append(where_from[current])
        current = parent[current]
        if current is not None:
            current.is_answer = True
    path.reverse()
    return path


def make_42(Cells: list[cell], visited: list[int],
            rows: int, cols: int) -> None:
    """Draw 42 in the middle"""

    n = cols // 2 - 1
    m = rows // 2 - 1
    idx = cols * m + n
    Cells[idx - 2].has_mid = True
    visited.append(idx - 2)
    Cells[idx - 2 - cols].has_mid = True
    visited.append(idx - 2 - cols)
    Cells[idx - 2 + cols].has_mid = True
    visited.append(idx - 2 + cols)
    Cells[idx - 1 + cols].has_mid = True
    visited.append(idx - 1 + cols)
    Cells[idx + cols].has_mid = True
    visited.append(idx + cols)
    Cells[idx + 2 * cols].has_mid = True
    visited.append(idx + 2 * cols)
    Cells[idx + 3 * cols].has_mid = True
    visited.append(idx + 3 * cols)
    idx += 1
    Cells[idx + 1 + cols].has_mid = True
    visited.append(idx + 1 + cols)
    Cells[idx + 2 + cols].has_mid = True
    visited.append(idx + 2 + cols)
    Cells[idx + 3 + cols].has_mid = True
    visited.append(idx + 3 + cols)
    Cells[idx + 3].has_mid = True
    visited.append(idx + 3)
    Cells[idx + 3 - cols].has_mid = True
    visited.append(idx + 3 - cols)
    Cells[idx + 2 - cols].has_mid = True
    visited.append(idx + 2 - cols)
    Cells[idx + 1 - cols].has_mid = True
    visited.append(idx + 1 - cols)
    Cells[idx + 1 + 2 * cols].has_mid = True
    visited.append(idx + 1 + 2 * cols)
    Cells[idx + 1 + 3 * cols].has_mid = True
    visited.append(idx + 1 + 3 * cols)
    Cells[idx + 2 + 3 * cols].has_mid = True
    visited.append(idx + 2 + 3 * cols)
    Cells[idx + 3 + 3 * cols].has_mid = True
    visited.append(idx + 3 + 3 * cols)


def create_maze(rows: int,
                cols: int,
                start_point: tuple[int, int],
                end_point: tuple[int, int],
                seed: int | None = None) -> tuple[list[cell], list[str]]:
    """Create a maze"""

    random.seed(seed)
    Cells = []
    visited = []
    for i in range(rows):
        for j in range(cols):
            Cells.append(cell(1, 1, 1, 1, (i, j)))

    idx1 = cols * (start_point[0] - 1) + (start_point[1] - 1)
    idx2 = cols * (end_point[0] - 1) + (end_point[1] - 1)
    if start_point[1] != cols:
        Cells[idx1].East = 0
        Cells[idx1 + 1].West = 0
    if start_point[1] != 1:
        Cells[idx1].West = 0
        Cells[idx1 - 1].East = 0
    if start_point[0] != 1:
        Cells[idx1].North = 0
        Cells[idx1 - cols].South = 0
    if start_point[0] != rows:
        Cells[idx1].South = 0
        Cells[idx1 + cols].North = 0
    if end_point[1] != cols:
        Cells[idx2].East = 0
        Cells[idx2 + 1].West = 0
    if end_point[1] != 1:
        Cells[idx2].West = 0
        Cells[idx2 - 1].East = 0
    if end_point[0] != 1:
        Cells[idx2].North = 0
        Cells[idx2 - cols].South = 0
    if end_point[0] != rows:
        Cells[idx2].South = 0
        Cells[idx2 + cols].North = 0

    visited.append(idx1)
    if cols > 7 and rows > 5:
        make_42(Cells, visited, rows, cols)
    else:
        print("ERROR: The 42 patern cannot printed in the "
              "middle of the maze, because the maze is to small")
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
            visited.append(idx1)
            path.append(idx1)
        else:
            path.pop()
            if path:
                idx1 = path[-1]
    idx1 = cols * (start_point[0] - 1) + (start_point[1] - 1)
    idx2 = cols * (end_point[0] - 1) + (end_point[1] - 1)
    Cells[idx1].special_point = True
    Cells[idx2].special_point = True
    return Cells, solve(Cells, Cells[idx1], Cells[idx2])
