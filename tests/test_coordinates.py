import pytest
from chess.util.coordinate import Coordinate


def test_construction():
    c = Coordinate((1,2))
    assert c.coord == (1,2)


def test_rc():
    c = Coordinate((1,2))
    assert c.row == 1
    assert c.col == 2

def test_fromStr():
    c = Coordinate.fromStr("C2")
    assert c.coord == (6,2)

def test_onBoard():
    with pytest.raises(ValueError):
        Coordinate((8,-1))

