# compare two values.
print(10 > 9) # True.
print(10 == 9) # False.
print(10 < 9) # False.

# condition in an if statement.
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate values and variables.
print(bool("Hello")) # True.
print(bool(15)) # True.

x = "Hello"
y = 15
print(bool(x)) # True.
print(bool(y)) # True.

# Any string is True, except empty strings.
# Any number is True, except 0. 
# Any list, tuple, set, and dictionary are True, except empty ones.
bool("abc") # True.
bool(123) # True.
bool(["apple", "cherry", "banana"]) # True.

# Some values are false.
bool(False) # False.
bool(None) # False.
bool(0) # False.
bool("") # False.
bool(()) # False.
bool([]) # False.
bool({}) # False.

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) # False.

# Functions can return a boolean.
def myFunction() :
  return True
print(myFunction()) # True.

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!") # YES!

# built-in isinstance() function.
x = 200
print(isinstance(x, int)) # True.