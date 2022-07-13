from .formulations.standard_form import new_grid, move_grid, won


# Class that implements the puzzle logic
class LogicGame:
    def __init__(self, n):
        self.__grid = new_grid(n)

    def __str__(self):
        return '\n\n'.join(['  '.join(map(str, grid))
                            for grid in self.grid])

    def __getitem__(self, args):  # apply the arguments to the grid
        return self.grid[args]

    def move(self, movement):  # move one of the puzzle pieces
        self.__grid = move_grid(self.grid, movement)

    @property
    def won(self):
        return won(self.grid)

    @property
    def n(self):
        return self.grid.shape[0]

    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, grid):
        self.__grid = grid


# Testing the game
if __name__ == "__main__":
    import sys  # get the list of arguments passed to the Python script

    N = int(sys.argv[1])

    puzzle = LogicGame(N)

    print(puzzle)
    while not puzzle.won:
        inp = input('Insert a move [l,r,u,d]: ')
        puzzle.move(inp)

        print(puzzle)

    print("You won!")
