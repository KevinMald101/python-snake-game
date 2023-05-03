# @KevinMald101 Github

import time
import random

# Play the game
play = True

while play == True:
  # Stuff before the game starts
  location = "the fields"
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
  # In case there's no wolf, add one
  if "wolf" not in game_dictionary.values():
    # The index to where to add the wolf
    ran_num = random.randint(2,num_of_grass)
    grass = "grass" + str(ran_num)
    # Change the value of the grass a wolf
    game_dictionary[grass] = "wolf"

  # When the game starts
  print("As you walk around you farm, you come across some wolf tracks leading toward your hoard of sheep.")
  #time.sleep(5)
  print("You take out your rifle and explore the thick grass.")
  #time.sleep(4)
  all_grass = game_dictionary.keys() # Holds all grass
  all_animals = game_dictionary.values() # Holds all animals
  # Empty list to add the brackets around the grass
  grass_brackets = ""
  # The string to display options
  grass_display = "|"
  # Empty list to add the animals in
  animal_list = []
  # Empty list to add the animals in
  grass_list = []
  # For loop to add the brackets, and add the new string to an existing string
  for grasses in all_grass:
    grass_brackets = " " + grasses + " |"
    grass_display += grass_brackets
    # A list of all the numbered grasses
    grass_list.append(grasses)
  # For loop to add all the animals in a list
  for animals in all_animals:
    animal_list.append(animals)
  # For the while loop
  check_input = True
  while check_input == True:
    # Display location
    print(f"You are currently in {location}")
    # Print all options
    print(f"Where do you search? \n{grass_display}")
    # Ask user for input
    act = input()
    # Valid inputs
    if act.isnumeric() == True:
      # And it's a number in between the amount of grass
      if int(act) in range(1, num_of_grass): # If just the #
        print(animal_list[int(act)])
        break
    elif act in grass_list: # CHeck if it's in the list
      print(animal_list[act])
      break
    else:
      print("Not a valid input")
      #time.sleep(4)
      print("Please type the number or grass(num)\n")
      #time.sleep(4)
  # Ask if they want to play again
  while play == True:
    continue_game = input("Would you like to play again? (y/n)\n").lower()
    if continue_game == "y":
      print("Alright wolf slayer!")
      #time.sleep(4)
      break
    # If "n" then make play false
    elif continue_game == "n":
      play = False
    else:
      print("Not a valid option")

# @KevinMald101 Github