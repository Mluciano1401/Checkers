class Movement(object):
    def __new__(self,player,matrix,target):
        self.player = player
        self.matrix = matrix
        self.target = target
        for e in player.positiontokens:
            newpositiontokens = []
            y= e[0]
            x= e[1]
          
            if x < 10 and y < 10 and x > 0 and y > 0:
                if player.colortoken == "Black":
                    if matrix[y + 1][x + 1] in target:
                        newpositiontokens.append([y + 1,x + 1])
                           
                        a = [y,x]
                        z = str(a)  
                        player.availabletokens[z] =  newpositiontokens  
                    if matrix[y + 1][x - 1] in target:
                        newpositiontokens.append([y + 1, x - 1])
                           
                        a = [y,x]
                        z = str(a)  
                        player.availabletokens[z] =  newpositiontokens  
                if player.colortoken == "White":
                    if matrix[y - 1][x + 1] in target:
                        newpositiontokens.append([y - 1, x + 1])
                        b = [y,x]
                        v = str(b)
                        player.availabletokens[v] = newpositiontokens   
                    if matrix[y - 1][x - 1] in target:
                        newpositiontokens.append([y - 1, x - 1]) 
                        b = [y,x]
                        v = str(b)
                        player.availabletokens[v] = newpositiontokens    
        if player.availabletokens == {}:
            player.availabletokens = None  

    @staticmethod
    def killtoken(player,matrix):
         for e in player.positiontokens:
            y= e[0]
            x= e[1]
            if player.colortoken == "Black":
                if matrix[y + 1][x + 1] == player.opponent.colortoken[0]  or matrix[y + 1][x + 1] =='QW' :
                    if matrix[y + 2][x + 2] == ' ':
                        matrix[y+ 2][x + 2] = player.colortoken[0]
                        player.positiontokens.append([y + 2,x + 2])
                        matrix[y][x] = ' '
                        matrix[y + 1][x + 1] = ' '
                        player.points += 1
                        player.opponent.canttokens -= 1
                        player.opponent.positiontokens.remove([y + 1,x + 1])
                        player.positiontokens.remove([y,x])
                        return True  

                if matrix[y + 1][x - 1] == player.opponent.colortoken[0] or matrix[y + 1][x - 1] =='QW':
                    if matrix[y + 2][x - 2] == ' ':
                        matrix[y+ 2][x - 2] = player.colortoken[0]
                        player.positiontokens.append([y + 2,x - 2])
                        matrix[y][x] = ' '
                        matrix[y + 1][x - 1] = ' '
                        player.points += 1
                        player.opponent.canttokens -= 1
                        player.opponent.positiontokens.remove([y + 1,x - 1]) 
                        player.positiontokens.remove([y,x])     
                        return True  

            if player.colortoken == "White":
                if matrix[y - 1][x + 1] == player.opponent.colortoken[0] or matrix[y - 1][x + 1] =='QB':
                    if matrix[y - 2][x + 2] == ' ':
                        matrix[y- 2][x + 2] = player.colortoken[0]
                        player.positiontokens.append([y - 2,x + 2])
                        matrix[y][x] = ' '
                        matrix[y - 1][x + 1] = ' '
                        player.points += 1
                        player.opponent.canttokens -= 1
                        player.opponent.positiontokens.remove([y - 1,x + 1])
                        player.positiontokens.remove([y,x])
                        return True  

                if matrix[y - 1][x - 1] == player.opponent.colortoken[0]  or matrix[y - 1][x - 1] == 'QB':
                    if matrix[y - 2][x - 2] == ' ':
                        matrix[y- 2][x - 2] = player.colortoken[0]
                        player.positiontokens.append([y - 2,x - 2])
                        matrix[y][x] = ' '
                        matrix[y - 1][x - 1] = ' '
                        player.points += 1
                        player.opponent.canttokens -= 1
                        player.opponent.positiontokens.remove([y - 1,x - 1])
                        player.positiontokens.remove([y,x])
                        return True      
  
    @staticmethod
    def move_token(player,matrix):
        
        try:
            a = []
            for e in player.availabletokens:
                a.append(e)
            print('Free Token ->', a)    
            movetoken = input('Write the coordinates of the token you want to move: (example -> 0,1) ')
            i,j = movetoken
            c = [i,j]
            z = str(c)  
            if c not in player.positiontokens and  matrix[i][j] == ' ':
                del player.availabletokens[z] 
                return Movement.move_token(player,matrix)  
            else:
                if z in player.availabletokens:
                    print('Possible movements to perform -->', player.availabletokens[z])
                    coordinates = input('Write the coordinates where you want to move the token: (example -> 0,1) ')
                    y,x = coordinates
                    r = [y,x]
                    matrix[i][j] = ' '
                    if r in  player.availabletokens[z]:
                        matrix[y][x] = player.colortoken[0]
                        player.positiontokens.append([y,x])
                        if  matrix[i][j] == ' ' and c in player.positiontokens:
                            player.positiontokens.remove(c)
                            del player.availabletokens[z]
                        return matrix  
                    else:
                        print('This position is not free') 
                        return Movement.move_token(player,matrix)  
                else:
                    print('This token is not free ')
                    return Movement.move_token(player,matrix) 
        except:
            print('Your coordinates could not be read well ')
            return Movement.move_token(player,matrix)    
         