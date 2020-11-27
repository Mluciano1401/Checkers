from Queen import *
from Movement import *
from Player import *
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

class Gameplayfeatures(object):
    def __new__(self,player,matrix):
        self.player = player
        self.matrix = matrix
        if player.colortoken == "Black":
            for x in range(1,9):
                for y in range(1,4):
                    if ' ' == matrix[y][x]:
                        matrix[y][x] = player.colortoken[0]
                        player.positiontokens.append([y,x])               

        if player.colortoken == "White":
           for x in range(1,9):
                for y in range(6,10): 
                    if ' ' == matrix[y][x]:
                        matrix[y][x] = player.colortoken[0]
                        player.positiontokens.append([y,x])
                               
        return matrix

    @staticmethod
    def winner(player):
        if player.points >= 12 or player.opponent.canttokens == 0:
            return True
        else:
            return False 
        
      
def rotatingshifts(players,boardinitial):
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
                    print('\n')
                    for rows in boardinitial:
                        print(rows)  
                    print('\n')     
                    target = [' ']
                    kill = Movement.killtoken(player,boardinitial)
                    if kill == True:
                         spaceblank = Movement(player,boardinitial,target)
                    else:
                        queen = MovementQueen(player,boardinitial,target)           
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
rotatingshifts(players,boardinitial)
