class Board(object):
    
    def __init__(self,matrix): 
        self.matrix = [['0','1','2','3','4','5','6','7','x'],
            ['x',' ','x',' ','x',' ','x',' ','1'],
            [' ','x',' ','x',' ','x',' ','x','2'],
            ['x',' ','x',' ','x',' ','x',' ','3'],
            [' ','x',' ','x',' ','x',' ','x','4'],
            ['x',' ','x',' ','x',' ','x',' ','5'],
            [' ','x',' ','x',' ','x',' ','x','6'],
            ['x',' ','x',' ','x',' ','x',' ','7'],
            [' ','x',' ','x',' ','x',' ','x','8']]

            
class Player(object):
    numplayer = 0
    def __init__(self,points,canttokens,colortoken,positiontokens,availabletokens):
        self.points = points
        self.canttokens = canttokens
        self.colortoken = colortoken
        self.positiontokens = positiontokens
        self.availabletokens = availabletokens
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

    def tokensimbol(self):
        return self.simbol
        
    def position(self,y,x):
        self.y = y
        self.x = x
        return [y,x]


class Gameplayfeatures(object):
    def __new__(self,player,matrix):
        self.player = player
        self.matrix = matrix
        token = []
        if player.colortoken == "Black":
            for i in range(0,player.canttokens):
                    nametoken = "Black" + str(i)
                    token.append(Token(nametoken,player.colortoken[0],1,False))
                    for e in token:
                        for x in range(0,8):
                            for y in range(1,4):
                                if ' ' == matrix[y][x]:
                                    e.position(y,x)
                                    matrix[y][x] = e.tokensimbol()
                                    player.positiontokens.append([y,x])
                                    

        if player.colortoken == "White":
            for i in range(0,player.canttokens):
                nametoken = "White" + str(i)
                token.append(Token(nametoken,player.colortoken[0],1,False))
                for e in token:
                    for x in range(0,8):
                        for y in range(6,9): 
                            if ' ' == matrix[y][x]:
                                e.position(y,x)
                                matrix[y][x] = e.tokensimbol()
                                player.positiontokens.append([y,x])
                                
        return matrix

    @staticmethod
    def winner(point):
        if point >= 4:
            return True
        else:
            return False 
                  
def Killtoken(player,matrix):
        if player.colortoken == "Black":
            for x in range(0,7):
                for y in range(1,8):
                    if matrix[y][x] != player.colortoken[0] and matrix[y][x] != ' ':
                        if matrix[y + 1][x + 1] == ' ':
                            c = [y + 1, x + 1] 
                            s = str([y,x])
                            player.positiontokens.append([y,x])
                            player.availabletokens[s] =  c  
        if player.colortoken == "White":       
            for x in range(0,7):
                for y in range(1,8):
                    if matrix[y][x] != player.colortoken[0] and matrix[y][x] != ' ':
                        if matrix[y + 1][x + 1] == ' ':
                            c = [y + 1, x + 1] 
                            s = str([y,x])
                            player.positiontokens.append([y,x])
                            player.availabletokens[s] =  c  
        


class Movement(object):
    def __new__(self,player,matrix,target):
        self.player = player
        self.matrix = matrix
        self.target = target
        for e in player.positiontokens:
            newpositiontokens = []
            y= e[0]
            x= e[1]
            if x < 8 and y < 8 and x > 0 and y > 0:
                if player.colortoken == "Black":
                    if matrix[y + 1][x + 1] in target:
                        a = [y,x]
                        z = str(a)
                        newpositiontokens.append([y + 1,x + 1])
                        player.availabletokens[z] = newpositiontokens
                    if matrix[y + 1][x - 1] in target:
                        newpositiontokens.append([y + 1, x - 1])
                        player.availabletokens[z] =  newpositiontokens   
                if player.colortoken == "White":
                    if matrix[y - 1][x + 1] in target:
                        b = [y,x]
                        v = str(b)
                        newpositiontokens.append([y - 1, x + 1])
                        player.availabletokens[v] = newpositiontokens
                    if matrix[y - 1][x - 1] in target:
                        newpositiontokens.append([y - 1, x - 1]) 
                        player.availabletokens[v] =  newpositiontokens  
        if player.availabletokens == {}:
            player.availabletokens = None           
        

    @staticmethod
   
    def move_token(player,matrix):
        try:
            Killtoken(player,matrix)
            a = []
            for e in player.availabletokens:
                a.append(e)
            print('Free Token ->', a)    
            movetoken = input('Write the coordinates of the token you want to move: (example -> 0,1) ')
            i,j = movetoken
            c = [i,j]
            z = str(c)
            if z in player.availabletokens:
                print('Possible movements to perform -->', player.availabletokens[z])
                coordinates = input('Write the coordinates where you want to move the token: (example -> 0,1) ')
                y,x = coordinates
                r = [y,x]
                matrix[i][j] = ' '
                if r in  player.availabletokens[z]:
                    if player.colortoken == "Black":
                        matrix[y][x] = player.colortoken[0]
                        player.positiontokens.append([y,x])
                    if player.colortoken == "White":
                        matrix[y][x] = player.colortoken[0]
                        player.positiontokens.append([y,x])
                else:
                    print('This position is not free  -1')    
                    player.points -= 1   
            else:
                print('This token is not free   -1') 
                player.points -= 1
            if  matrix[i][j] == ' ' and c in player.positiontokens:
                player.positiontokens.remove(c)    
        except:
            print('Your coordinates could not be read well ')   
         
        return matrix              


    
    
def rotatingshifts(players,boardinitial):
    msg = ' '   
    finish = False   
    while finish == False: 
        for player in players:
            if Gameplayfeatures.winner(player.points):
                msg = "Winner -> ",player.name
                finish = True 
                break
            else:
                if player.availabletokens == None:
                    msg = "Locked",player.name
                    finish = True 
                    break
                else:
                    print('turn of ->', player.name,'Points: ', player.points,'Tokens on board: ', player.canttokens)
                    for e in boardinitial:
                        print(e)   
                    print('total tokens on the board -->',Token.numtokens)
                    target = [' ']
                    spaceblank = Movement(player,boardinitial,target)
                    move =  Movement.move_token(player,boardinitial)
                    player.points += 1  
                    spaceblank = Movement(player,move,target)          

    print(msg)

board =  Board([]) 
player1 = Player(0,12,"Black",[],{})
player2 = Player(0,12,"White",[],{})
boardinitial = Gameplayfeatures(player1,board.matrix)
boardinitial = Gameplayfeatures(player2,board.matrix)    
players = [player1,player2]
#killtoken(boardinitial)
rotatingshifts(players,boardinitial)