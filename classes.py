#Class

class nb_players:
    def __init__(self, nb=1):
        self.nb=nb
        
    def hmp(self):
        print("There are " + str(self.nb) + " players. Prepare for the battle!")



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




class cards_game:
    def __init__(self, cards_list = np.array(["Ifrit","Ifrit","Ifrit","Ifrit","Ifrit","Ifrit","Ifrit","Ifrit",
                                              "Shiva","Shiva","Shiva","Shiva","Shiva","Shiva","Shiva","Shiva",
                                              "Ondine","Ondine","Ondine","Ondine","Ondine","Ondine","Ondine","Ondine",
                                              "Ahuri","Ahuri","Ahuri","Ahuri","Ahuri","Ahuri","Ahuri","Ahuri",
                                              "Bahamut","Bahamut","Bahamut","Bahamut","Bahamut","Bahamut","Bahamut","Bahamut",
                                              "Leviathan","Leviathan","Leviathan","Leviathan","Leviathan","Leviathan","Leviathan","Leviathan",
                                              "Golgotha","Golgotha","Golgotha","Golgotha","Golgotha","Golgotha","Golgotha","Golgotha",
                                              "Taurus","Taurus","Taurus","Taurus","Taurus","Taurus","Taurus","Taurus"]),
                       last_cards=np.array([])
                 ):
        self.cards_list = cards_list
        self.last_cards = last_cards
        

class dice:
    def __init__(self, winner = 0, players_list = []):
        self.winner = winner
        self.players_list = players_list
    
    def random_choose(self):
        self.winner = random.randint(1,len(self.players_list))-1
    
    def who_start(self):
        print(str(self.players_list[self.winner].name) + " starts !")
        
class game_turn_nb:
    def __init__(self,num = 1, first = 0, players_list = []):
        self.num = num
        self.first = first
        self.players_list = players_list
    
    def which_turn(self):
        print("It's turn number " + str(self.num) + "! " + str(self.players_list[self.first].name) + " starts !")