from  .piece import Piece
from ..util.coordinate import Coordinate


class Rook(Piece):

    def __init__(self, suit: bool, coord: Coordinate):
        super().__init__(5, suit, coord)

    def __str__(self):
        if self.suit:
            return "♖"
        return "♜"
    

