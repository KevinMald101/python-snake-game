import termcolor
# Color of the locations
location = termcolor.colored('the fields','green')
print(f"Only the location should be colored {location}")
# Color of Dans enemies
dans_enemies = termcolor.colored('the enemies','red')
print(f"Only the enemies should be colored {dans_enemies}")
# Color of Dans money
money = termcolor.colored('$100','yellow')
print(f"Only the coins should be colored {money}")
# Color of Dans animals
animal = termcolor.colored('sheep','blue')
print(f"Only the animals should be colored {animal}")