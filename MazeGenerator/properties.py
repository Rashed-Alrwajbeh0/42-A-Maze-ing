class cell:
    """Class for cells"""

    def __init__(self, E: int, W: int, N: int, S: int,
                 Point: tuple[int, int]) -> None:
        """Initialization"""

        self.East = E
        self.West = W
        self.North = N
        self.South = S
        self.Point = Point
        self.has_mid = False
        self.is_answer = False
        self.special_point = False

    def change_to_Hex(self) -> str:
        """Print info as hex"""

        Hex_nums = "0123456789ABCDEF"
        idx = 0
        if self.North:
            idx += 1
        if self.East:
            idx += 2
        if self.South:
            idx += 4
        if self.West:
            idx += 8
        return Hex_nums[idx]


Rows = None
Cols = None
Entry = None
Exit = None
Output_file = None
Perfect = None
Seed = None


def get_confing() -> bool | Exception:
    """Function to get config.txt"""

    import sys
    argv = sys.argv
    if len(argv) > 2:
        raise FileNotFoundError("ERROR: a_maze_ing.py and config.txt are must"
                                " just exist, but you enter more !!")
    elif len(argv) < 2:
        raise FileNotFoundError("Error: a_maze_ing.py and config.txt are "
                                "must exist, but you didn't enter"
                                " config.txt !!")
    elif argv[1] != "config.txt":
        raise FileNotFoundError("ERROR: config.txt must exist, "
                                "it isn't found !!")
    file = open(argv[1], "r")
    global Rows, Cols, Entry, Exit, Output_file, Perfect, Seed
    content = file.read().strip().split("\n")
    for ii in content:
        i = ii.strip()
        if i and i[0] == "#" or i == "":
            if "SEED" in i.upper():
                Seed = None
            continue
        if "=" not in i:
            raise ValueError("ERROR: Garbage values in config.txt,"
                             " it must contain KEY = VALUE !!")
        aa, bb = i.split("=")
        a = aa.strip()
        b = bb.strip()
        if a.upper() == "WIDTH":
            try:
                n = int(b)
                if n <= 0:
                    raise ValueError("ERROR: HEIGHT must be a "
                                     "positive integer !!")
                Cols = n
            except ValueError:
                raise ValueError("ERROR: HEIGHT must be a positive integer !!")
        elif a.upper() == "HEIGHT":
            try:
                n = int(b)
                if n <= 0:
                    raise ValueError("ERROR: WIDTH must be a positive"
                                     " integer !!")
                Rows = n
            except ValueError:
                raise ValueError("ERROR: WIDTH must be a positive integer !!")
        elif a.upper() == "ENTRY":
            if "," not in b:
                raise ValueError("ERROR: The point must seperated by (,)")
            c, d = b.split(",")
            try:
                x, y = (int(c), int(d))
            except ValueError:
                raise ValueError("ERROR: Entry point must be a tuple of "
                                 "positive intgets , (int, int) !!")
            if Cols is None or Rows is None:
                raise ValueError("ERROR: You must enter the WIDTH and HEIGHT "
                                 "before the Entry point !!")
            if x <= 0 or y <= 0:
                raise ValueError("ERROR: Entry point must be a tuple of "
                                 "positive intgets , (int > 0, int > 0) !!")
            if x > Rows or y > Cols:
                raise ValueError("ERROR: Entry point must be a tuple of "
                                 "positive intgets , (int < rows, int < cols)"
                                 " !!")
            if Exit is not None and Exit[0] == x and Exit[1] == y:
                raise ValueError("Error: Entry point and Exsit point cann't"
                                 " be the same")
            Entry = (x, y)

        elif a.upper() == "EXIT":
            if "," not in b:
                raise ValueError("ERROR: The point must seperated by (,)")
            c, d = b.split(",")
            try:
                x, y = (int(c), int(d))
            except ValueError:
                raise ValueError("ERROR: EXIT point must be a tuple of "
                                 "intgets , (int, int) !!")
            if Cols is None or Rows is None:
                raise ValueError("ERROR: You must enter the WIDTH and HEIGHT "
                                 "before the EXIT point !!")
            if x <= 0 or y <= 0:
                raise ValueError("ERROR: Exit point must be a tuple of "
                                 "positive intgets , (int > 0, int > 0) !!")
            if x > Rows or y > Cols:
                raise ValueError("ERROR: Exit point must be a tuple of "
                                 "positive intgets , (int < rows, int < cols)"
                                 " !!")
            if Entry is not None and Entry[0] == x and Entry[1] == y:
                raise ValueError("ERROR: Entry point and Exsit"
                                 " point cann't be the same")
            Exit = (x, y)

        elif a.upper() == "OUTPUT_FILE":
            Output_file = b
        elif a.upper() == "PERFECT":
            if b.upper() == "TRUE":
                Perfect = True
            elif b.upper() == "FALSE":
                Perfect = False
            else:
                raise ValueError("ERROR: Perfect must be True or "
                                 f"False not ({b}) !!")
        elif a.upper() == "SEED":
            try:
                Seed = int(b)
            except ValueError:
                raise ValueError("ERROR: SEED must be an integer !!")
        else:
            raise ValueError(f"Error: This key({a}) and value({b})"
                             " are not supported")
    if not Cols:
        raise ValueError("ERROR: HEIGHT is mandatory !!")
    elif not Rows:
        raise ValueError("ERROR: WIDTH is mandatory !!")
    elif not Entry:
        raise ValueError("ERROR: ENTRY is mandatory !!")
    elif not Exit:
        raise ValueError("ERROR: EXIT is mandatory !!")
    elif not Output_file:
        raise ValueError("ERROR: OUTPUT_FILE is mandatory !!")
    elif Perfect is None:
        raise ValueError("ERROR: PERFECT is mandatory !!")
    return True


__all__ = ["cell", "get_confing"]
