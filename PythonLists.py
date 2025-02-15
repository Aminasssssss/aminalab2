# List.
# lists are used to store multiple items in a single variable.
# create a List :
thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Items.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates.
# Since lists are indexed, lists can have items with the same value.
# Lists allow duplicate values :
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length.
# To determine how many items a list has, use the len() function.
# Print the number of items in the list :
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3.

# List Items - Data Types.
# List items can be of any data type.
# String, int and boolean data types :
list1 = ["apple", "banana", "cherry"] # string.
list2 = [1, 5, 7, 9, 3] # int.
list3 = [True, False, False] # boolean.
# A list can contain different data types :
list1 = ["abc", 34, True, 40, "male"]

# type().
# From Python's perspective, lists are defined as objects with the data type 'list'.
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'> .

# The list() Constructor.
# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets.
print(thislist)

# Python Collections (arrays).
# list - is a collection which is ordered and changeable. Allows duplicate members.
# tuple -  is a collection which is ordered and unchangeable. Allows duplicate members.
# set -  is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# dictionary - is a collection which is ordered and changeable. No duplicate members.