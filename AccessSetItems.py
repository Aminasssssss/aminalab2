# Access Items.
# You cannot access items in a set by referring to an index or a key.
# Loop through the set, and print the values :
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Check if "banana" is present in the set :
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # True.

# Check if "banana" is NOT present in the set :
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) # False.

# Change Items.
# Once a set is created, you cannot change its items, but you can add new items.