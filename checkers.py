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
    def __init__(self,name,points,token,canttokens):
        self.name = name
        self.points =points
        self.token = token
        self.canttokens = canttokens
       
class Token(object):
    def __init__(self,simbol,value,Queen):
        self.simbol = simbol
        self.value = value
        self.Queen = Queen
        if Queen == True:
            self.value = 2
           
class Token_Initialposition(Token):
    def __init__(self,token,canttokens,matrix):
        self.matrix = matrix
        self.token = token
        self.canttokens = canttokens
        if self.token == "Black":
            for x in range(0,8):
                for y in range(0,3):
                    if ' ' == matrix[y][x]:
                         matrix[y][x] = 'O'
        if self.token == "White":
            for x in range(0,8):
                for y in range(5,8): 
                    if ' ' == matrix[y][x]:                     
                        matrix[y][x] = '0'
                        


board = Board()
player1 = Player('Player1',0,"white",12)
player2 = Player('Player2',0,"Black",12)


boardinitial = Token_Initialposition("white",12,board.matrix)
boardinitial = Token_Initialposition("Black",12,board.matrix)
for e in boardinitial.matrix:
    print(e)
print(player1.__dict__)

