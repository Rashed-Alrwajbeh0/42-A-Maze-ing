from perfect_maze import create_maze as perfect_maze
from non_perfect_maze import create_maze as imperfect_maze
from print_maze import print_grid
from properties import cell


class MazeGenerator:
    def __init__(self) -> None:
        self.rows: int | None = None
        self.cols: int | None = None
        self.start_point: tuple[int, int] | None = None
        self.end_point: tuple[int, int] | None = None
        self.perfect: bool | None = None
        self.seed: int | None = None
        self.TheMaze: list[cell] | None = None
        self.TheMazeAnswer: list[str] | None = None

    def Creatre_Maze(self, Rows: int, Cols: int, Start: tuple[int, int],
                     End: tuple[int, int], Seed: int,
                     Perfect: bool) -> None:
        self.rows = Rows
        self.cols = Cols
        self.start_point = Start
        self.end_point = End
        self.perfect = Perfect
        self.seed = Seed

        if self.perfect:
            self.TheMaze, self.TheMazeAnswer = perfect_maze(self.rows,
                                                            self.cols,
                                                            self.start_point,
                                                            self.end_point,
                                                            self.seed)
        else:
            self.TheMaze, self.TheMazeAnswer = imperfect_maze(self.rows,
                                                              self.cols,
                                                              self.start_point,
                                                              self.end_point,
                                                              self.seed)

    def print_the_maze(self, MazeColor: str, PathColor: str) -> None:
        if (self.TheMaze is not None and
                self.rows is not None and
                self.cols is not None):
            print_grid(self.TheMaze,
                       self.rows,
                       self.cols,
                       MazeColor,
                       PathColor)

    def make_output(self, out_file: str) -> None:
        if self.rows is None or self.cols is None or self.TheMaze is None:
            return
        with open(out_file, "w") as file:
            for i in range(self.rows):
                for j in range(self.cols):
                    idx = i * self.cols + j
                    file.write(self.TheMaze[idx].change_to_Hex())
                file.write("\n")
            file.write("\n")
            if self.start_point is None or self.end_point is None:
                return
            file.write(f"{self.start_point[0]}, {self.start_point[1]}\n")
            file.write(f"{self.end_point[0]}, {self.end_point[1]}\n")
            if self.TheMazeAnswer is None:
                return
            for ii in self.TheMazeAnswer:
                file.write(ii)
            file.write("\n")
