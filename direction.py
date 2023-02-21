'''
This file runs when the user picks left or right.
'''
import sys

#This function runs if the user picks right as the direction above.
def right():
    #This will ask them what they want to do with the sword and make sure they only pick one of two options.
     while True:
            choice = input('After walking a while, you see a sword on the ground. Do you (pick-up or leave) the sword? ').lower().strip()

            #This runs if they choose pickup and then asks them a follow-up question about the sword.
            if choice == 'pick-up':
                while True:
                   choice = input('A monster pops up out of the ground before you can grab the sword. Do you (run) or try to (pick-up) the sword again? ').lower().strip()
                   if choice == "pick-up":
                       print('The monster swipes at you, hitting you in the air and killing you.')
                       sys.exit() #This function will stop the program from running.
                   elif choice == 'run':
                       print('You ran back to your ship as fast as you could and left Mars for good')
                       sys.exit()
                   else:
                       print('That is not a valid choice. Please try again!')

            #This runs if they leave the sword and then ask them about a gold chest they find.          
            elif choice == 'leave':
                while True:
                    print('You leave the sword behind and keep walking.')
                    choice = input('You see a gold treasure chest; as you walk up to it, you get a weird feeling about it. Do you (open) it or (leave) it alone? ').lower().strip()
                    if choice == 'open':
                        print('You find what looks like a rare piece of stone. You pick it up and head back to your ship to head home.')
                        sys.exit()
                    elif choice == 'leave':
                        print('You walk past the chest and look around the rest of mars and do not find anything else, so you had to return home empty-handed.')
                        sys.exit()
                    else:
                       print('That is not a valid choice. Please try again!')
            else:
                print('That is not a valid choice. Please try again!')  


#This function runs if the user picks left as the direction above.
def left():
    #This will ask them what they want to do with the sword and make sure they only pick one of two options.
     while True:
            choice = input('''You walk for a while and see a wall of strange fog.
Do you (walk-up) to the fog or try to find a way (around) it? ''').lower().strip()

            #This runs if they choose walk up to the fog.
            if choice == 'walk-up':
                while True:
                   choice = input('Walking up to the fog, you hear a strange voice telling you to touch the fog. Do you (touch) the fog or (keep-looking) at it? ').lower().strip()
                   if choice == "touch":
                       print('As you touch the fog, you can feel something grab ahold of you and pull you into the fog. You were never seen again.')
                       sys.exit() #This function will stop the program from running.
                   elif choice == 'keep-looking':
                       print('As you look into the fog, a strange figure starts forming. You can not look away; the figure pops out, stabs you with a knife, and kills you.')
                       sys.exit()
                   else:
                       print('That is not a valid choice. Please try again!')

            #This runs if they walk around the fog.          
            elif choice == 'around':
                while True:
                    choice = input('''You do not know if you will ever find the end of the fog, but after a while, you get to the end of it, and at the end, you see what looks like
another person walking toward you. Do you walk up to them to say (hi), or do you (run-away) back to your ship? ''').lower().strip()
                    if choice == 'hi':
                        print('As you walk up to the person, you see they look evil and have a weapon; you decide to start running away, but too late, they catch up to you and kill you.')
                        sys.exit()
                    elif choice == 'run-away':
                        print('''You take off in a dead sprint toward your ship as you look behind you. You see the person running after you, and they are getting closer.
But luckily, you make it back to your ship and back home safely.''')
                        sys.exit()
                    else:
                       print('That is not a valid choice. Please try again!')
            else:
                print('That is not a valid choice. Please try again!') 
