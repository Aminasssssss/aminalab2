# Set Methods.

# add() - adds an element to the set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) # {'banana', 'cherry', 'orange', 'apple'}.

# clear() - removes all the elements from the set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits) # set().

# copy() - returns a copy of the set.
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x) # {'apple', 'banana', 'cherry'}.

# difference() - returns a set containing the difference between two or more sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z) # {'banana', 'cherry'}.

# difference_update() - removes the items in this set that are also included in another, specified set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x) # {'cherry', 'banana'}.

# discard() - remove the specified item.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) # {'apple', 'cherry'}.

# intersection() - returns a set, that is the intersection of two other sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) # {'apple'}.

# intersection_update() - removes the items in this set that are not present in other, specified set(s).
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) # {'apple'}.

# isdisjoint() - returns whether two sets have a intersection or not.
# Return True if no items in set x is present in set y :
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z) # True.

# issubset() - returns whether another set contains this set or not.
# Return True if all items in set x are present in set y :
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z) # True.

# issuperset() - returns whether this set contains another set or not.
# Return True if all items set y are present in set x :
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) # True.

# pop() - removes an element from the set.
# Remove a random item from the set :
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# remove() - removes the specified element.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # {'cherry', 'apple'}.

# symmetric_difference() - returns a set with the symmetric differences of two sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) # {'microsoft', 'cherry', 'google', 'banana'}.

# union() - return a set containing the union of sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z) # {'banana', 'apple', 'cherry', 'google', 'microsoft'}.

# update() - update the set with the union of this set and others.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x) # {'cherry', 'apple', 'banana', 'microsoft', 'google'}.