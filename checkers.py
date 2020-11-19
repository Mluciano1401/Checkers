class Board(object):
    
    def __init__(self,matrix): 
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
       
    def availabletokens(self,listposition):   
        for e in positiontokens:
            listposition.append(positiontokens[e])

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

def deletetoken(player,matrix):
        x = space_blank(player,matrix,) 

 

class Gameplayfeatures(Token):
    def __init__(self,matrix):
      super(Gameplayfeatures, self).__init__(*args, **kwargs)

    @staticmethod        
    def Token_Initialposition(player,matrix):
        token = []
        if player.colortoken == "Black":
            for i in range(0,player.canttokens):
                    token.append(Token("Black","B",1,False))
                    for e in token:
                        for x in range(0,8):
                            for y in range(0,3):
                                if ' ' == matrix[y][x]:
                                    matrix[y][x] = e.simbol
                                    player.positiontokens.append([y,x])

        if player.colortoken == "White":
            for i in range(0,player.canttokens):
                token.append(Token("White","W",1,False))
                for e in token:
                    for x in range(0,8):
                        for y in range(5,8): 
                            if ' ' == matrix[y][x]:
                                matrix[y][x] = e.simbol
                                player.positiontokens.append([y,x])
        return matrix
    @staticmethod 
    def space_blank(player,matrix,target):
        
        availabletoken = {}
        for e in player.positiontokens:
            newpositiontokens = []
            y= e[0]
            x= e[1]
            if x < 7 and y < 7 and x > 0 and y > 0:
                if player.colortoken == "Black":
                    if matrix[y + 1][x + 1] == target:
                        z = [y,x]
                        z = str(z)
                        newpositiontokens.append([y + 1,x + 1])
                        availabletoken[z] = newpositiontokens
                    if matrix[y + 1][x - 1] == target:
                        newpositiontokens.append([y + 1, x - 1])
                        availabletoken[z] =  newpositiontokens   
                if player.colortoken == "White":
                    if matrix[y - 1][x + 1] == target:
                        v = [y,x]
                        v = str(v)
                        newpositiontokens.append([y - 1, x + 1])
                        availabletoken[v] = newpositiontokens
                    if matrix[y - 1][x - 1] == target:
                        newpositiontokens.append([y - 1, x - 1]) 
                        availabletoken[v] =  newpositiontokens  
        if availabletoken == {}:
            availabletoken = None           
        player.positiontokens = availabletoken  

    @staticmethod 
    def movetoken(player,matrix):
        try:
            movetoken = input('Write the coordinates of the token you want to move: (example -> 0,1) ')
            i,j = movetoken
            c = [i,j]
            z = str(c)
            if z in player.positiontokens:
                matrix[i][j] = ' '
                print('Possible movements to perform -->', player.positiontokens[z])
                coordinates = input('Write the coordinates where you want to move the token: (example -> 0,1) ')
                y,x = coordinates
                r = [y,x]
                if r in  player.positiontokens[z]:
                    if player.colortoken == "Black":
                        matrix[y][x] = 'B'
                    if player.colortoken == "White":
                        matrix[y][x] = 'W'
                else:
                    print('esta posicion no esta libre   -1')    
                    player.points -= 1
            else:
                print('esta ficha no esta libre    -1') 
                player.points -= 1
        except:
            print('no se pudo leer sus coordenadas')
        return matrix                 
   
    @staticmethod 
    def winner(point):
        if point >= 2:
            return True
        else:
            return False 
    

    
    
def rotatingshifts(players,boardinitial):
    msg = ' '   
    finish = False   
    while True: 
        if finish == True:
            break
        else:
            for player in players:
                if Gameplayfeatures.winner(player.points):
                    msg = "Winner -> ",player.name
                    finish = True 
                    break
                else:
                    if player.positiontokens == None:
                        msg = "Locked",player.name
                        finish = True 
                        break
                    else:
                        print('turn of ->', player.name)
                        for e in boardinitial:
                            print(e)   
                        print('total tokens on the board -->',Token.numtokens)
                
                        spaceblank = Gameplayfeatures.space_blank(player,boardinitial, ' ')
                        print(player.__dict__)
                        move =  Gameplayfeatures.movetoken(player,boardinitial)
                        player.points += 1 
                        boardinitial = move
                   

    print(msg)
board =  Board([]) 
player1 = Player(0,12,"Black",[])
player2 = Player(0,12,"White",[])
boardinitial = Gameplayfeatures.Token_Initialposition(player1,board.matrix)
boardinitial = Gameplayfeatures.Token_Initialposition(player2,board.matrix)    
players = [player1,player2]
rotatingshifts(players,boardinitial)
