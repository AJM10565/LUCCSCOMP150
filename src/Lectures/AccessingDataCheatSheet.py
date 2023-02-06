## Numbers:
"""
In python, we represent number in 2 distinct ways, as Integers and as Floats
"""
# Integers:
"""
Some Examples of Integers:
"""
5
10
51
12
17
# Floats:
"""
Some Examples of floats:
"""
1.1
0.27
12.93
# Numbers store 1 value
"""
While you can access the nth digit of a string or float, because there is no canonical way to do so, your mileage may 
vary, see https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python
"""
## Strings:
"""
In python, strings are groupings of text symbols. Those symbols can include letters, numbers and special characters
"""
str1 = "This little man went to the markey and bought some peppers."
# To get the value of a single letter by index, we use the [] operator
print(str1[0])  # prints 'T'
print(str1[-1])  # prints '.'
# to get more than 1 symbol, use :
print(str1[0:])  # prints: This little man went to the markey and bought some peppers.
print(str1[0::])  # same thing

str2 = str1
print(f"{str2=}")
del str2
# print(f"{str2=}") # NameError: name 'str2' is not defined
"""
We can set new variables to old variables, and we can remove old variables, but we can't modify strings
Strings are immutable

"""
str3 = "fly away"
print(str3)
# We're re-assigning to a variable
str3 = "flow down"
print(str3)

# but here:
str4 = "fly away"
# This is bad: >>> str4[0] = "m"
# TypeError: 'str' object does not support item assignment
"""
Tuples: tuples are a data structure that is immutable
"""
tuple0 = (-1, 2, 4, 5)
tuple1 = 1, 2, 3
tuple2 = 1, "a", "car", 1.23

# when you make a tuple, all you need are things, separated by commas
# you can wrap the items in "(" and ")" if you want to be more explicit about what you are creating
tuple4 = (-1, 0, 1)
print(tuple4[0])  # prints -1
print(tuple4[-1])  # prints 1
"""
tuples are also immutable! no changing the order or the items is allowed
"""
tuple5 = 0, 1, 2, 3, 4
# Don't do this: >>>tuple5[2] = 17 # TypeError: 'tuple' object does not support item assignment
"""

"""
