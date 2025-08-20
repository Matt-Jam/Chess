from  .piece import Piece
from ..util.coordinate import Coordinate


class Queen(Piece):

    def __init__(self, suit: bool, coord: Coordinate):
        super().__init__(9, suit, coord)

    def __str__(self):
        if self.suit:
            return "♕"
        return "♛"
    

