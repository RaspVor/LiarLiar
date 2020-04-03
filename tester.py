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


class game_turn:
    myMatrix = pd.DataFrame(columns=["turn", "picker_name", "picker_cards", "picker_call", "caller_name", "caller_choose", "winner"])
    
    def __init__(self,turn_num = 1, first = 0, players_list = [],picker_name = "ERROR", picker_cards = "ERROR", picker_call = "ERROR", caller_name = "ERROR", caller_choose = "ERROR", winner = "ERROR"):
        self.turn_num = turn_num
        self.first = first
        self.players_list = players_list
        self.picker_name = picker_name
        self.picker_cards = picker_cards
        self.picker_call = picker_call
        self.caller_name = caller_name
        self.caller_choose = caller_choose
        self.winner = winner
        self.myMatrix = pd.concat([myMatrix, pd.dataframe([self.turn_num,self.picker_name,self.picker_cards,self.picker_call,self.caller_name,self.caller_choose,self.winner])], ignore_index=True)

    
    def which_turn(self):
        print("It's turn number " + str(self.turn_num) + "! " + str(self.players_list[self.first].name) + " starts !")
   
    
   
  # def turn(self):
      
#tour 1
game_turnZ = game_turn(1,dice.winner,Player.players_list)  
game_turnZ.which_turn()




class turn_start:
    def __init__(self,turn_num = 1, player_number = 0, players_list = []):
        self.turn_num = turn_num
        self.player_number = player_number
        self.players_list = players_list
    
    def which_turn(self):
        print("It's turn number " + str(self.turn_num) + "! " + str(self.players_list[self.player_number].name) + " starts !")

#tour 1
turn_startZ = turn_start(1,dice.winner,Player.players_list)  
turn_startZ.which_turn()


class turn_picker:
    def __init__(self, player_number = 0, players_list = [], picker_cards = "ERROR", picker_call = "ERROR"):
        self.player_number = player_number
        self.players_list = players_list
        self.picker_cards = picker_cards
        self.picker_call = picker_call
    
    def turn_picker_call(self):
        print("Me! Summoner " + str(self.players_list[self.player_number].name) + "! I call " + str(self.picker_call) + "!")

#tour 1
turn_pickerZ = turn_picker(dice.winner,Player.players_list, "Leviathan", "Shiva")  
turn_pickerZ.turn_picker_call()


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

#tour 1
turn_callerZ = turn_caller((dice.winner+1)%len(Player.players_list),Player.players_list, "TRUE")  
turn_callerZ.turn_caller_call()
turn_callerZ = turn_caller((dice.winner+1)%len(Player.players_list),Player.players_list, "FALSE")  
turn_callerZ.turn_caller_call()


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

    def tellwhowon(self):
        if ((self.picker_cards == self.picker_call) and self.caller_choose == "TRUE") or ((self.picker_cards != self.picker_call) and self.caller_choose == "FALSE"):
            print(str(self.players_list[(self.player_number+1)%len(self.players_list)].name) + " WON!!!")
        else:
            print(str(self.players_list[self.player_number].name) + " WON!!!")

#tour 1
who_wonZ1 = who_won(dice.winner,Player.players_list,"Leviathan", "Shiva","TRUE") 
who_wonZ1.tellwhowon()

who_wonZ2 = who_won(dice.winner,Player.players_list,"Leviathan", "Shiva","FALSE") 
who_wonZ2.tellwhowon()

who_wonZ3 = who_won(dice.winner,Player.players_list,"Leviathan", "Leviathan","TRUE") 
who_wonZ3.tellwhowon()

who_wonZ4 = who_won(dice.winner,Player.players_list,"Leviathan", "Leviathan","FALSE") 
who_wonZ4.tellwhowon()



column_names = ["turn", "picker_number", "caller_number", "picker_cards", "picker_call", "caller_choose", "winner"]
myMatrix = pd.DataFrame(columns = column_names)
myMatrix_temp = pd.DataFrame([[game_turnZ.turn_num,dice.winner,(dice.winner+1)%len(Player.players_list),"Leviathan", "Shiva","TRUE",who_wonZ1.return_winner()]],columns = column_names)

myMatrix = myMatrix.append(myMatrix_temp, ignore_index=True)   


class turn_results:
    myMatrix = pd.DataFrame(columns=["turn", "picker_number", "players_list", "picker_cards", "picker_call", "caller_choose", "winner"])
    
    def __init__(self,turn_num = 1, picker_number = 0, caller_number = 0, picker_cards = "ERROR", picker_call = "ERROR", caller_choose = "ERROR", winner = "ERROR"):
        self.turn_num = turn_num
        self.picker_number = picker_number
        self.caller_number = caller_number
        self.picker_cards = picker_cards
        self.picker_call = picker_call
        self.caller_choose = caller_choose
        self.winner = winner
        self.myMatrix.append(self, ignore_index=True)
        
    
#tour 1   
turn_resultsZ1 = turn_results(game_turnZ.turn_num,dice.winner,(dice.winner+1)%len(Player.players_list),"Leviathan", "Shiva","TRUE",who_wonZ1.return_winner())
turn_resultsZ2 = turn_results(game_turnZ.turn_num,dice.winner,Player.players_list,"Leviathan", "Shiva","FALSE",who_wonZ2.return_winner())
turn_resultsZ3 = turn_results(game_turnZ.turn_num,dice.winner,Player.players_list,"Leviathan", "Leviathan","TRUE",who_wonZ3.return_winner())
turn_resultsZ4 = turn_results(game_turnZ.turn_num,dice.winner,Player.players_list,"Leviathan", "Leviathan","FALSE",who_wonZ4.return_winner())


aaa = turn_resultsZ1.myMatrix

game_turnZ.players_list


column_names = ["turn", "picker_name", "picker_cards", "picker_call", "caller_name", "caller_choose", "winner",who_wonZ.return_winner()]
df = pd.DataFrame(columns = column_names)

df = pd.DataFrame([[1,2,3,4,5,6,7]],columns = column_names)
df.head()

len(Player.players_list)
