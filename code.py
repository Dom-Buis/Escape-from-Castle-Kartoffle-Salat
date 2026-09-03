#import things
import sys
import time

#start the timer
start = time.time()


#ask the user if they want to start the game at basic settings or change the settings
print('Would you like to start the game or open game settings? (type "game" or "settings")')
game = input('').upper()

#ask the user to type either game or settings if they do not enter a valid option
if game != ('GAME') or ('SETTINGS'):
    print('Please enter a valid option...\n')
    print('Would you like to start the game or open game settings? (type "game" or "settings")')
    game = input('').upper()

#code for if the user just wants to play the game at basic settings without changing the settings
if game == ('GAME'):
    #change the colour of text and input text
    INPUT_COLOUR = '\033[90m'
    RESET = '\033[0m'

#make text typewriter style text at basic settings
    def typing(text, delay=0.1):
        for character in text:
            sys.stdout.write(character)  
            sys.stdout.flush()            
            time.sleep(delay)
    def typing2(text, delay=0.07):
        for character in text:
            sys.stdout.write(character)  
            sys.stdout.flush()            
            time.sleep(delay)


#code for if the user wants to open and edit the games settings
elif game == ('SETTINGS'):
    #ask the user what text speed they want
    print('Please choose text speed: (slow, medium, fast)')
    text_speed = input('').upper()
    #code for slow text speed
    if text_speed == ('SLOW'):
        def typing(text, delay=0.15):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)
        def typing2(text, delay=0.12):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)

#code for medium text speed
    if text_speed == ('MEDIUM'):
        def typing(text, delay=0.1):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)
        def typing2(text, delay=0.07):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)

#code for fast text speed
    if text_speed == ('FAST'):
        def typing(text, delay=0.06):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)
        def typing2(text, delay=0.03):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)
            
#code for ultra fast text speed. intended for testing and dev use only
    if text_speed == ('SKIP'):
        def typing(text, delay=0.001):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)
        def typing2(text, delay=0.001):
            for character in text:
                sys.stdout.write(character)  
                sys.stdout.flush()            
                time.sleep(delay)

#ask the user to choose a text colour and code for all text colours. pink is a secret option :)
    print('Please choose a text colour: (white, grey, red, yellow, green, blue)')
    text_colour_choice = input('').upper()
    if text_colour_choice == ('WHITE'):
        RESET = '\033[0m'
    if text_colour_choice == ('GREY'):
        RESET = '\033[90m'
    if text_colour_choice == ('RED'):
        RESET = '\033[91m'
    if text_colour_choice == ('YELLOW'):
        RESET = '\033[93m'
    if text_colour_choice == ('GREEN'):
        RESET = '\033[92m'
    if text_colour_choice == ('BLUE'):
        RESET = '\033[96m'
    if text_colour_choice == ('PINK'):
        RESET = '\033[95m'

#ask the user to choose an input text colour and code for all input text colours. pink is still a secret option :). text colour and input text colour can be the same
    print('Please choose a input-text colour: (white, grey, red, yellow, green, blue)')
    input_text_colour_choice = input('').upper()
    if input_text_colour_choice == ('WHITE'):
        INPUT_COLOUR = '\033[0m'
    if input_text_colour_choice == ('GREY'):
        INPUT_COLOUR = '\033[90m'
    if input_text_colour_choice == ('RED'):
        INPUT_COLOUR = '\033[91m'
    if input_text_colour_choice == ('YELLOW'):
        INPUT_COLOUR = '\033[93m'
    if input_text_colour_choice == ('GREEN'):
        INPUT_COLOUR = '\033[92m'
    if input_text_colour_choice == ('BLUE'):
        INPUT_COLOUR = '\033[96m'
    if input_text_colour_choice == ('PINK'):
        INPUT_COLOUR = '\033[95m'
        


#dictionary for player inventory
inventory = {"Bedroom Key": False, "Kitchen Key": False, "Lounge Key": False, "Manor Key": False}

#main menu and all admin done. into the actual game now

#print original text/backstory
print(f"{RESET}")
typing("You were on a hike in the alps. You felt the cold snow beneath your boots, \nyou were doing well on the hike, but then you slipped and hit your head on the ice......  \nYou fell unconscious. \nNow you've woken up here, in the bedroom of a strange manor.")
print()

#describe the bedroom
typing2("You are locked inside an aristocratic bedroom, \nthere's a king size bed next to you with a duvet on it, and theres two comfy looking cushions, \nyou feel like you could sleep here...\n")

#code to ask what the user wants to do in the first room
typing2("What do you do?\n")
while True:
  search = input(f"{INPUT_COLOUR}Do you try the door or do you search the room? \nTo try the door type 'DOOR', and to search the room type 'ROOM'. \n{RESET}").upper()
  if search == "ROOM":
    while True:
        #code to explore the first room
        where = input(f"{INPUT_COLOUR}Where in the room do you check? \nThere are 3 spots, there's a pillowcase, there's the vase, and there is behind the curtain. \nTo check the pillowcase type 'PILLOWCASE'. \nTo check the vase type 'VASE', \nand to check behind the curtain type 'CURTAIN'.{RESET}\n").upper()
        if where == "CURTAIN":
          typing("You check the curtain and find nothing there.\n")
        elif where == "VASE":
          typing("You check the vase and get your hand stuck in it, \nyou break the vase on the bedside cabinet.\n")
        elif where == "PILLOWCASE":
          typing("You checked the pillowcase, and you found the key.\n")
          #get bedroom key
          inventory["Bedroom Key"] =True
          break
        else:
          typing("that isn't a valid option\n")
          #open the door
  elif search == "DOOR":
      typing2("The door won't budge.\n")
      if inventory["Bedroom Key"] == True:
        key_used = input(f"{INPUT_COLOUR}Try the key? \nType 'YES' for yes, or 'NO' for no.\n{RESET}").upper()
        if key_used == 'YES':
            typing2("The door opens and you exit the bedroom.\n")
            break
        elif key_used == 'NO':
            typing("Maybe you should try the key.\n")
        else:
            typing("That's not even a option.\n")
  else:
    typing("that isn't a valid option\n")

#enter the hallway
typing("You are now in the manor's hallway, \nthere's doors to every room in the mansion, \nthough the door to the dining room is the only open one.\n")
while True:
  rooms = input(f"{INPUT_COLOUR}Where do you go, the dining room or the bedroom? \n(You can also access the other rooms such as the Kitchen or the Lounge if it has been specified you have the key, \njust type in the name of the room.)\n{RESET}").upper()

  #go back to the bedroom
  if rooms == "BEDROOM":
      typing2("You go back into the bedroom, you don't find anything there.\n")
  if rooms == "BEDROOM" and inventory["Lounge Key"] == True:
     typing2("You go back to the bedroom, \nyou see a hairbrush, \nyou didn't notice it before, \nit has the name, Halzinger on it.")

#go to dining room
  elif rooms == "DINING ROOM":
      if inventory["Kitchen Key"] == True and inventory["Lounge Key"] == False:

        #describe the dining room
         typing("You go back into the dining room, it's still a pretty boring room. \nThere's a nice mable table, \naswell as some fancy stained glass cups.\n")
      elif inventory["Lounge Key"] == True:

        #code for entering in dining room if the user already has the lounge key. they can find the exit here
         typing("You go back into the dining room again, \nyou are upset, \nyou don't know where the exit is, it was meant to be in the lounge...... \n\n\nWait, the rug? \nIs that a trapdoor under it?\n\n")
         while True:

        #the user finds the trapdoor to escape
          trapdoor = input(f"{INPUT_COLOUR}You walk over to the trapdoor, you try to open it...... \nIt's locked. \nDo you you try to investigate the trapdoor, or do you just leave? \nTo investigate type 'INVESTIGATE', \nto leave type 'LEAVE'.\n{RESET}").upper()
          if trapdoor == "INVESTIGATE":
            typing("You investigate the trapdoor, \nyou find out there are rules to it, \nyou need to input the names of the three keys. \nThat being the 'BEDROOM KEY', \nthe 'KITCHEN KEY', \nand the 'LOUNGE KEY'. \nYou need to input them opposite to the order you got them. \n")
            key1 = input(f"{INPUT_COLOUR}What was the most recent key? \n{RESET}").upper()
            if key1 == "LOUNGE KEY":
              typing("The first one of the three locks on the trapdoor click, \nyou have two left to get through.\n")
              key2 = input(f"{INPUT_COLOUR}What was the 2nd key that you got? \n{RESET}").upper()
            else:
              typing("You realize you put in the wrong key and have to try again.")
              if key2 == "KITCHEN KEY":
                 typing("The second of the three locks on the trapdoor click, \nyou have one left to get through.\n")
                 key3 = input(f"{INPUT_COLOUR}What was the first key that you got? \n{RESET}").upper()
              else:
                 typing("You realize you put in the wrong key and have to try again.")
                 if key3 == "BEDROOM KEY":
                    typing("The trapdoor opens, and you descend down, \nyou climb down the ladder, \nit goes down, and down, and down, and you enter a hidden room, \nit's moldy and damp, and there's a box in it, \nto open it...... \nYou need the manor director's name.\n")
                    director_name = input(f"{INPUT_COLOUR}What is the Manor Director's name?\n{RESET}").upper()
                 else:
                    typing("You realize you put in the wrong key and have to try again.")
                    if director_name == "HALZINGER":
                       typing("You unlock the box, \nyou slowly open it\n you hear the creak of the rusty latch...... \n\nWait, \nis that, \nTHE MANOR KEY.\n")
                       inventory["Manor Key"] = True
                       break
                    else:
                       typing("You try to put that in but the lock on the box doesn't budge.")
          if trapdoor == "LEAVE":
            typing("For some reason you decide to leave......\n")
            break
      elif inventory["Kitchen Key"] == False:

        #finding vase in the dining room
        typing2("You explore the dining room and you find a vase.\n")
        #ask if the user wants to investiage the vase
        vase = input(f"{INPUT_COLOUR}Do you check the vase? \ntype 'YES' for yes, \ntype 'NO' for no.\n{RESET}").upper()
        if vase == "YES":
          while True:

            #ask where in the vase the user wants to look
            vase_investigate = input(f"{INPUT_COLOUR}To check under the vase type 'UNDER', \nto check the sides of the inside of the vase type 'SIDES', \nto check the front of the inside of the vase type 'FRONT', \nand to check back of the inside of the vase, type 'BACK'. \n{RESET}").upper()
            if vase_investigate == "UNDER":
              typing("You check under the vase, \nyou do not find anything there.\n")
            elif vase_investigate == "SIDES":
              typing("You put your hand inside the vase, and scrape the sides, \nyou don't find anything.\n")
            elif vase_investigate == "FRONT":
              typing("You put your hand into the vase, and you scrape the front of it, \nyou find nothing but some old dirt.\n")
            elif vase_investigate == "BACK":
                #find the kitchen key in the back of the vase
              typing("You put your hand into the vase, \nyou feel around the back of the inside of the vase......... \nYou find a key to the kitchen\n")
              inventory["Kitchen Key"] = True
              break
            else:
                #code for if the user enters and invalid option
              typing("The vase judges you.\n\n\n>:(\n\n")
        elif vase  == "NO":
          typing("Maybe you should check the vase?\n")
        else:
          typing("It's a YES or a NO!?!?!\n\n\n")



  elif rooms == "KITCHEN" and inventory["Kitchen Key"] == True:
    #entering the kitchen
     typing2("You walk into the kitchen and you see a fancy kitchen..... \nThere's a smell of baking powder in the air and there's lots of drawers, \nthere is also a potted plant at the side of the room...... \nIt feels a bit out of place. \nOh there's also a knife block maybe there's a key hidden in one of the knives......\n")
     while True:
        #ask what the user wants to do in the kitchen
      investigate = input(f"{INPUT_COLOUR}Where in the room do you check? \nThere may be a key somewhere, \nif you want to check out the drawers to find the weird baking soda smell type 'BAKING POWDER', \nif you want to check out the potted plant type 'POTTED PLANT', \nPerhaps you should see what would happen if you typed 'KNIVES'.\n{RESET}").upper()
      if investigate == "BAKING POWDER":
         typing("You check the different drawers in the kitchen, \nyou find lots of stuff, \neven a spatula made of gold, \nbut you still can't find the key......\n")
      elif investigate == "POTTED PLANT":
        typing("You check the potted plant, \nit's a nice plant, probably some kind of austrian shrub, \nand then you find it..... \nTHE LOUNGE KEY....... \n:)\n\n")
        inventory["Lounge Key"] = True
        break
      elif investigate == "KNIVES":
         typing("You check the Knife Block, \nyou are a bit clumsy and accidentally cut your finger on a butcher's knife, \nsomehow it didn't draw blood, \nyou still need to find the key however.")
      else:
          typing("try one of the options above, \nor just stop doing typos.\n")
  elif rooms == "KITCHEN" and inventory["Kitchen Key"] == False:
    typing("The door won't budge, \nmaybe try to find the Kitchen Key.\n")
  elif rooms == "LOUNGE" and inventory["Lounge Key"] == True:
    typing("You go into the lounge...... \nThere's no clear exit, \nThere's gotta be a way out somewhere, \nMaybe there's a way out in another room.... \n\nBut where?\n\n")
  elif rooms == "LOUNGE" and inventory["Lounge Key"] == False:
     typing("You can't open the door, \nthe exit is in there right?\n")
  else:
    typing("There aren't any other rooms, \nwas that a typo?\n")
     

 
#end the timer and print the time it took for the program to run
end = time.time()

length = end - start
num = length
num1 = num/60
time1 = round(num1, 1)
print("Program ran for", time1, "minutes")
