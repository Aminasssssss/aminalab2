# Remove Item.
# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method :
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # {'apple', 'cherry'}.
# If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method :
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # {'cherry', 'apple'}.
# If the item to remove does not exist, discard() will NOT raise an error.

# We can also use the pop() method to remove an item, but this method will remove a random item, so we cannot be sure what item that gets removed.
# Remove a random item by using the pop() method :
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # cherry / banana / apple.
print(thisset) # {'apple', 'banana'} / {'apple', 'cherry'} / {'cherry', 'banana'}.

# The clear() method empties the set :
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set().

# The del keyword will delete the set completely :
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)