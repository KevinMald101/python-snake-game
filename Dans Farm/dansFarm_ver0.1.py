# @KevinMald101 Github

def warn_the_sheep(queue):
  # Reverse the list. The wolf will attack the sheep to it's right
  queue.reverse()
  # Mark where the wolf is
  wolf = queue.index('wolf')
  # If the wolf is at where you are at (end of the list)
  if wolf == 0:
    # Tell the wolf to go away
    print ("Pls go away and stop eating my sheep")
  # If the wolf isn't in front of you
  else:
    # Sheep in front of the wolf
    vulnerable_sheep = wolf
    print(f"Oi! Sheep number {vulnerable_sheep}! You are about to be eaten by a wolf!")
# Test
warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep'])
warn_the_sheep(['wolf', 'sheep', 'sheep'])
warn_the_sheep(['sheep', 'sheep', 'wolf', 'sheep', 'sheep', 'sheep'])
warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf'])
warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep'])
warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep'])

# @KevinMald101 Github