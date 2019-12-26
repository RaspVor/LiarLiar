class nb_players:
    def __init__(self,nb):
        self.nb=nb
        
    def hmp(self):
        print("There are " + str(self.nb) + " players. Prepare for the battle!")
        
nb_players = nb_players(3)

for i in range(nb_players.nb):
    print(i)
