          
class Player(object):
    numplayer = 0
    def __init__(self,colortoken):
        self.points = 0
        self.canttokens = 12
        self.colortoken = colortoken
        self.positiontokens = []
        self.availabletokens = {}
        Player.numplayer += 1
        self.name = 'Player' + str(Player.numplayer)

    def opponent(self,opponent):
        self.opponent = opponent 
        return self.opponent.colortoken[0]  

