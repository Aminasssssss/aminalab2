# Change Tuple Values.
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Convert the tuple into a list to be able to change it :
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) # ('apple', 'kiwi', 'cherry').

# Add Items.
# Convert the tuple into a list, add "orange", and convert it back into a tuple :
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) 
print(thistuple) # ('apple', 'banana', 'cherry', 'orange').

# Create a new tuple with the value "orange", and add that tuple :
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) # ('apple', 'banana', 'cherry', 'orange').

# Remove Items.
# Tuples are unchangeable, so you cannot remove items from it.
# Convert the tuple into a list, remove "apple", and convert it back into a tuple :
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) # ('banana', 'cherry').

# The del keyword can delete the tuple completely :
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # this will raise an error because the tuple no longer exists.