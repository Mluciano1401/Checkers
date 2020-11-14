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
    def __init__(self,name,simbol,value,Queen):
        self.name = name
        self.simbol = simbol
        self.value = value
        self.Queen = Queen
        if Queen == True:
            self.value = 2
           
class Token_Initialposition(Token):
    def __init__(self,name,simbol,value,Queen,matrix):
        Token.__init__(self,name,simbol,value,Queen = False)
        self.matrix = matrix
        if self.name == "Black":
            for x in range(0,8):
                for y in range(0,3):
                    if ' ' == matrix[y][x]:
                        matrix[y][x] = self.simbol 
        if self.name == "White":
            for x in range(0,8):
                for y in range(5,8): 
                    if ' ' == matrix[y][x]:
                        matrix[y][x] = self.simbol
                        

          
class Player(object):
    def __init__(self,name,points,canttokens):
        self.name = name
        self.points = points
        self.canttokens = canttokens
        



board = Board()
token1 = Token("white","0",1,False)
token2 = Token("Black","O",1,False)
player1 = Player('Jugador1',0,12)
player2 = Player('Jugador2',0,12)
boardinitial = Token_Initialposition("Black","O",1, False,board.matrix)
boardinitial1 = Token_Initialposition("White","0",1, False,board.matrix)
print(boardinitial1.matrix)
print(player1.__dict__)
print(token1.__dict__)

