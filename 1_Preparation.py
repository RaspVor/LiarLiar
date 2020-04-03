#How many players
nb_players = HowManyPlayers()

#Who is playing?
for i in range(nb_players.nb):
    WhoAreYou(i)



#Shuffling the cards
deck = cards_game()

if nb_players.nb == 2:
    deck.cards_list = shuffle_deck(deck.cards_list)[:-10] 
else:
    deck.cards_list = shuffle_deck(deck.cards_list)

if len(deck.cards_list) % nb_players.nb != 0:
    deck.last_cards = deck.cards_list[-1]
    deck.cards_list = deck.cards_list[:-1]



#Distribution of the cards
nb_players.hmp()
    
for i in Player.players_list:
    i.myname()
    
    if i.player_number < nb_players.nb:
        i.cards = np.unique(list(np.sort(deck.cards_list[:len(deck.cards_list)//nb_players.nb*nb_players.nb].reshape(len(deck.cards_list)//nb_players.nb,nb_players.nb)[:,i.player_number])), return_counts=True)
    else:
        i.cards = np.unique(list(np.sort(np.append(deck.cards_list[:len(deck.cards_list)//nb_players.nb*nb_players.nb].reshape(len(deck.cards_list)//nb_players.nb,nb_players.nb)[:,i.player_number],deck.last_cards))), return_counts=True)

    print(i.cards)
        

#Choose who start
dice = dice(0,Player.players_list)
dice.random_choose()
dice.who_start()

#Initialize Counter
counter_turnZ = counter_turn(1, dice.winner)


#THE GAME
turn_startZ = turn_start(1,counter_turnZ.winner,Player.players_list)  
turn_startZ.which_turn()


##pick & announce
if Player.players_list[counter_turnZ.winner].IA == "Bot" :
    card_picked = one_turn_IA_picked(counter_turnZ.counter, counter_turnZ.winner)
    card_announced = one_turn_IA_announce(counter_turnZ.counter, counter_turnZ.winner)
else:
    card_picked = one_turn_human_picked(counter_turnZ.counter, counter_turnZ.winner)
    card_announced = one_turn_human_announce(counter_turnZ.counter, counter_turnZ.winner) 
    
turn_pickerZ = turn_picker(counter_turnZ.winner,Player.players_list, card_picked, card_announced)  
turn_pickerZ.turn_picker_call()
    


##guess
if Player.players_list[(counter_turnZ.winner+1)%len(Player.players_list)].IA == "Bot" :
    choice_made = one_turn_IA_guess(counter_turnZ.counter, (counter_turnZ.winner+1)%len(Player.players_list))
    
else:
    choice_made = one_turn_human_guess(counter_turnZ.counter, (counter_turnZ.winner+1)%len(Player.players_list))


turn_callerZ = turn_caller((counter_turnZ.winner+1)%len(Player.players_list),Player.players_list, choice_made)  
turn_callerZ.turn_caller_call()    
    

##wicher
who_wonZ = who_won(counter_turnZ.winner,Player.players_list,card_picked, card_announced,choice_made) 
who_wonZ.tellwhowon()    
