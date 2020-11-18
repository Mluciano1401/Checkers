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
    def __init__(self,points,canttokens,colortoken,positiontokens):
        self.points = points
        self.canttokens = canttokens
        self.colortoken = colortoken
        self.positiontokens = positiontokens
        Player.numplayer += 1
        self.name = 'Player' + str(Player.numplayer)

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

   

class Gameplayfeatures(object):
    def __init__(self,xposition,yposition):
        self.xposition = xposition
        self.yposition = yposition

    @staticmethod              
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
                                    player.positiontokens.append([y,x])

        if player.colortoken == "White":
            for i in range(0,player.canttokens):
                token.append(Token("White","0",1,False))
                for e in token:
                    for x in range(0,8):
                        for y in range(5,8): 
                            if ' ' == matrix[y][x]:
                                matrix[y][x] = e.simbol
                                player.positiontokens.append([y,x])
        return matrix

    @staticmethod 
    def space_blank(player,matrix):
        newpositiontokens = []
        availabletoken = {}
        for e in player.positiontokens:
            y= e[0]
            x= e[1]
            if x < 7 and y < 7 and x > 0 and y > 0:
                if player.colortoken == "Black":
                    if matrix[y + 1][x + 1] == ' ':
                        z = [y,x]
                        z = str(z)
                        newpositiontokens.append([y + 1,x + 1])
                        availabletoken[z] = newpositiontokens
                    if matrix[y + 1][x - 1] == ' ':
                        newpositiontokens.append([y + 1, x - 1])
                        availabletoken[z] =  newpositiontokens   
                if player.colortoken == "White":
                    if matrix[y - 1][x + 1] == ' ':
                        v = [y,x]
                        v = str(v)
                        newpositiontokens.append([y - 1, x + 1])
                        availabletoken[v] = newpositiontokens
                    if matrix[y - 1][x - 1] == ' ':
                        newpositiontokens.append([y - 1, x - 1]) 
                        availabletoken[v] =  newpositiontokens        
        player.positiontokens = availabletoken    
    @staticmethod                 
    def movetoken(player,matrix):
        coordinates = input('insert the coordinates: (example -> 0,1) ')
        y,x = coordinates
        if player.colortoken == "Black":
            matrix[y][x] = 'O'
        if player.colortoken == "White":
            matrix[y][x] = '0'    
        print(matrix)
    
    def winner(self,point):
        if self.point >= 12:
            return True
        else:
            return False 
    

    def deletetoken():
        pass  
   
    
def rotatingshifts():      
    board = Board()   
    player1 = Player(0,12,"Black",[])
    player2 = Player(0,12,"White",[])
    boardinitial = Gameplayfeatures.Token_Initialposition(player1,board.matrix)
    boardinitial = Gameplayfeatures.Token_Initialposition(player2,board.matrix)

    for e in boardinitial:
        print(e)   
    print('total tokens on the board -->',Token.numtokens)
    print(player1.__dict__)
    print(player2.__dict__)
    spaceblank = Gameplayfeatures.space_blank(player1,boardinitial)
    spaceblank = Gameplayfeatures.space_blank(player2,boardinitial)
    print(player1.__dict__)
    print(player2.__dict__)
    move =  Gameplayfeatures.movetoken(player1,boardinitial)
    return

rotatingshifts()






  

