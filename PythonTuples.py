# Tuple.
# Tuples are used to store multiple items in a single variable.
# Create a Tuple :
thistuple = ("apple", "banana", "cherry")
print(thistuple) # ('apple', 'banana', 'cherry').

# Tuple Items.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates.
# Since tuples are indexed, they can have items with the same value.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # ('apple', 'banana', 'cherry', 'apple', 'cherry').

# Tuple Length.
# To determine how many items a tuple has, use the len() function.
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # 3.

# Create Tuple With One Item.
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple)) # <class 'tuple'> .
thistuple = ("apple")
print(type(thistuple)) # <class 'str'> .

# Tuple Items - Data Types.
# String, int and boolean data types :
tuple1 = ("apple", "banana", "cherry") # string.
tuple2 = (1, 5, 7, 9, 3) # int.
tuple3 = (True, False, False) # boolean.

# A tuple can contain different data types :
tuple1 = ("abc", 34, True, 40, "male")

# type().
# From Python's perspective, tuples are defined as objects with the data type 'tuple'.
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # <class 'tuple'> .

# The tuple() Constructor.
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) # ('apple', 'banana', 'cherry').