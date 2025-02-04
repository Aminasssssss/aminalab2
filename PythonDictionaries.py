# Dictionary.
# Dictionaries are used to store data values in key:value pairs.
# Create and print a dictionary :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}.

# Dictionary Items.
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# Print the "brand" value of the dictionary :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) # Ford.

# Changeable.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed.
# Dictionaries cannot have two items with the same key :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}.

# Dictionary Length.
# To determine how many items a dictionary has, use the len() function.
# Print the number of items in the dictionary :
print(len(thisdict)) # 3.

# Dictionary Items - Data Types.
# The values in dictionary items can be of any data type.
# String, int, boolean, and list data types :
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# type().
# From Python's perspective, dictionaries are defined as objects with the data type 'dict'.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) # <class 'dict'> .

# The dict() Constructor.
# Using the dict() method to make a dictionary :
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) # {'name': 'John', 'age': 36, 'country': 'Norway'}.