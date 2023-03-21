import sys
import random
import sub.game_program as gf
import mysql.connector

print("Lets play Hangman!!")

def database_connection():
    #connecting with the database
    connection = {'host':'localhost',
           'database':'hangman_history',
           'user':'root',
           'password':''}
    
    database = mysql.connector.connect(**connection)
    return database

        
def insert(database,name,word,tries,winlost):
    #Inserting data to the database table(records table)
    number = random.randrange(1000,9999)#Selecting a random number
    listdata = [number,name,word,len(word),tries,winlost]

    record_update = str("INSERT INTO records VALUES "+str(tuple(listdata)).replace(' ',''))
    print('updating records to the database...')
    cursor =  database.cursor(record_update)
    cursor.execute(record_update)
    
    database.commit()
    database.close()
    

def replay():
    #Asking the user whether he/she wants to play again
    answer = input("Would you like to play again? yes or no:")
    if answer == 'no':
        sys.exit()
    else:        
        play = gf.game()
        
        print('name .',name)
        print('word is : ',play[2])
        print('win/lost',play[0])
        print('turns used = ',play[1])
        database = database_connection()
        insert(database,name,play[2],play[1],play[0])
        replay()

st = input('Do you want to play game? yes or no:')

if st == 'yes':
    name = input('enter your name : ')
    play = gf.game()
    
    print('name .',name)
    print('word is : ',play[2])
    print('win/lost',play[0])
    print('turns used = ',play[1])
    database = database_connection()
    insert(database,name,play[2],play[1],play[0])
    
    replay()

