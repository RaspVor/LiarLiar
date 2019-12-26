#Who is playing?
nb_players = nb_players(3)

p1=Player("FrancoisBot", "Bot", 1)
p2=Player("Neuromancer", "Bot", 2)
p3=Player("Shooter", "Bot", 3)



#Shuffling the cards
deck = cards_game()

if nb_players.nb == 2:
    deck.cards_list = shuffle_deck(deck.cards_list)[:-10] 
else:
    deck.cards_list = shuffle_deck(deck.cards_list)

last_cards=np.array([])
if len(deck.cards_list) % nb_players.nb != 0:
    last_cards = deck.cards_list[-1]
    deck.cards_list = deck.cards_list[:-1]



#Distribution of the cards
nb_players.hmp()
    
for i in Player.players_list:
    i.myname()
    
    if i.player_number < nb_players.nb:
        i.cards = deck.cards_list.reshape(len(deck.cards_list)//nb_players.nb,nb_players.nb)[:,i.player_number-1]
    else:
        i.cards = np.append(deck.cards_list.reshape(len(deck.cards_list)//nb_players.nb,nb_players.nb)[:,i.player_number-1],last_cards)

        
        
