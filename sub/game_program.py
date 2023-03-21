import sys
import random
def get_word():
    #Getting a random word from a list
    mylist=["hen","pen","elephant","kit","calculator","november","phone","report","pencil","calander","apple","orange","vegetable","facebook","industry","news","world","university","sanitizer","book"]
    return random.choice(mylist)

def game():
    #Getting user inputs to the random word.
    alphabet='abcdefghijklmnopqrstuvwxyz'
    letter_guessed = []
    word = get_word()
    tries = len(word)
    guessed = False
    count=0
    winst = ''
    
    
    print('The word has',len(word),'letters')
    print(len(word)*'_ ')
    while guessed == False and tries > 0:       
        print('you have '+ str(tries) + ' tries')
        letter = input('Gusse a letter:')
        if len(letter) == 1:
            if letter not in alphabet:
                print('ENTER A LETTER')
            elif letter in letter_guessed:
                print('LETTER IS ALREADY GUESSED')
            elif letter not in word:
                letter_guessed.append(letter)
                tries -=1
            elif letter in word:
                letter_guessed.append(letter)
            else:
                print('ERROR')

        x=''
        if guessed == False:
            for y in word:
                if y in letter_guessed:
                    x += y
                else:
                    x +='_ '
            print(x)
          
        if x == word:            
            print()
            print('YOU WON')
            winst = 'win'
            return (winst,tries,word)
            guessed = True
        elif tries == 0:
            print()
            print('YOU LOST')
            winst = 'lost'
            return (winst,tries,word)
            break
            
    
        
        
