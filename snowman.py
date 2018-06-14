import random
from words import tech, internet, simple

snowman_states = []

snowman_states.append('''


                            Guessed: %s
                            Percentage Correct: %s

    Imagine a
    beautiful snowy         Do Not Fail Us
    field






The Phrase: %s
''')

snowman_states.append('''


                            Guessed: %s
                            Percentage Correct: %s


                            Bah! But is one mistake.
                            You can recover from this.


     ___________
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''


                            Guessed: %s
                            Percentage Correct: %s


      _________ 
     /         \            He is but two lumps!
    |           |           
    |           |
     \_________/
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''


       _______              Guessed: %s
      /       \             Percentage Correct: %s
     |         |                            
     |         |
      \_______/             We understand this is
     /         \            difficult but please
    |           |           proceed with caution.
    |           |
     \_________/
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''


       _______              Guessed: %s
      /       \             Percentage Correct: %s
     |  o      |                            
     |         |
      \_______/ 
     /         \            That black beady eye....
    |           |
    |           |
     \_________/
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''


       _______              Guessed: %s
      /       \             Percentage Correct: %s
     |  o   o  |                            
     |         |
      \_______/             Look deep into his soul.
     /         \            He thirsts.
    |           |
    |           |
     \_________/
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''


       _______              Guessed: %s
      /       \             Percentage Correct: %s
     |  o   o  |                            
     |  \___/  |
      \_______/ 
     /         \            This smile is a trick!
    |           |           You can only make 3 more mistakes.
    |           |
     \_________/
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''


       _______              Guessed: %s
      /       \             Percentage Correct: %s
     |  o   o  |                            
     |  \___/  |
      \_______/ 
     /         \            With one appendage he will
    |           |--|-       difficult to stop
    |           |
     \_________/
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''


       _______              Guessed: %s
      /       \             Percentage Correct: %s
     |  o   o  |                            
     |  \___/  |
      \_______/ 
     /         \            With two, he becomes
-|--|           |--|-       infinite. You have one
    |           |           last shot to end this.
     \_________/
    /           \ 
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

snowman_states.append('''
       _______
      |       |
     _|_______|_            Guessed: %s
      / \   / \             Percentage Correct: %s
     |  o   o  |                            
     |  \___/  |
      \_______/ 
     /         \            HE HAS BEEN FORMED!
-|--|           |--|-       THE WORLD SHALL FALL
    |           |           TO THE MIGHT OF THE 
     \_________/            SNOWMAN!
    /           \           
   |             |    
   |             |
    \___________/

The Phrase: %s
''')

class Snowman:

    mistakes = 0
    successes = 0
    total = 0
    the_word = ''
    the_blanks = []
    guessed = ''
    percentage = ''

    def start_game(self):
        print('Welcome to Snowman!')
        choosing = True
        while(choosing):
            print('''You get to pick the list of words you would like the game to pick from.
            If you would like to go with some simple words, enter the letter S.
            For something a little more difficult and more tech related, enter the letter T.
            If you want to open yourself to some difficult words, enter I.
            I grabs a word from the internet, so you could get something really difficult.''')
            choice = input()
            if choice.lower() == 'i':
                self.the_word = self.get_word('i')
                choosing = False
            elif choice.lower() == 't':
                self.the_word = self.get_word('t')
                choosing = False
            elif choice.lower() == 's':
                self.the_word = self.get_word('s')
                choosing = False
            else:
                print('Invalid input.')

        self.the_blanks = ['-'] * len(self.the_word)

        while(self.mistakes != len(snowman_states)-1) and not (self.blanks_string().isalpha()):
            self.print_state()
            print('''Please enter your guess; A Single Letter will be interpreted as a single letter guess.
            If you like, you can type out the whole word as a guess, but incorrectly guessing also counts
            as a mistake.\n''')
            guess = input().lower()
            self.check_input(guess)

        self.print_state()
        if(self.mistakes == len(snowman_states)-1):
            print('And so the world fell to the wrath of the Snowman, and the new Ice Age began.')
            print('The word was %s' % self.the_word)
        elif(self.blanks_string().isalpha()):
            print('Congrats! You win!')

    def get_word(self, type):
        if type == 'i':
            return str(random.choice(internet).lower())[2:-1]
        elif type == 't':
            return random.choice(tech)
        elif type == 's':
            return random.choice(simple)

    def print_state(self):
        if(self.total == 0):
            print (snowman_states[self.mistakes] % (self.guessed, 'N\A', self.blanks_string()))
        else:
            print (snowman_states[self.mistakes] % (self.guessed, '{:.1%}'.format(self.successes / self.total), self.blanks_string()))

    def check_input(self, input):
        if not input.isalpha():
            print ('Incorrect input. Only letters are taken')
        elif len(input) == 0:
            print ('No input.')
        elif len(input) == 1:
            self.check_letter(input)
        elif len(input) > 1:
            self.check_guess(input)

    def check_guess(self, guess):
        if guess.lower() == self.the_word.lower():
            print('Solid guess my friend. Victory goes to you.')
            self.the_blanks = self.the_word
        else:
            print('Incorrect guess! You fool! The Snowman grows stronger!')
            self.mistakes += 1


    def check_letter(self, letter):
        if not self.check_if_guessed(letter):
            self.guessed = self.guessed + letter
            locations = self.find(self.the_word, letter)
            if not locations:
                print('No dice. That letter is not in the word.')
                self.mistakes += 1
                self.total += 1
            else:
                print ('Nice! That letter is in the word!')
                self.successes += 1
                self.total += 1
                for x in locations:
                    self.the_blanks[x] = letter
        else:
            print('You already guessed that one friend.')

    def check_if_guessed(self, letter):
        if not self.find(self.guessed, letter):
            return False
        else:
            return True


    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def blanks_string(self):
        blanks_string = ''
        for x in self.the_blanks:
            blanks_string = blanks_string + x
        return blanks_string


