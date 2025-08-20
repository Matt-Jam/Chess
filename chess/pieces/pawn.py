from  .piece import Piece
from ..util.coordinate import Coordinate


class Pawn(Piece):

    def __init__(self, suit: bool, coord: Coordinate):
        super().__init__(1, suit, coord)
        self.moved = False

    def __str__(self):
        if self.suit:
            return "♙"
        return "♟"
    

