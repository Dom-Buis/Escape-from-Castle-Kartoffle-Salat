#import things
import sys
import time

#font colour change for input text
INPUT_COLOUR = '\033[90m'
RESET = '\033[0m'

#start the timer
start = time.time()

#make text typewriter style
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

#dictionary for player inventory
inventory = {"Bedroom Key": False, "Kitchen Key": False, "Lounge Key": False}
#print original text/backstory
typing("You were on a hike in the alps. You felt the cold snow beneath your boots, \nyou were doing well on the hike, but then you slipped and hit your head on the ice......  \nYou fell unconscious. \nNow you've woken up here, in the bedroom of a strange manor.")
print()

#first room
typing2("You are locked inside an aristocratic bedroom, \nthere's a king size bed next to you with a duvet on it, and theres two comfy looking cushions, \nyou feel like you could sleep here...\n")

#code to escape the first room
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
          typing("that isn't a valid option")
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
    typing("that isn't a valid option")

#enter the hallway
typing("You are now in the manor's hallway, \nthere's doors to every room in the mansion, \nthough the door to the dining room is the only open one.\n")
while True:
  rooms = input(f"{INPUT_COLOUR}Where do you go, the dining room or the bedroom? \n(You can also access the other rooms such as the Kitchen or the Lounge if it has been specified you have the key, \njust type in the name of the room.)\n{RESET}").upper()

  #go back to the bedroom
  if rooms == "BEDROOM":
      typing2("You go back into the bedroom, you don't find anything there.\n")

#go to dining room
  elif rooms == "DINING ROOM":
      if inventory["Kitchen Key"] == True:
         typing("You go back into the dining room, it's still a pretty boring room. \nThere's a nice mable table, \naswell as some fancy stained glass cups.")
      elif inventory["Kitchen Key"] == False:
        typing2("You explore the dining room and you find a vase.\n")
        vase = input(f"{INPUT_COLOUR}Do you check the vase? \n{RESET}").upper()
        if vase == "YES":
          while True:
            vase_investigate = input(f"{INPUT_COLOUR}To check under the vase type 'UNDER', \nto check the sides of the inside of the vase type 'SIDES', \nto check the front of the inside of the vase type 'FRONT', \nand to check back of the inside of the vase, type 'BACK'. \n{RESET}").upper()
            if vase_investigate == "UNDER":
                typing("You check under the vase, \nyou do not find anything there.")
            elif vase_investigate == "SIDES":
                typing("You put your hand inside the vase, and scrape the sides, \nyou don't find anything.")
            elif vase_investigate == "FRONT":
                typing("You put your hand into the vase, and you scrape the front of it, \nyou find nothing but some old dirt.")
            elif vase_investigate == "BACK":
                typing("You put your hand into the vase, \nyou feel around the back of the inside of the vase......... \nYou find a key to the kitchen\n")
                inventory["Kitchen Key"] = True
                break
            else:
               typing("The vase judges you.\n\n\n >:(\n\n")
        elif vase  == "NO":
          typing("Maybe you should check the vase?\n")
        else:
          typing("......ITS A YES OR NO???\n")
  elif rooms == "KITCHEN" and inventory["Kitchen Key"] == True:
     typing2("You walk into the kitchen and you see a fancy kitchen..... \nThere's a smell of baking powder in the air and there's lots of drawers, \nthere is also a potted plant at the side of the room...... \nIt feels a bit out of place. \nOh there's also a knife block maybe there's a key hidden in one of the knives......\n")
     while True:
      investigate = input(f"{INPUT_COLOUR}Where in the room do you check? \nThere may be a key somewhere, \nif you want to check out the drawers to find the weird baking soda smell type 'BAKING POWDER', \nif you want to check out the potted plant type 'POTTED PLANT', \nPerhaps you should see what would happen if you typed 'KNIVES'.\n{RESET}").upper()
      if investigate == "BAKING POWDER":
         typing("You check the different drawers in the kitchen, \nyou find lots of stuff, \neven a spatula made of gold, \nbut you still can't find the key......")
      elif investigate == "POTTED PLANT":
        typing("You check the potted plant, \nit's a nice plant, probably some kind of austrian shrub, \nand then you find it..... \nTHE LOUNGE KEY....... \n:)\n\n")
        inventory["Lounge Key"] = True
        break
      elif investigate == "KNIVES":
         typing("You check the Knife Block, \nyou are a bit clumsy and accidentally cut your finger on a butcher's knife, \nsomehow it didn't draw blood, \nyou still need to find the key however.")
      else:
          typing("try one of the options above, \nor just stop doing typos.\n")
  elif rooms == "KITCHEN" and inventory["Kitchen Key"] == False:
    typing("The door won't budge, \nmaybe try to find the Kitchen Key.")
  elif rooms == "LOUNGE" and inventory["Lounge Key"] == True:
    typing("You go into the lounge...... \nThere's no clear exit, \nThere's gotta be a way out somewhere, \nMaybe there's a way out in another room.... \n\nBut where?\n\n")
  else:
    typing("There aren't any other rooms, \nwas that a typo?")
     

 
#end the timer and print the time it took for the program to run
end = time.time()

length = end - start
num = length
num1 = num/60
time1 = round(num1, 1)
print("Program ran for", time1, "minutes")
