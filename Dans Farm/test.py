import random
# How many grass should there be
num_of_grass = random.randint(2,4)
game_dictionary = {}
for num in range(1, num_of_grass):
  grass = "grass" + str(num)
  # Choosing where the animals are
  pick_animal = random.randint(1,4)
  # If num i one then sheep
  if pick_animal == 1 or pick_animal == 2 or pick_animal == 3:
    animal = "sheep"
  # Else pick_animal is 2 and make it a wolf
  else:
    animal = "wolf"
  # Check if there's already a wolf
  if "wolf" in game_dictionary.values():
    animal = "sheep"

  game_dictionary.update({grass: animal})
  print(game_dictionary)   
  # In case there's no wolf, add one
if "wolf" not in game_dictionary.values():
  ran_num = random.randint(2,num_of_grass)
  grass = "grass" + str(ran_num)
  game_dictionary[grass] = "wolf"
  print(game_dictionary)