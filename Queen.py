class MovementQueen(object):
     def __new__(self,player,matrix,target):
        self.player = player
        self.matrix = matrix
        self.target = target
        for e in player.positiontokens:
            newpositiontokens = []
            y= e[0]
            x= e[1]
            if player.colortoken == "White" and y == 1:
                matrix[y,x]= 'QW'   
                     
            if player.colortoken == "Black"  and y == 8:
                matrix[y,x] = 'QB'
            if x < 10 and y < 10 and x > 0 and y > 0:
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
