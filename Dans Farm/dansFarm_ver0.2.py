# @KevinMald101 Github

import time
import random

# Play the game
play = True
while play == True:
  # Stuff before the game starts
  # How many grass should there be
  num_of_grass = random.randint(3,10)
  game_dictionary = {}
  for num in range(1, num_of_grass):
    grass = "grass" + str(num)
    # Choosing where the animals are
    pick_animal = random.randint(1,2)
    # If num i one then sheep
    if pick_animal == 1:
      animal = "sheep"
    # Else pick_animal is 2 then make it a wolf
    else:
      animal = "wolf"
    # Check if there's already a wolf
    if "wolf" in game_dictionary.values():
      # If there is then make the animal a sheep since for now only 1 wolf
      animal = "sheep"
    # Add the grass with what's hiding in it to the grass dictionary 
    game_dictionary.update({grass: animal})
    print(game_dictionary)
  # In case there's no wolf, add one
  if "wolf" not in game_dictionary.values():
    # The index to where to add the wolf
    ran_num = random.randint(2,num_of_grass)
    grass = "grass" + str(ran_num)
    # Change the value of the grass a wolf
    game_dictionary[grass] = "wolf"
    print(game_dictionary)

  # When the game starts
  print("As you walk around you farm, you come across some wolf tracks leading toward your hoard of sheep.")
  time.sleep(5)
  print("You take out your rifle and explore the thick grass.")
  time.sleep(4)
  print("Where do you search?")
  # Ask if you want to play again
  while play == True:
    continue_game = input("Would you like to play again? (y/n)\n").lower()
    if continue_game == "y":
      print("Alright wolf slayer!")
      break
    # If n then make play false
    elif continue_game == "n":
      play = False
    else:
      print("Not a valid option")

# @KevinMald101 Github