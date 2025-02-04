# Access Tuple Items.
# Print the second item in the tuple :
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # banana.

# Negative Indexing.
# Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the tuple :
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # cherry.

# Range of Indexes.
# Return the third, fourth, and fifth item :
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # ('cherry', 'orange', 'kiwi').

# Return the items from the beginning to, but NOT included, "kiwi" :
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # ('apple', 'banana', 'cherry', 'orange').

# Return the items from "cherry" and to the end :
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # ('cherry', 'orange', 'kiwi', 'melon', 'mango').

# Range of Negative Indexes.
# Return the items from index -4 (included) to index -1 (excluded) :
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # ('orange', 'kiwi', 'melon').

# Check if Item Exists.
# Check if "apple" is present in the tuple :
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") # Yes, 'apple' is in the fruits tuple.