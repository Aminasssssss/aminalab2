# List Comprehension.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) # ['apple', 'banana', 'mango'].

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango'].

# The Syntax.
# newlist = [expression for item in iterable if condition == True].
# The return value is a new list, leaving the old list unchanged.

# Condition.
# The condition is like a filter that only accepts the items that evaluate to True.
# Only accept items that are not "apple" :
newlist = [x for x in fruits if x != "apple"]

# With no if statement :
newlist = [x for x in fruits]

# Iterable.
# The iterable can be any iterable object, like a list, tuple, set etc.
# range() function to create an iterable :
newlist = [x for x in range(10)]

# Accept only numbers lower than 5 :
newlist = [x for x in range(10) if x < 5]

# Expression.
# Set the values in the new list to upper case :
newlist = [x.upper() for x in fruits]

# Set all values in the new list to 'hello' :
newlist = ['hello' for x in fruits]

# Return "orange" instead of "banana" :
newlist = [x if x != "banana" else "orange" for x in fruits]