def shuffle_deck(deck):
    deck_copy = deck
    np.random.shuffle(deck_copy)
    return(deck_copy)


def HowManyPlayers():
    
    
    sg.ChangeLookAndFeel('DarkAmber')
    # All the stuff inside the window.
    layout = [  [sg.Text('How many summoners?')],
                [sg.Text('Give me a number'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Introduce yourself!', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Ok'):   # if user closes window or clicks cancel
            
            print(values[0], "challengers will compete")
            break
    
    window.close()
    
    return(nb_players(int(values[0])))
    

def WhoAreYou(num=int):
    sg.ChangeLookAndFeel('GreenTan')
    # All the stuff inside the window.
    layout = [  [sg.Text('My Lord,')],
                [sg.Text('What is your summoner name?'), sg.InputText()],
                [sg.Text('Are your a human?'), sg.Radio('I am a human!     ', "RADIO1"), sg.Radio('I am a ROBOT!    ', "RADIO1", default=True)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Introduce yourself!', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        
        player_statut = "as an IA!"
        player_statut_official = "Bot"
        
        if values[1] == True:
            player_statut = "as a humanoid!"
            player_statut_official = "Human"

            
        print(values[0], "has joined the game", player_statut)
        break
    
    window.close()
    
    Player(values[0], player_statut_official, num)