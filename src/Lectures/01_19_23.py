"""
Goals for this lecture:
1. Review Quiz Results
2. Review New material:
    - Basics of conditionals
    - while loops
    - working inside functions for homework and labs
3. Labs
    - Boolean Tables Lab
    - current day lab
    - atm lab
    - calculate shipping lab
"""


# print("Quiz 1 review")
# print("If you're not sure, try it out")
# print("What is the result of the expression 6/8 in Python?")
# print(f"{6/8=}")
# print("What does the function max(5, 11, 2) return?")
# # print(f"{max(5, 11, 2)=}")
# print("Similarly")
# print(f"{int('125')}")
# print(f"{int(len([2, 4, 6]))}")
# print("What symbol does Python use to find the remainder of a division?")
# print(f"{5/2=}")
# print(f"{5//2=}")
# print(f"{5%2=}")
# print('What is the output of the following code: x = 3 y = 5 z=f"{x} + {y} = {x + y}" print(z)')
# x = 3
# y = 5
# z=f"{x} + {y} = {x + y}"
# print(z)

# Basic of conditionals
# Python has 3 kinds of conditional statements: if, elif, and else
# print("Example 1: if ")
# value = 3
# print(f"{value=}")
# if value > 2:
#     print(f"value is greater than 2")


# print("Example 2: else")
# value = 1
# print(f"{value=}")
# if value > 2:
#     print(f"value is greater than 2")
# else:
#     print(f"value is less than or equal to 2")

# print("Example 3: elif")
# value = 2
# print(f"{value=}")
# if value > 2:
#     print(f"value is greater than 2")
# elif value == 2:
#     print(f"value is equal to 2")
# else:
#     print(f"value is less than 2")


# def some_new_function():
#     print("did a thing")

# some_new_function()

# # print(f"{type(some_new_function)=}")
# # print(f"{type(some_new_function())=}")

# def went_to_a_store_with(person_name):
#     """
#     prints: I went to a store with a person called {value}
#     """
#     print(f"I went to a store with a person called {person_name}")

# went_to_a_store_with("Sam")
# went_to_a_store_with("Sara")

def returns_a_value(a, b):
    """
    Some functions returns stuff
    """
    return a + b


what_is_this = returns_a_value(4, 5)
# print("what is this: ", what_is_this)
# print("what is this: " + what_is_this)

# #talk about type annotations in python

# def while_loop_example(value: int):
#     """
#     >, < >=, <=, ==, !=
#     print a value, then reduce it by 1, stop when you hit 0, return the value
#     """
#     while value != 0:
#         print(value)
#         value = value -1
#     return value

# while_loop_example(4)


# def while_loop_example_with_guard_condition(value: int):
#     """
#     print a value, then reduce it by 1, stop when you hit 12, return the value
#     """
#     keep_running = True
#     if value <=12:
#         value = value + 12
#     while value != 0:
#         if value == 12:
#             keep_running = False
#             print("Termination condition reached, exiting loop")
#         else:
#             print(value)
#             value = value -1
#     return value

number = 1
print(number)
print(f"{type(number)=}")
number = "two"
print(number)
print(f"{type(number)=}")
number = ["1"]
print(number)
print(f"{type(number)=}")

result = input("Tell me a decimal number: ")

print(f"5 times your number is: {5 * float(result)}")
