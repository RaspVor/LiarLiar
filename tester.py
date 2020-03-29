class nb_players:
    def __init__(self,nb):
        self.nb=nb
        
    def hmp(self):
        print("There are " + str(self.nb) + " players. Prepare for the battle!")
        
nb_players = nb_players(3)

for i in range(nb_players.nb):
    print(i)

nb_players.hmp()






nb_players.hmp()

class game_turn_nb:
    def __init__(self,num = 1):
        self.num=num
        
    def which_turn(self):
        print("It's turn number " + str(self.num) + "!")
        
game_turn_nb = game_turn_nb(1,dice.winner,Player.players_list)  
game_turn_nb.which_turn()