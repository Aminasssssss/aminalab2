# Sort List Alphanumerically.
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default.

# Sort the list alphabetically :
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple'].

# Sort the list numerically :
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100].

# Sort Descending.
# To sort descending, use the keyword argument reverse = True.
# Sort the list descending :
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana'].

# Sort the list descending :
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23].

# Customize Sort Function.
# The function will return a number that will be used to sort the list (the lowest number first).
# Sort the list based on how close the number is to 50 :
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # [50, 65, 23, 82, 100].

# Case Insensitive Sort.
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
# Case sensitive sorting can give an unexpected result :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry'].

# Perform a case-insensitive sort of the list :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange'].

# Reverse Order.
# The reverse() method reverses the current sorting order of the elements.
# Reverse the order of the list items :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana'].