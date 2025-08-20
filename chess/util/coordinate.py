class Coordinate:

    def __init__(self, coord: tuple[int, int]):
        self.coord = coord 

    def __str__(self):
        return f'{chr(self.col+ord("A"))}{8-self.row}'
    
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
    
    

