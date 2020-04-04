#Class

class nb_players:
    def __init__(self, nb=1):
        self.nb=nb
        
    def hmp(self):
        print("There are " + str(self.nb) + " players. Prepare for the battle!")



class Player:
    players_list = []
    
    def __init__(self, name = "Anonymous", IA = "Bot", player_number = int, cards = list(), cave = list()):
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


class card_played:
    def __init__(self, card = "ERROR"):
        self.card=card
        
class card_announced:
    def __init__(self, card = "ERROR"):
        self.card=card
        
class card_guessed:
    def __init__(self, card = "ERROR"):
        self.card=card

        

class dice:
    def __init__(self, winner = 0, players_list = []):
        self.winner = winner
        self.players_list = players_list
    
    def random_choose(self):
        self.winner = random.randint(1,len(self.players_list))-1
    
    def who_start(self):
        print(str(self.players_list[self.winner].name) + " starts !")


class counter_turn:
    def __init__(self, counter = 1, winner = 0):  
        self.counter = counter
        self.winner = winner

class turn_start:
    def __init__(self,turn_num = 1, player_number = 0, players_list = []):
        self.turn_num = turn_num
        self.player_number = player_number
        self.players_list = players_list
    
    def which_turn(self):
        print("It's turn number " + str(self.turn_num) + "! " + str(self.players_list[self.player_number].name) + " plays !")


class turn_picker:
    def __init__(self, player_number = 0, players_list = [], picker_cards = "ERROR", picker_call = "ERROR"):
        self.player_number = player_number
        self.players_list = players_list
        self.picker_cards = picker_cards
        self.picker_call = picker_call
    
    def turn_picker_call(self):
        print("Me! Summoner " + str(self.players_list[self.player_number].name) + "! I call " + str(self.picker_call) + "!")


class turn_caller:
    def __init__(self, player_number = 0, players_list = [], caller_choose = "ERROR"):
        self.player_number = player_number
        self.players_list = players_list
        self.caller_choose = caller_choose
    
    def turn_caller_call(self):
        if self.caller_choose == "TRUE":
            print("Me! Summoner " + str(self.players_list[self.player_number].name) + "! You tell the truth!")
        elif self.caller_choose == "FALSE":
            print("Me! Summoner " + str(self.players_list[self.player_number].name) + "! You are a LIAARRRRR!")



class who_won:
    def __init__(self, player_number = 0, players_list = [], picker_cards = "ERROR", picker_call = "ERROR", caller_choose = "ERROR"):
        self.player_number = player_number
        self.players_list = players_list
        self.picker_cards = picker_cards
        self.picker_call = picker_call
        self.caller_choose = caller_choose


    def return_winner(self):
        if ((self.picker_cards == self.picker_call) and self.caller_choose == "TRUE") or ((self.picker_cards != self.picker_call) and self.caller_choose == "FALSE"):
            return (self.player_number+1)%len(Player.players_list)
        else:
            return (self.player_number)
        
    def return_loser(self):
        if ((self.picker_cards == self.picker_call) and self.caller_choose == "TRUE") or ((self.picker_cards != self.picker_call) and self.caller_choose == "FALSE"):
            return (self.player_number)
        else:
            return (self.player_number+1)%len(Player.players_list)

    def tellwhowon(self):
        if ((self.picker_cards == self.picker_call) and self.caller_choose == "TRUE") or ((self.picker_cards != self.picker_call) and self.caller_choose == "FALSE"):
            print(str(self.players_list[(self.player_number+1)%len(self.players_list)].name) + " WON!!!")
        else:
            print(str(self.players_list[self.player_number].name) + " WON!!!")

    def showwhowon(self):
        if ((self.picker_cards == self.picker_call) and self.caller_choose == "TRUE") or ((self.picker_cards != self.picker_call) and self.caller_choose == "FALSE"):
            return(str(self.players_list[(self.player_number+1)%len(self.players_list)].name) + " WON!!!")
        else:
            return(str(self.players_list[self.player_number].name) + " WON!!!")