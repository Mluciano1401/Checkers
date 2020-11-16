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
    numplayer = 0
    def __init__(self,name,points,canttokens,colortoken):
        self.name = name
        self.points = points
        self.canttokens = canttokens
        self.colortoken = colortoken
        Player.numplayer += 1
 

class Token(object):
    
    numtokens = 0
    def __init__(self,name,simbol,value,Queen):
        self.name = name
        self.simbol = simbol
        self.value = value
        self.Queen = Queen
        if Queen == True:
            self.value = 2
            self.simbol = 'Q' 
        Token.numtokens +=  1

           
def Token_Initialposition(player,matrix):
    token = []
    if player.colortoken == "Black":
        for i in range(0,player.canttokens):
                token.append(Token("Black","O",1,False))
                for e in token:
                    for x in range(0,8):
                        for y in range(0,3):
                            if ' ' == matrix[y][x]:
                                matrix[y][x] = e.simbol

    if player.colortoken == "White":
        for i in range(0,player.canttokens):
            token.append(Token("White","0",1,False))
            for e in token:
                for x in range(0,8):
                    for y in range(5,8): 
                        if ' ' == matrix[y][x]:
                            matrix[y][x] = e.simbol
    return matrix

class movement(object):
    pass
  
board = Board()   
player1 = Player('Player1',0,12,"Black")
player2 = Player('Player2',0,12,"White")
boardinitial = Token_Initialposition(player1,board.matrix)
boardinitial = Token_Initialposition(player2,board.matrix)
for e in boardinitial:
    print(e)   
print(player1.__dict__)
print(player2.__dict__)
print('total tokens on the board -->',Token.numtokens)
print(Player.numplayer)
