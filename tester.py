class nb_players:
    def __init__(self,nb):
        self.nb=nb
        
    def hmp(self):
        print("There are " + str(self.nb) + " players. Prepare for the battle!")
        
nb_players = nb_players(3)

for i in range(nb_players.nb):
    print(i)

nb_players.hmp()

np.array[1:nb_players.nb]
np.arange(1,nb_players.nb+1)

random.randint(1,len(Player.players_list))-1
np.arange(0,4)

print(myMatrix)
mkTkinter

nb_players.hmp()nb_players.listing(loser_num)
import threading
t = threading.Thread() 
t.setDaemon(True) 
t.start()

nb_players.listing.pop(who_wonZ.return_loser())

arr = nb_players.listing

nb_players.listing.remove(0)
nb_players.nb

np.delete(nb_players.listing, np.where(nb_players.listing == 0))


aa = nb_players(4,np.arange(0,4))
bb = nb_players(2,np.arange(0,2))
aa.listing
bb.listing

class A:
   
   def __init__(self, message="class message"):
        self.message=message
   
   @classmethod
   def cfoo(cls):
      print(cls.message)

   def foo(self, msg):
      self.message = msg
      print(self.message)

   def __str__(self):
      return self.message

a = A()
a.foo('instance call')

b = A()












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
myMatrix_temp = pd.DataFrame([[turn_startZ.turn_num,dice.winner,(dice.winner+1)%len(Player.players_list),"Leviathan", "Shiva","TRUE",who_wonZ1.return_winner()]],columns = column_names)

myMatrix = myMatrix.append(myMatrix_temp, ignore_index=True)   

topage_cards = np.where(Player.players_list[0].cards[0] == 'Ondine')[0][0]
topage_cave = np.where(Player.players_list[0].cave[0] == 'Ondine')[0][0]

topage_cards
topage_cave

print(Player.players_list[0].cards)
print(Player.players_list[0].cave)

Player.players_list[0].cards[1][Player.players_list[0].cards[1][topage_cards]] = Player.players_list[0].cards[1][Player.players_list[0].cards[1][topage_cards]] -1
Player.players_list[0].cave[1][Player.players_list[0].cave[1][topage_cave]] = Player.players_list[0].cave[1][Player.players_list[0].cave[1][topage_cave]] + 1

print(Player.players_list[0].cards)
print(Player.players_list[0].cave)



animals = Player.players_list[0].cards
animals[0]



print(Player.players_list[1].cards)


topage = np.where(Player.players_list[0].cards[0] == 'Ondine')[0][0]
topage

Player.players_list[0].cards[1][Player.players_list[0].cards[1][topage]] = Player.players_list[0].cards[1][Player.players_list[0].cards[1][topage]] -1


print(Player.players_list[0].cards)



cavernZ = (np.array(['Ahuri', 'Bahamut', 'Golgotha', 'Ifrit', 'Leviathan', 'Ondine', 'Shiva', 'Taurus'], dtype='<U9'), np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype='int64'))

cavernZ[0]

print('Updated animals list: ', animals)

z = np.unique(Player.players_list[0].cards, return_counts=True)
z
y = np.array(['Ahuri', 'Bahamut',  'Ondine', 'Shiva', 'Taurus'], dtype='<U9')
np.where(y == 'Ondine')[0][0]


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

z = deck.cards_list[:len(deck.cards_list)//nb_players.nb*nb_players.nb].reshape(len(deck.cards_list)//nb_players.nb,nb_players.nb)
z.shape

z[:,0].shape
z[:,1].shape
z[:,2].shape





def one_turn_human_guess(turn_number, after_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    radio_choices = ["TRUE", "FALSE"]
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( Player.players_list[after_winner].name + '. Make a choice!')],
                [sg.Radio(text, 1) for text in radio_choices],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            choice_indZ = list(values.values()).index(True)
            choiceZ = radio_choices[choice_indZ]
            
            break
    
    window.close()
    
    return(choiceZ)


def one_turn_IA_guess(turn_number, after_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    IAchoice =  np.random.choice(["TRUE", "FALSE"],1)[0]
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( 'Me, ' + Player.players_list[after_winner].name + '! I say it is ' + IAchoice)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            choiceZ = IAchoice
            
            break
    
    window.close()
    
    return(choiceZ)

choice_made =one_turn_human_guess(counter_turnZ.counter, (counter_turnZ.winner+1)%len(Player.players_list))
choice_made =one_turn_IA_guess(counter_turnZ.counter, (counter_turnZ.winner+1)%len(Player.players_list))


(counter_turnZ.winner+1)%len(Player.players_list)



np.where(Player.players_list[0].cave[1] > 3)[0]





def ifloser_die(turn_number, loser_num, players_list):
    
    if np.where(players_list[loser_num].cave[1] > 3)[0].size != 0:
        
        sg.ChangeLookAndFeel('DarkAmber')
        # All the stuff inside the window.
        
        IAchoice =  np.random.choice(["TRUE", "FALSE"],1)[0]
        
        
        layout = [  [sg.Text('Round ' + str(turn_number))],
                    [sg.Text( players_list[loser_num].name + ' is eliminated! Go to hell!!')],
                    [sg.Button('Ok'), sg.Button('Cancel')] ]
    
        # Create the Window
        window = sg.Window('Summoners! Rise Up', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event in (None, 'Cancel','Ok'):   # if user closes window or clicks cancel
                break
        
        window.close()
        
        players_list.pop(loser_num)
    
np.where(Player.players_list[0].cards[1] < 1)[0].size





check_ifloser_die(counter_turnZ.counter, who_wonZ.return_loser(), Player.players_list)

np.where(Player.players_list[0].cave[1] > 3)[0].size


zz = Player.players_list.pop(0)


Player.players_list[0].cave[1]
Player.players_list[1].cave[1]

zz[1].cave[1]

len(Player.players_list)
len(Player.players_list)
 
def one_turn_human_picked(turn_number, past_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    radio_choices = Player.players_list[counter_turnZ.winner].cards[0][np.where(Player.players_list[past_winner].cards[1] > 0 )[0]]
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( Player.players_list[past_winner].name + ' pick a card !')],
                [sg.Radio(text, 1) for text in radio_choices],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            card_played_indZ = list(values.values()).index(True)
            card_playedZ = radio_choices[card_played_indZ]
            
            break
    
    window.close()
    
    return(card_playedZ)



def one_turn_IA_picked(turn_number, past_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    IAchoice = np.random.choice(Player.players_list[counter_turnZ.winner].cards[0][np.where(Player.players_list[past_winner].cards[1] > 0 )[0]],1)[0]
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( 'Me, ' + Player.players_list[past_winner].name + '! I pick ' + IAchoice)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
        
            card_playedZ = IAchoice
            break
    
    window.close()
    
    return(card_playedZ)


card_played =one_turn_IA_picked(counter_turnZ.counter, counter_turnZ.winner)
card_played =one_turn_human_picked(counter_turnZ.counter, counter_turnZ.winner)




zz = Player.players_list[counter_turnZ.winner].cards[1]
zz = np.array([1, 4, 2, 4, 3, 2, 0, 4], dtype='int64')
aa = np.where(zz > 0 )[0]


Player.players_list[counter_turnZ.winner].cards[0][aa]











 np.random.choice(Player.players_list[counter_turnZ.winner].cards[0],1)[0]


one_turn_IA_call(counter_turnZ.counter, counter_turnZ.winner)

card_played =one_turn_IA_call(counter_turnZ.counter, counter_turnZ.winner)
card_played =one_turn_human_call(counter_turnZ.counter, counter_turnZ.winner)


zz = {0: False, 1: False, 2: True, 3: False, 4: False, 5: False, 6: False, 7: False}
card_played_ind = list(zz.values()).index(True)
list(zz.values())[card_played_ind]


radio_choices = Player.players_list[counter_turnZ.winner].cards[0][3]




{x: zz for x in (True)}
zz[2]
zz.index(True)

l=[]
[l.extend([k,v]) for k,v in zz]

zz.values()

people = [
{'name': "Tom", 'age': 10},
{'name': "Mark", 'age': 5},
{'name': "Pam", 'age': 7}
]

list(filter(lambda x: x == True, zz))







    
def one_turn_human_call(turn_number, past_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    radio_choices = Player.players_list[past_winner].cards[0]
    
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( Player.players_list[past_winner].name + ' makes a call. Choose a card !')],
                [sg.Radio(text, 1) for text in radio_choices],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            card_played_indZ = list(values.values()).index(True)
            card_playedZ = radio_choices[card_played_indZ]
            
            break
    
    window.close()
    
    return(card_playedZ)


def one_turn_IA_call(turn_number, past_winner):
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    
    IAchoice = np.random.choice(Player.players_list[past_winner].cards[0],1)[0]
    
    layout = [  [sg.Text('Round ' + str(turn_number))],
                [sg.Text( 'Me, ' + Player.players_list[past_winner].name + '! I summon ' + IAchoice)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Summoners! Rise Up', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
        
            card_playedZ = IAchoice
            break
    
    window.close()
    
    return(card_playedZ)


    