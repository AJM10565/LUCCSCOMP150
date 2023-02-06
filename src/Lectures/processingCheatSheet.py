"""
Processing data python cheat sheet (cook book)
"""


# Problem: Iterate over the items in a sequence
# Solution: use a for loop
# Example: sum of list members
def add_together_list_membersV1(sequence):
    sum_of_sequence_members = 0
    for number in sequence:
        sum_of_sequence_members += number
    return sum_of_sequence_members


# Solution, use a python built-in
def add_together_list_membersV2(sequence):
    return sum(sequence)


"""
Which is better? In our case, sum() is a python specific function, so its usefulness doesn't translate to working in 
other languages. Additionally, we must trust that sum is doing what we want it to. Also, without being able to write out
the solution ourselves, we can't improve as programmers and more generally as problem solvers.
"""


# Problem: receive input from console until the user is finished then print it all back
# solution, use while loop

def receive_input_until_done():
    def check_if_send_more():
        response = input(f"Is there more you want to send (Y/N)")
        if response == "Y":
            return True
        else:
            return False

    sending_finished = False
    total = []
    while sending_finished:
        total.append(input(f"what do you want to add? "))
        sending_finished = not check_if_send_more()
    print(total)
