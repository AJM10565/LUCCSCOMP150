"""
Agenda:
- Review Homework #1 Solutions
- Review Quiz #2 Solutions
- Introduce the Research paper
- For loops (for-in loops and for in range loops)
simple data structures:
strings: "This is a string"
lists: ["this","is","a","list"]
dictionaries: {"Key":"Value"}
"""
# Homework 1 Solutions
# for index in my_fun_list:
#     print(index)

# for number in my_fun_list:
#     print(number)

# for index in range(len(my_fun_list)):
#     print(my_fun_list[index])

if __name__ == "__main__":

    my_fun_list = [1, 2, 3, 4, 5, 7, 6, 5, 4, 3, 2, 1]

    index = 0

    # while index < len(my_fun_list):
    #     print(f"{index=}")
    #     print(f"{my_fun_list[index]}")
    #     index = index + 1
    while index < len(my_fun_list):
        print(f"{index+1=}")
        print(f"{index < len(my_fun_list)=}")

        print(f"{my_fun_list[index]}")
        index = index + 1

