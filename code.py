#print original text/backstory
print("You were on a hike in the alps. \n You felt the cold snow beneath your boots, you were doing well on the hike, but then you slipped and hit your head on the ice, and you fell unconscious. \n Now you've woken up here, in the bedroom of a strange manor.")

#first room
have_bedroom_key = 'false'
print("You are locked inside an aristocratic bedroom, there's a king size bed next to you with a duvet on it, and theres two comfy looking cushions, you feel like you could sleep here. ")
if have_bedroom_key == 'false':
  print("Now, lets find that key")
if have_bedroom_key == 'true':
  print("Alright, it's time to go")
