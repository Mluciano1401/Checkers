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


class Token(object):
    def __init__(self,name,simbol,value,Queen = False):
        self.name = name
        self.simbol = simbol
        self.value = value
        if Queen == True:
            self.value = 2


class Player(object):
    def __init__(self,name,points,canttokens):
        self.name = name
        self.points = points
        self.canttokens = canttokens

        
        
    



board = Board()
print(board.matrix)
token1 = Token("white","0",1,Queen = False)
token2 = Token("Black","O",1,Queen = False)

player1 = Player('Jugador1',0,12)
player2 = Player('Jugador2',0,12)
print(player1.__dict__)
print(token1.__dict__)
