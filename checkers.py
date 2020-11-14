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

class Player(object):
    def __init__(self,name,points,canttokens):
        self.name = name
        self.points = points
        self.canttokens = canttokens
    
 

class Token(object):
    def __init__(self,name,simbol,value,Queen):
        self.name = name
        self.simbol = simbol
        self.value = value
        self.Queen = Queen
        if Queen == True:
            self.value = 2
            self.simbol = 'Q'

           
class Token_Initialposition(Token):
    
    token1 = Token("white","0",1,False)
    token2 = Token("Black","O",1,False)
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

class Movement(Token_Initialposition):
   pass

board = Board()
player1 = Player('Player1',0,12)
player2 = Player('Player2',0,12)
boardinitial = Token_Initialposition("Black","O",1, False,board.matrix)
boardinitial = Token_Initialposition("White","0",1, False,board.matrix)
for e in boardinitial.matrix:
    print(e) 
print(player1.__dict__)
print(player2.__dict__)


