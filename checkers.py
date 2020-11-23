from Movement import *
class Board(object):
    
    def __init__(self,matrix): 
        self.matrix = [['x','1','2','3','4','5','6','7','8','x'],
            ['1','x',' ','x',' ','x',' ','x',' ','1'],
            ['2',' ','x',' ','x',' ','x',' ','x','2'],
            ['3','x',' ','x',' ','x',' ','x',' ','3'],
            ['4',' ','x',' ','x',' ','x',' ','x','4'],
            ['5','x',' ','x',' ','x',' ','x',' ','5'],
            ['6',' ','x',' ','x',' ','x',' ','x','6'],
            ['7','x',' ','x',' ','x',' ','x',' ','7'],
            ['8',' ','x',' ','x',' ','x',' ','x','8'],
            ['x','1','2','3','4','5','6','7','8','x']]

            
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

    def opponent(self,opponent):
        self.opponent = opponent 
        return self.opponent.colortoken[0]  
        
   
 
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
                        for x in range(1,9):
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
                    for x in range(1,9):
                        for y in range(6,10): 
                            if ' ' == matrix[y][x]:
                                e.position(y,x)
                                matrix[y][x] = e.tokensimbol()
                                player.positiontokens.append([y,x])
        

                                          
                                
        return [matrix,token]

    @staticmethod
    def winner(player):
        if player.points >= 12:
            return True
        else:
            return False 
    @staticmethod          
    def Queentoken(player,token):
        for e in token:
            if  player.colortoken == "White" and [1,range(0,8)] in player.positiontokens:
                e.Queen = True     
                     
            if  player.colortoken == "Black" and [8,range(0,8)] in player.positiontokens:
                e.Queen = True
      
def rotatingshifts(players,boardinitial,tokens):
    msg = ' '   
    finish = False   
    while finish == False: 
        for player in players:
            if Gameplayfeatures.winner(player):
                msg = "Congratulations you are the winner -> ",player.name
                finish = True 
                break
            else:
                if player.availabletokens == None:
                    msg = "Locked",player.name
                    finish = True 
                    break
                else:
                    print('\n')
                    print('Turn of ->', player.name,'Color:',player.colortoken,'Points: ', player.points,'Tokens on board: ', player.canttokens)
                    for e in boardinitial:
                        print(e)   
                    print('total tokens on the board -->',Token.numtokens)
                    target = [' ']
                    kill = Movement.killtoken(player,boardinitial)
                    if kill == True:
                         spaceblank = Movement(player,boardinitial,target)
                    else:
                        queen = Gameplayfeatures.Queentoken(player,tokens)                    
                        spaceblank = Movement(player,boardinitial,target)
                        move =  Movement.move_token(player,boardinitial)
                            

    print(msg)

board =  Board([])
player1 = Player(0,12,"White",[],{})
player2 = Player(0,12,"Black",[],{})
player1.opponent(player2)
player2.opponent(player1)
boardinitial = Gameplayfeatures(player1,board.matrix)
boardinitial = Gameplayfeatures(player2,board.matrix)   
players = [player1,player2]
rotatingshifts(players,boardinitial[0],boardinitial[1])