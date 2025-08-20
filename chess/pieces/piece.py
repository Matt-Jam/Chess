from ..util.coordinate import Coordinate

class Piece:

    def __init__(self, icon: str, value: int, team: bool, coord: Coordinate):
        self.icon = icon
        self.value = value
        self.team = team
        self.coord = coord


        
