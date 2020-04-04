exec(open("./requirements.py").read())
exec(open("./classes.py").read())
exec(open("./functions.py").read())
exec(open("./1_Preparation.py").read())

myMatrix.to_csv('game_saved.csv',mode = 'w', index=False)

