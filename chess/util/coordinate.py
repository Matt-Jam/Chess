class Coordinate:

    def __init__(self, coord: tuple[int, int]):
        self.coord = coord 
        self.onBoardCheck()

    def __str__(self):
        return f'{chr(self.col+ord("A"))}{8-self.row}'
    
    def onBoardCheck(self):
        if self.row < 0 or self.col < 0 or self.row > 7 or self.col > 7:
            raise ValueError("Coordinate is off the b")

    @property
    def row(self):
        return self.coord[0]
    
    @property
    def col(self):
        return self.coord[1]
    
    @staticmethod
    def fromStr(s:str):
        r = 8-int(s[1])
        c = ord(s[0])-ord("A")
        return Coordinate((r,c))
    
    

