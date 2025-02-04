# Python For Loops.
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# Print each fruit in a fruit list :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String.
# Even strings are iterable objects, they contain a sequence of characters.
# Loop through the letters in the word "banana" :
for x in "banana":
  print(x)

# The break Statement.
# With the break statement we can stop the loop before it has looped through all the items.
# Exit the loop when x is "banana" :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# Exit the loop when x is "banana", but this time the break comes before the print :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue Statement.
# With the continue statement we can stop the current iteration of the loop, and continue with the next.
# Do not print banana :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() Function.
# Using the range() function :
for x in range(6): # range(6) is not the values of 0 to 6, but the values 0 to 5.
  print(x)

# Using the start parameter :
for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1) :
for x in range(2, 30, 3):
  print(x)

# Else in For Loop.
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
# Print all numbers from 0 to 5, and print a message when the loop has ended :
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Nested Loops.
# Print each adjective for every fruit :
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement.
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error :
for x in [0, 1, 2]:
  pass