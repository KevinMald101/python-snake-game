# @KevinMald101 Github

# For time stuff
import time
# Loop for if you want to continue looping and repeat for repeating the script
loop, repeat = True, 1
# The counting sheep function, makes a string with how many sheep counted
def count_sheep(num):
  # Result for the final result, sheep for the string, num for amount to count
  result, sheep, num = "", " sheep...", int(num)
  # If num is greater than 0 then run
  if num > 0:
    # Iterate over 1 to the variable "num"
    for num in range(1, num+1):
      # Make the current num a string and add it with the "sheep" variable
      numSheep = str(num) + sheep
      # Add the value of "numSheep" to result
      result += numSheep
    # When finished, print out the result
    print(result)
  # If num is less than 0 than tell the user it can't be less than 0
  else:
    print("No sheep to count and we can't count negative sheep")
# WHile loop to ask user for input
while loop == True:
  # Ask the user for input
  ask = input("How many sheep would you like to count? \n")
  # If the input is a number then load function
  if ask.isnumeric() == True:
    count_sheep(ask)
    # Make ask variable back to nothing and make the script repeatable
    ask, repeat = "", 0
  # If the input is not a number, tell the user, and say it only takes numbers
  else:
    print(f"Your input \"{ask}\" is an invalid input")
    time.sleep(3)
    print("Please type a number")
    time.sleep(2)
  # The repeat loop, both conditions have to be true to run
  while loop == True and repeat == 0:
    # Ask the user if they would like to count again
    ask = input("Would you like to count again? y/n \n")
    # If "y" then repeat script
    if ask.lower() == "y":
      print("Alright then!")
      time.sleep(1)
      break
    # If "n" then close script
    elif ask.lower() == "n":
      print("Goodnight!")
      loop = False
    # If neither 2 options then tell the user and repeat the question
    else:
      print(f"Your input \"{ask}\" is an invalid input")
      time.sleep(2)
      print("Please choose \"y\" for yes and \"n\" for no")
      time.sleep(2)

# @KevinMald101 Github
