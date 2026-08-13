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

#print original text/backstory
def backstory():
  typing("You were on a hike in the alps. You felt the cold snow beneath your boots, \nyou were doing well on the hike, but then you slipped and hit your head on the ice......  \nYou fell unconscious. \nNow you've woken up here, in the bedroom of a strange manor.")
backstory()
print()

#first room
have_bedroom_key = 'false'
typing2("You are locked inside an aristocratic bedroom, \nthere's a king size bed next to you with a duvet on it, and theres two comfy looking cushions, \nyou feel like you could sleep here...\n")
def bedroom_key():
  if have_bedroom_key == 'false':
    typing2("'Now, lets find that key'")
  if have_bedroom_key == 'true':
    typing2("Alright, it's time to go")

#code to escape the first room
typing2("What do you do?\n")
while True:
  search = input(f"{INPUT_COLOUR}Do you try the door or do you search the room? \nTo try the door type 'DOOR', and to search the room type 'ROOM'.{RESET} ").upper()
  print(' ')
  if search == "ROOM":
    while True:
        #code to explore the first room
        where = input(f"{INPUT_COLOUR}Where in the room do you check? \nThere are 3 spots, there's a pillowcase, there's the vase, and there is behind the curtain. \nTo check the pillowcase type 'PILLOWCASE'. to check the vase type 'VASE', \nand to check behind the curtain type 'CURTAIN'.{RESET} ").upper()
        if where == "CURTAIN":
          typing("Wrong place, try again.\n")
        elif where == "VASE":
          typing("Wrong place, try again.\n")
        elif where == "PILLOWCASE":
          typing("You checked the pillowcase, and you found the key.\n")
          #get bedroom key
          have_bedroom_key = 'true'
          break
        else:
          print("that isn't a valid option")
          #open the door
  elif search == "DOOR":
      typing2("The door won't budge.\n")
      if have_bedroom_key == 'true':
        key_used = input(f"{INPUT_COLOUR}Try the key? \nType 'YES' for yes, or 'NO' for no.{RESET} ").upper()
        if key_used == 'YES':
            typing2("The door opens and you exit the first room.\n")
            break
        elif key_used == 'NO':
            typing("Maybe you should try the key.\n")
        else:
            print("That's not even a option")
  else:
    print("that isn't a valid option")

#enter the hallway
have_kitchen_key = 'false'
typing("You are now in the manor's hallway,\nthere's doors to every room in the mansion, though the door to the dining room is the only open one\n")
while True:
  rooms = input(f"{INPUT_COLOUR}Where do you go, the dining room or the bedroom? {RESET}").upper()

  #go back to the bedroom
  if rooms == "BEDROOM":
      typing2("You go back into the bedroom, you don't find anything there.\n")

#go to dining room

  elif rooms == "DINING ROOM":
      typing2("You explore the dining room and you find a vase.\n")
      vase = input(f"{INPUT_COLOUR}Do you check the vase?{RESET}").upper()
      if vase == "YES":
        while True:
          vase_investigate = input(f"{INPUT_COLOUR}To check under the vase type 'UNDER', \nto check the sides of the inside of the vase type 'SIDES', \nto check the front of the inside of the vase type 'FRONT', \nand to check back of the inside of the vase, type 'BACK'.{RESET}").upper()
          if vase_investigate == "UNDER":
              typing("You check under the vase,\nyou do not find anything there.")
              break
          elif vase_investigate == "SIDES":
              typing("You put your hand inside the vase, and scrape the sides,\nyou don't find anything")
              break
          elif vase_investigate == "FRONT":
              typing("You put your hand into the vase, and you scrape the front of it,\nyou find nothing but some old dirt.")
          elif vase_investigate == "BACK":
              typing("You put your hand into the vase,\nyou feel around the back of the inside of the vase.........\nYou find a key to the kitchen")
              have_kitchen_key = 'true'
      elif vase  == "NO":
        typing("Maybe you should check the vase?\n")


#end the timer and print the time it took for the program to run
end = time.time()
length = end - start
num = length
num1 = num/60
time1 = round(num1, 1)
print("Program ran for", time1, "minutes")

