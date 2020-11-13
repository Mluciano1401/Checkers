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

class CharacterToken(object):
    def __init__(self,name,simbol):
        self.name = name
        self.simbol = simbol

class Token(CharacterToken):
    def __init__(self,name,simbol,value,Queen = False):
        CharacterToken.__init__(self,name,simbol)
        self.value = value
        if Queen == True:
            self.value = 2

    def positioninboard(self):  
        pass      






token1 = Token("white","0",1,Queen = False)
token2 = Token("Black","O",1,Queen = False)
board = Board()
print(board.matrix)