# Access Items.
# List items are indexed and you can access them by referring to the index number.
# Print the second item of the list :
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana.

# Negative Indexing.
# Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the list :
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # cherry.

# Range of Indexes.
# Return the third, fourth, and fifth item :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi'].
# The search will start at index 2 (included) and end at index 5 (not included).

# Return the items from the beginning to, but NOT including, "kiwi" :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange'].

# Return the items from "cherry" to the end :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango'].

# Range of Negative Indexes.
# Return the items from "orange" (-4) to, but NOT including "mango" (-1) :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon'].

# Check if Item Exists.
# Check if "apple" is present in the list :
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")