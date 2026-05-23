class cell:
    def __init__(self, E, W, N, S, Point: tuple):
        self.East = E
        self.West = W
        self.North = N
        self.South = S
        self.Point = Point
        self.has_mid = False

Rows = None
Cols = None
Entry = None
Exit = None
Output_file = None
Perfect = None
Seed = None

def get_confing():
    import sys
    argv = sys.argv
    if len(argv) > 2:
        raise FileNotFoundError("ERROR: a_maze_ing.py and config.txt are must just exist, but you enter more !!")
    elif len(argv) < 2:
        raise FileNotFoundError("Error: a_maze_ing.py and config.txt are must exist, but you didn't enter config.txt !!")
    file = open(argv[1], "r")
    global Rows, Cols, Entry, Exit, Output_file, Perfect, Seed
    content = file.read().strip().split("\n")
    for i in content:
        if "=" not in i:
            raise ValueError("ERROR: Garbage values in config.txt, it must contain KEY = VALUE !!")
        aa, bb = i.split("=")
        a = aa.strip()
        b = bb.strip()
        if a.upper() == "HEIGHT":
            try:
                Cols = int(b)
            except ValueError:
                raise ValueError("ERROR: HEIGHT must be an integer !!")
        elif a.upper() == "WIDTH":
            try:
                Rows = int(b)
            except ValueError:
                raise ValueError("ERROR: WIDTH must be an integer !!")
        elif a.upper() == "ENTRY":
            c, d = b.split(",")
            try:
                Entry = (int(c), int(d))
            except ValueError:
                raise ValueError("ERROR: Entry point must be a tuple of intgets , (int, int) !!")
        elif a.upper() == "EXIT":
            c, d = b.split(",")
            try:
                Exit = (int(c), int(d))
            except ValueError:
                raise ValueError("ERROR: EXIT point must be a tuple of intgets , (int, int) !!")
        elif a.upper() == "OUTPUT_FILE":
            Output_file = b
        elif a.upper() == "PERFECT":
            Perfect = True if b.upper() == "TRUE" else False
        elif a.upper() == "SEED":
            try:
                Seed = int(b)
            except ValueError:
                raise ValueError("ERROR: SEED must be an integer !!")
        else:
            raise ValueError(f"Error: This key({a}) and value({b}) are not supported")
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
    elif Perfect == None:
        raise ValueError("ERROR: PERFECT is mandatory !!")
    return True

__all__ = ["cell", "get_confing"]
