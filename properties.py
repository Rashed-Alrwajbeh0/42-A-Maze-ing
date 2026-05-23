class cell:
    def __init__(self, E, W, N, S, Point: tuple):
        self.East = E
        self.West = W
        self.North = N
        self.South = S
        self.Point = Point
        self.has_mid = False

rows = 100
cols = 100

__all__ = ["rows", "cols", "cell"]
