#print original text/backstory
print('You were on a hike in the alps. \n You felt the cold snow beneath your boots, you were doing well but then you slipped, hit your head on the ice, and fell unconscious. \n Now you've woken up here, the bedroom of a strange manor.')

#first room
have_bedroom_key = 'false'
print('You are locked inside an aristocratic bedroom, theres a king size bed with a duvet, and theres two comfy looking cushons, you feel like you could sleep here')
if have_bedroom_key == 'false':
  print('Now, lets find that key')
if have_bedroom_key == 'true':
  print('Alright, it's time to go')
