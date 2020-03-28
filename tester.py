class nb_players:
    def __init__(self,nb):
        self.nb=nb
        
    def hmp(self):
        print("There are " + str(self.nb) + " players. Prepare for the battle!")
        
nb_players = nb_players(3)

for i in range(nb_players.nb):
    print(i)

nb_players.hmp()




class Player:
    players_list = []
    
    def __init__(self, name = "Anonymous", IA = "Bot", player_number = int, cards = np.array([]), cave = np.array([])):
        self.name = name
        self.IA = IA
        self.player_number = player_number
        self.cards = cards
        self.cave = cave
        self.players_list.append(self)
    
    
    def myname(self):
        if self.IA == "Bot" :
            print("Hello my name is " + self.name + ". I'm a robot.")
        else:
            print("Hello my name is " + self.name + ".")


nb_players.hmp()

class game_turn_nb:
    def __init__(self,num = 1):
        self.num=num
        
    def which_turn(self):
        print("It's turn number " + str(self.num) + "!")
        
game_turn_nb = game_turn_nb()        
game_turn_nb.which_turn()