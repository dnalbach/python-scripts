from os import system
import time

system('clear')

counter = 0
pattern_character = "*"

while True :

    if counter == 0 :
        flow_toggle = True
    
    if counter == 12 :
        flow_toggle = False
    
    if counter < 12 and flow_toggle == True :
        counter += 1
    
    if counter > 0 and flow_toggle == False :
        counter -= 1

    print pattern_character * (counter * counter)
    time.sleep(.01)

# Make terminal resolution higher (500x300+) to see more detail in shape





