from perfect_maze import create_maze as perfect_maze
from non_perfect_maze import create_maze as imperfect_maze
from properties import cell
from print_maze import print_grid
from print_maze import make_output



class MazeGenerator:
    def __init__(self) -> None:
        self.rows = None
        self.cols = None
        self.start_point = None
        self.end_point = None
        self.perfect = None
        self.seed = None
        self.TheMaze = None
        self.TheMazeAnswer = None

    def Creatre_Maze(self, Rows: int, Cols: int, Start: tuple[int, int],
                 End: tuple[int, int], Seed: int,
                 Perfect: bool):
        self.rows = Rows
        self.cols = Cols
        self.start_point = Start
        self.end_point = End
        self.perfect = Perfect
        self.seed = Seed

        if self.perfect:
            self.TheMaze, self.TheMazeAnswer = perfect_maze(self.rows, self.cols,
                                                            self.start_point, self.end_point,
                                                            self.seed)
        else:
            self.TheMaze, self.TheMazeAnswer = imperfect_maze(self.rows, self.cols,
                                                            self.start_point, self.end_point,
                                                            self.seed)
        
        #return self.TheMaze, self.TheMazeAnswer
    

    def print_the_maze(self, MazeColor: str, PathColor: str):
        print_grid(self.TheMaze, self.rows, self.cols, MazeColor, PathColor)


    def make_output(self, out_file: str) -> None:
        with open(out_file, "w") as file:
            for i in range(self.rows):
                for j in range(self.cols):
                    idx = i * self.cols + j
                    file.write(self.TheMaze[idx].change_to_Hex())
                file.write("\n")
            file.write("\n")

            file.write(f"{self.start_point[0]}, {self.start_point[1]}\n")
            file.write(f"{self.end_point[0]}, {self.end_point[1]}\n")
            for ii in self.TheMazeAnswer:
                file.write(ii)
            file.write("\n")

