# @KevinMald101 Github

# The Collatz conjecture is one of the most famous unsolved problems in 
# mathematics. The conjecture asks whether repeating two simple arithmetic 
# operations will eventually transform every positive integer into 1.
def collatz(n):
  # Make a list with the current number
  list = [n]
  # While n is not 1
  while n != 1:
    # Check if the number is even or odd
    if n % 2 == 0:
      # If even then divide by two
      n //= 2
      # And add it to the end of the list
      list.append(n)
    # If odd then multiply by 3 and add one
    else:
      n *= 3
      n += 1
      # Then add to the end of the list
      list.append(n)
  # After "n" is one then print out the list
  print(list) 
# Test
collatz(130)
collatz(20)
collatz(34)
collatz(3)
collatz(58)
collatz(37)
collatz(100)

# @KevinMald101 Github