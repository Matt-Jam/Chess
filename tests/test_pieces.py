from chess.pieces.pawn import Pawn
from chess.util.coordinate import Coordinate


def test_pawn_str():
    
    p1 = Pawn(True, Coordinate((1,2)))
    assert str(p1) == "♙"

    p2 = Pawn(False, Coordinate((2,3)))
    assert str(p2) == "♟"

    