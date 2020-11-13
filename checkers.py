class Board(object):
    
    def __init__(self): 
        self.matrix = [['x',' ','x',' ','x',' ','x',' '],
            [' ','x',' ','x',' ','x',' ','x'],
            ['x',' ','x',' ','x',' ','x',' '],
            [' ','x',' ','x',' ','x',' ','x'],
            ['x',' ','x',' ','x',' ','x',' '],
            [' ','x',' ','x',' ','x',' ','x'],
            ['x',' ','x',' ','x',' ','x',' '],
            [' ','x',' ','x',' ','x',' ','x']]


    def update_board(self):
        pass

class CharacterToken(object):
    def __init__(self,name,simbol):
        self.name = name
        self.simbol = simbol

class Token(CharacterToken):
    def __init__(self,name,simbol,value,Queen = False):
        CharacterToken.__init__(self,name,simbol)
        self.value = value
        if Queen == True:
            self.value = 2

    def positioninboard(self):  
        pass      

class Player(object):
    def __init__(self,name,points,cantToken):
        self.name = name
        self.points = points
        self.cantToken = cantToken




token1 = Token("white","0",1,Queen = False)
token2 = Token("Black","O",1,Queen = False)
player1 = Player('jugador1',0,12)
board = Board()
print(board.matrix)
print(player1.points)