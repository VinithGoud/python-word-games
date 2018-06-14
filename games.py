from snowman import Snowman

playing = True
while(playing):
    print('''Welcome to word games! What game would you like to play?''')
    print('''The options are :
            snowman''')
    print('''Input the name of the game to select it!
            or type \'exit\' to leave :(''')
    desire = input()
    if desire == 'snowman':
        game = Snowman()
        game.start_game()
    elif desire == 'exit':
        playing = False