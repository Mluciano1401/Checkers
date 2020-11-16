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
    def __init__(self,name,points,canttokens,colortoken):
        self.name = name
        self.points = points
        self.canttokens = canttokens
        self.colortoken = colortoken
    
 

class Token(object):
    def __init__(self,name,simbol,value,Queen,x,y):
        self.name = name
        self.simbol = simbol
        self.value = value
        self.Queen = Queen
        if Queen == True:
            self.value = 2
            self.simbol = 'Q'
        self.x = x 
        self.y = y    

    def token(self):
        return self.simbol        

           
def Token_Initialposition(token,matrix):
    
    if token.name == "Black":
        for x in range(0,8):
            for y in range(0,3):
                if ' ' == matrix[y][x]:
                    matrix[y][x] = token.token()
    if token.name == "White":
        for x in range(0,8):
            for y in range(5,8): 
                if ' ' == matrix[y][x]:
                    matrix[y][x] = token.token()

    return matrix

board = Board()
token1 = Token("White","0",1,False,0,0)
token2 = Token("Black","O",1,False,0,0)
    
player1 = Player('Player1',0,12,"Black")
player2 = Player('Player2',0,12,"White")
boardinitial = Token_Initialposition(token1,board.matrix)
boardinitial = Token_Initialposition(token2,board.matrix)
for e in boardinitial:
    print(e) 
print(player1.__dict__)
print(player2.__dict__)

