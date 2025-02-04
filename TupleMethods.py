# Tuple Methods.

# count() - returns the number of times a specified value occurs in a tuple.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) # 2.

# index() - searches the tuple for a specified value and returns the position of where it was found.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) # 3.