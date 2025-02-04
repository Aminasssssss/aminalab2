# Set.
# Sets are used to store multiple items in a single variable.
# Create a Set :
thisset = {"apple", "banana", "cherry"}
print(thisset) # {'cherry', 'apple', 'banana'}.

# Set Items.
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable.
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicates Not Allowed.
# Duplicate values will be ignored :
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # {'apple', 'banana', 'cherry'}.

# The values True and 1 are considered the same value in sets, and are treated as duplicates.
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # {True, 2, 'banana', 'cherry', 'apple'}.

# The values False and 0 are considered the same value in sets, and are treated as duplicates.
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) # {False, True, 'apple', 'cherry', 'banana'}.

# Get the Length of a Set.
# Get the number of items in a set :
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # 3.

# Set Items - Data Types.
# String, int and boolean data types :
set1 = {"apple", "banana", "cherry"} # string.
set2 = {1, 5, 7, 9, 3} # int.
set3 = {True, False, False} # boolean.

# A set can contain different data types :
set1 = {"abc", 34, True, 40, "male"} 

# type().
# From Python's perspective, sets are defined as objects with the data type 'set'.
myset = {"apple", "banana", "cherry"}
print(type(myset)) # <class 'set'> .

# The set() Constructor.
# Using the set() constructor to make a set :
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets.
print(thisset) # {'banana', 'apple', 'cherry'}.