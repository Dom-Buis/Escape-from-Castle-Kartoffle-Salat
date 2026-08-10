##import things
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
typing("You were on a hike in the alps. \n You felt the cold snow beneath your boots, you were doing well on the hike, but then you slipped and hit your head on the ice, and you fell unconscious. \n Now you've woken up here, in the bedroom of a strange manor.")
print()

#first room
have_bedroom_key = 'false'
typing2("You are locked inside an aristocratic bedroom.\nthere's a king size bed next to you with a duvet on it.\nand theres two comfy looking cushions.\nyou feel like you could sleep here...\n ")
def bedroom_key():
  if have_bedroom_key == 'false':
    typing2("'Now, lets find that key'")
  if have_bedroom_key == 'true':
    typing2("Alright, it's time to go")

#code to escape the first room
typing2("What do you do?\n")
while True:
  search = input(f"{INPUT_COLOUR}Do you try the door or do you search the room?{RESET} ").upper()
  if search == "SEARCH THE ROOM":
    while True:
        #code to explore the first room
        where = input(f"{INPUT_COLOUR}Where in the room do you check? There are 3 spots, there's a pillowcase, there's the vase, and there is behind the curtain.{RESET} ").upper()
        if where == "BEHIND THE CURTAIN":
          typing("Wrong place, try again.\n")
        elif where == "THE VASE":
          typing("Wrong place, try again.\n")
        elif where == "A PILLOWCASE":
          typing("You checked the pillowcase, and you found the key\n")
          #get bedroom key
          have_bedroom_key = 'true'
          break
        else:
          print("that isn't a valid option")
          #open the door
  elif search == "TRY THE DOOR":
      typing2("The door won't budge.\n")
      if have_bedroom_key == 'true':
        key_used = input(f"{INPUT_COLOUR}Try the key?{RESET} ").upper()
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
typing("You are now in the manor's hallway, there's doors to every room in the mansion, though the door to the dining room is the only open one\n")
while True:
  rooms = input(f"{INPUT_COLOUR}Where do you go, the dining room or  the bedroom?{RESET}").upper()

  #go back to the bedroom
  if rooms == "BEDROOM":
      typing2("You go back into the bedroom, you don't find anything there.\n")

#go to dining room
  elif rooms == "DINING ROOM":
      typing2("You explore the dining room and you find a vase.\n")

#end the timer and print the time it took for the program to run
end = time.time()
length = end - start
num = length
num1 = num/60
time1 = round(num1, 1)
print("Program ran for", time1, "minutes")
