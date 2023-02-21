# INF360 - Programming in Python
# Brian Nicewander
# Final Project

'''
My final is a text-based adventure game where the player lands on mars
and gets to pick different things. From where they go to what weapon they use if they
decide to attack. 
'''

import sys #This is to import the system exit function.
import logging #This is for debugging
logging.basicConfig(filename='myLogReport.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')

try:
    from direction import * #Imports all functions in direction
    from player import * #Imports all functions in player
    logging.debug('Files loaded successfully')
except:
    print('One of your files was not loaded. The program will now exit.')
    logging.critical('One of the files is missing.')
    sys.exit()

def start(): #This starts the game.
    
    player = playerOne() #This calls the Player() class in the player file.
    player.setNameAndAge() #This calls the setAge and setName function in the player file
    print('Hello ' + player.name + ' age ' + str(player.age) + ' I hope you are ready to go on an adventure. Your choices are in (); for example, (right) will be a choice you can make.')
          
    #This will ask them what way they want to go and make sure they pick one of the ways.      
    while True:
        direction = input('''You landed on Mars and just got out of your ship.
Do you want to go (left or right?) ''').lower().strip()#The lower function turns the letters to lowercase, and the strip function removes white space.
                          
        if direction == "left":
            left()#This will run the def left() function in the direction file.       
                    
        elif direction == "right":
            right()#This will run the def right() function in the direction file.

        else:
           print("That is not a valid diraction. Please try again!")

start()


#I GOT 100 PERCENT COMMENT: fix array on player file.

