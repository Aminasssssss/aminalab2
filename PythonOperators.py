# Operators are used to perform operations on variables and values.
print(10 + 5) # 15.

# Arithmetic Operators.
x = 5
y = 3
# Addition.
print(x + y) # 8.
# Substraction.
print (x - y) # 2.
# Multiplication.
print(x * y) # 15.
# Division.
print(x / y) # 1.6666666666666667.
# Modulus.
print(x % y) # 2.
# Exponentiation.
print(x ** y) # 125.
# Floor division.
print(x // y) # 1.

# Assignment Operators.
# += :
x = 5
x += 3 # same as x = x + 3.
print(x) # 8.
# -= :
x = 5
x -= 3 # same as x = x - 3.
print(x) # 2.
# *= :
x = 5
x *= 3 # same as x = x * 3.
print(x) # 15.
# /= :
x = 5
x /= 3 # same as x = x / 3.
print(x) # 1.6666666666666667.
# %= :
x = 5
x %= 3 # same as x = x % 3.
print(x) # 2.
# //= :
x = 5
x //= 3 # same as x = x // 3.
print(x) # 1.
# **= :
x = 5
x **= 3 # same as x = x ** 3.
print(x) # 125.

# Comparison Operators.
x == y # equal.
x != y # not equal.
x > y # greater than.
x < y # less than.
x >= y # greater than or equal to.
x <= y # less than or equal to.

# Logical Operators.
x = 5
# and - returns True if both statements are true.
print(x > 3 and x < 10) # returns True because 5 is greater than 3 and 5 is less than 10.
# or - returns True if one of the statements is true.
print(x > 3 or x < 4) # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4).
# not - reverse the result, returns False if the result is true.
print(not(x > 3 and x < 10)) # returns False because not is used to reverse the result.

# Identity Operators.
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
# is - returns True if both variables are the same object.
print(x is z) # returns True because z is the same object as x.
print(x is y) # returns False because x is not the same object as y, even if they have the same content.
print(x == y) # to demonstrate the difference betweeen "is" and "==" : this comparison returns True because x is equal to y.
# is not - returns True if both variables are not the same object.
print(x is not z) # returns False because z is the same object as x.
print(x is not y) # returns True because x is not the same object as y, even if they have the same content.
print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y.

# Membership Operators.
x = ["apple", "banana"]
# in - returns True if a sequence with the specified value is present in the object.
print("banana" in x) # returns True because a sequence with the value "banana" is in the list.
# not in - returns True if a sequence with the specified value is not present in the object.
print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list.

# Bitwise Operators.

# 6 = 0000000000000110.
# 3 = 0000000000000011.

# &, and - sets each bit to 1 if both bits are 1.
print(6 & 3) # 2.
# 2 = 0000000000000010.

# |, or - sets each bit to 1 if one of two bits is 1.
print(6 | 3) # 7.
# 7 = 000000000000011.

# ^, xor - sets each bit to 1 if only one of two bits is 1.
print(6 ^ 3) # 5.
# 5 = 0000000000000101.

# ~, not - inverts all the bits.
print(~3) # -4.
# -4 = 1111111111111100.

# <<, zero fill left shift - shift left by pushing zeros in from the right and let the leftmost bits fall off.
print(3 << 2) # 12.
# 12 = 0000000000001100.

# >>, signed right shift - shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off.
print(3 >> 2) # 0.
# 0 = 0000000000000000.

# Operator Precedence.
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first.
print((6 + 3) - (6 + 3)) # 0.
# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions.
print(100 + 5 * 3) # 115.
# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right.
print(5 + 4 - 7 + 3) # 5.