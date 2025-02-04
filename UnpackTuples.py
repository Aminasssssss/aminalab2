# Unpacking a Tuple.
# Packing a tuple :
fruits = ("apple", "banana", "cherry") 

# Unpacking a tuple :
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) # apple.
print(yellow) # banana.
print(red) # cherry.

# Using Asterisk*.
# Assign the rest of the values as a list called "red" :
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) # apple.
print(yellow) # banana.
print(red) # ['cherry', 'strawberry', 'raspberry'].

# Add a list of values the "tropic" variable :
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) # apple.
print(tropic) # ['mango', 'papaya', 'pineapple'].
print(red) # cherry.# Unpacking a Tuple.
# Packing a tuple :
fruits = ("apple", "banana", "cherry") 

# Unpacking a tuple :
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) # apple.
print(yellow) # banana.
print(red) # cherry.

# Using Asterisk*.
# Assign the rest of the values as a list called "red" :
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) # apple.
print(yellow) # banana.
print(red) # ['cherry', 'strawberry', 'raspberry'].

# Add a list of values the "tropic" variable :
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) # apple.
print(tropic) # ['mango', 'papaya', 'pineapple'].
print(red) # cherry.