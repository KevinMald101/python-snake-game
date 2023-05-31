# @KevinMald101 Github
import time
import random
import termcolor
# Play the game
play = True

while play == True:
  # Stuff before the game starts
  location = termcolor.colored('the fields', 'green')
  # How many grass should there be
  num_of_grass = random.randint(4,8)
  game_dictionary = {}
  for num in range(1, num_of_grass):
    grass = "grass" + str(num)
    # Choosing where the animals are
    pick_animal = random.randint(1,5)
    # If num is one, then sheep
    if pick_animal >= 3:
      animal = 'sheep'
    # Else pick_animal is 2 then make it a wolf
    else:
      animal = 'wolf'
    # Check if there's already a wolf
    if "wolf" in game_dictionary.values():
      # If there is then make the animal a sheep
      # Since i only want one wolf right now
      animal = 'sheep'
    # Add the grass with what's hiding in it to the grass dictionary 
    game_dictionary.update({grass: animal})
  # Variables of the colored animals
  wolf = termcolor.colored('wolf', 'red')
  sheep = termcolor.colored('sheep', 'blue')
  # In case there's no wolf, add one
  # Only have this since the termcolor changes the string value
  if "wolf" not in game_dictionary.values():
    # The index to where to add the wolf
    ran_num = random.randint(2,num_of_grass)
    grass = "grass" + str(ran_num)
    # Change the value of the grass a wolf
    game_dictionary[grass] = wolf
  # Makes all the animals to their color
  count_grass_position = 1 # Very long variable name
  for animals in game_dictionary.values():
    if animals == 'sheep':
      grass = "grass" + str(count_grass_position)
      game_dictionary[grass] = sheep
      count_grass_position += 1
    else:
      grass = "grass" + str(count_grass_position)
      game_dictionary[grass] = wolf
      count_grass_position += 1
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
    if act.isnumeric() == True and int(act) in range(1, num_of_grass):
      # And it's a number in between the amount of grass
      act_but_in_int = int(act)
      act_but_in_int -= 1 # So it can reach all the way
      time.sleep(1)
      print(f"You spot a {animal_list[act_but_in_int]}")
      time.sleep(1)
    elif act in grass_list: # Check if it's in the list, grass[num]
      time.sleep(1)
      print(f"You spot a {game_dictionary[act]}")
      time.sleep(1)
    # I CAN MAKE A FUNCTION FOR ACTING
    else:
      print("Not a valid input")
      time.sleep(3)
      print("Please type the number or grass(num)\n")
      time.sleep(3)
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