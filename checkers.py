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

class Token(object):
    def __init__(self,name,simbol,value,Queen = False):
        self.name = name
        self.simbol = simbol
        self.value = value
        if Queen == True:
            self.value = 2


        

     






token1 = Token("white","0",1,Queen = False)
token2 = Token("Black","O",1,Queen = False)
board = Board()
print(board.matrix)
print(token1.__dict__)