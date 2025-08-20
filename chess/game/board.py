from ..pieces.piece import Piece

class Board:

    def __init__(self):
        self.grid: list[list[Piece | None]] = [[None for _ in range(8)] for _ in range(8)]
    
    def __str__(self):
        s = ""
        for row in self.grid:
            for piece in row:
                s += str(piece) if piece else " "
            s+="\n"
        return s
