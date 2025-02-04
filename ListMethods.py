# List Methods.

# append() - adds an element at the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# clear() - removes all the elements from the list.
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

# copy() - returns a copy of the list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy() 

# count() - Returns the number of elements with the specified value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry") 

# extend() - add the elements of a list (or any iterable), to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

# index() - returns the index of the first element with the specified value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

# insert() - adds an element at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

# pop() - removes the element at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

# remove() - removes the item with the specified value.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

# reverse() - reverses the order of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

# sort() - sorts the list.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()