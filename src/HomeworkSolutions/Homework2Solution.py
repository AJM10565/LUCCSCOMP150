"""
Homework #2 Instructions:
Submit final solution on sakai. Use this file as a template, rename according to the class convention: UVIDHomework2.py
To the best of your ability complete problems 1,2,3,4, and 5. If you use a resource, be sure to leave a link inside the
function documentation for that problem.
"""


def problem1(number: int) -> str:
    """
    Problem:

    Write a Python function that takes an integer returns a string that represents the number with its ordinal
    suffix. The ordinal suffix should be one of 'st', 'nd', 'rd', or 'th', depending on the input number. The program
    should be able to handle input numbers within 1 to 100.

    Examples:

    Input: 1, Output: "1st"
    Input: 2, Output: "2nd"
    Input: 3, Output: "3rd"
    Input: 4, Output: "4th"
    Input: 11, Output: "11th"
    Input: 12, Output: "12th"
    Input: 21, Output: "21st"
    Input: 22, Output: "22nd"
    Constraints:

    The input number will be a positive integer and will be between 1 and 100.
    Note:

    For full credit, you must use a dictionary to store the suffixes and use it to determine the suffix based on the
    input number. Test your program with different inputs to make sure it's working correctly.
    """

    if 10 < number % 100 < 20:
        return str(number) + 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
        return str(number) + suffix


def problem2(number: int) -> list:
    """
    Problem:

    Write a Python function that generates the Fibonacci sequence of a given length. The program should ask the user for
    the number of Fibonacci numbers to generate, and then generate and print the sequence. Your program should utilize
    functions and/or a dictionary to make the solution more reusable and readable.

    Examples:

    Input: 5, Output: [1, 1, 2, 3, 5]
    Input: 8, Output: [1, 1, 2, 3, 5, 8, 13, 21]
    Constraints:

    The input number will be a positive integer.

    Hint:
    The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous
    two numbers in the sequence.
    The sequence starts with 1, 1
    You can use a loop or recursion to generate the sequence. You can create a function that takes an argument as
    the number of Fibonacci numbers to generate and returns the sequence.
    You can also create a function that takes two arguments, current and previous, and returns the next number
    in the sequence.
    """
    # Without recursion
    if number == 0:
        return []
    elif number == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, number):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


def problem3(user_input_to_be_validated, validation_type) -> bool:
    """
    Many times, when we create functions, we're exposing ourselves to accept user input, and we assume the input is ok,
    but now we will write an input validator function to verify that the input "makes sense."
    Create a function in Python that takes 2 parameters:
    user_input_to_be_validated and validation_type
    and verifies that user_input_to_be_validated  is a valid value according to the criteria of validation_type.

    Functionality:

    1. if validation_type is a dictionary{} and the key of the dictionary is an
        a. integer then the values will be a list with length 2, and you should verify that the first parameter is an
         integer between the two numbers in the list
        problem3(4,{"integer":[1,5]})
         b. string, then the values will be a list of length 1 or greater, and you should verify that the first
         parameter can be found in the list of values
         problem3("rock",{"string":["rock","paper","scissors"]})

    2. if validation_type of "email" should check if string can be an email (contains @ symbol and ends with
    .com or .edu or .net or .gov or .org)
    3. if validation_type of "phone_number" should check if the string could be a phone number, a phone number has 3
    digits, then a single '-', then 3 more digits, then another '-' then 4 digits


    Examples:

    problem3("abc", validation_type: ["abc","123","do re mi"]) => True
    problem3("da rey me", validation_type: ["abc","123","do re mi"]) => False
    problem3("123", {"integer":[1,1000]}) => True
    problem3("(123)-456-7891", "phone_number") => False
    problem3("amiller17@luc.edu", validation_type: "email") => True

    Note: This homework assignment should not be asking the user for input using the input() function.
    """
    if type(validation_type) == dict:
        key = list(validation_type.keys())[0]
        values = validation_type[key]
        if key == 'integer':
            if type(user_input_to_be_validated) == int:
                return values[0] <= user_input_to_be_validated <= values[1]
            else:
                return False
        elif key == 'string':
            return user_input_to_be_validated in values
    elif validation_type == 'email':
        at_symbol = user_input_to_be_validated.find('@')
        if at_symbol == -1:
            return False
        domains = ['.com', '.edu', '.net', '.gov', '.org']
        for domain in domains:
            if user_input_to_be_validated.endswith(domain):
                return True
        return False
    elif validation_type == 'phone_number':
        parts = user_input_to_be_validated.split('-')
        if len(parts) != 3:
            return False
        if len(parts[0]) != 3 or len(parts[1]) != 3 or len(parts[2]) != 4:
            return False
        for part in parts:
            for character in part:
                if not character.isdigit():
                    return False
        return True
    return False


def problem4(coordinates: str) -> str:
    """
    Problem:

    Write a Python function that takes the coordinates of a square on a chessboard as input (e.g. "A1", "D5") and
    returns the color of the square (either "black" or "white"). The chessboard is a 8x8 grid, where the rows are
    numbered 1 to 8 and the columns are labeled "A" to "H". The program should be able to handle any valid input
    coordinates within the chessboard.

    Functionality:

    Accept a string as input representing the coordinates of a square on a chessboard (e.g. "A1", "D5")
    Determine the color of the square at the given coordinates (black or white)
    Return the color of the square as a string
    Examples:

    Input: "A1", Output: "black"
    Input: "B2", Output: "white"
    Input: "H8", Output: "black"
    Input: "D5", Output: "black"
    Constraints:

    The input will be a string in the format of a letter (A-H) followed by a number (1-8)
    The program should be able to handle any valid input coordinates within the chessboard.
    """

    column_index = ord(coordinates[0].upper())
    row_index = int(coordinates[1]) - 1
    if (column_index + row_index) % 2 == 0:
        return 'black'
    else:
        return 'white'


def problem5():
    """
    Problem:

    Create a Tic-Tac-Toe game in Python where two players can play against each other. The game should be played on a
    3x3 grid, where the players take turns to place their symbol (X or O) on the grid. The player who succeeds in
    placing three of their symbols in a horizontal, vertical or diagonal row wins the game. The game should be able
    to detect a win or a draw and display the result on the screen.

    Functionality:

    Display an empty 3x3 grid on the screen:
    _|_|_    _|_|_
    _|_|_ => _|X|_
    _|_|_    _|_|_


    Allow player 1 to place their symbol (X) on the grid
    Allow player 2 to place their symbol (O) on the grid
    Check for a win or a draw after each turn
    Display the result on the screen
    Constraints:

    The game should be played on a 3x3 grid.
    The players should be able to input the row and column where they want to place their symbol.
    The game should detect a win or a draw and display the result on the screen.
    The game should ask the players if they want to play again after the game is over.
    Note:

    You can use the above problem statement as a base and can make more specific or add more constraint or examples as per your requirement.
    You can use nested loops, if-else statements, and other control flow statements to implement the game.
    You can use functions to organize your code and make it more readable.
    Make sure to test your program with different inputs to make sure it's working correctly.
    """

    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    # first a helper function to determine if a player has won
    def is_victory(icon_character, game_board):
        for combination in winning_combinations:
            if all(game_board[i] == icon_character for i in combination):
                return True
        return False

    # then a helper function to print out the board
    def print_board(game_board):
        print("|".join(game_board[:3]))
        print("|".join(game_board[3:6]))
        print("|".join(game_board[6:]))
        print("")

    # finally the code for the game
    def do_tic_tac_toe():
        board = ["_"] * 9
        turn = 0
        while "_" in board:
            print_board(board)

            if turn % 2 == 0:
                icon = "X"
            else:
                icon = "O"

            move = int(input(f"{icon}'s turn. Choose a number between 0 and 8: "))
            while board[move] != "_":
                move = int(input("Space already taken. Choose another number between 0 and 8: "))
            board[move] = icon

            if is_victory(icon, board):
                print_board(board)
                print(f"{icon} wins!")
                break

            turn += 1
            if "_" not in board:
                print("Draw!")

        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again == "N":
            return
        else:
            return do_tic_tac_toe()

    do_tic_tac_toe()


if __name__ == "__main__":
    """ Uncomment one of these to run/test that problem"""
    assert problem1(1234) == "1234th"
    assert problem2(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert problem3("abc", {"string": ["abc", "123", "do re mi"]})
    assert not problem3("da rey me", {"string": ["abc", "123", "do re mi"]})
    assert problem3(123, {"integer": [1, 1000]})
    assert not problem3("(123)-456-7891", "phone_number")
    assert problem3("amiller17@luc.edu", "email")
    assert problem4("A1") == "black"
    assert problem4("A8") == "white"
    assert problem4("H1") == "white"
    assert problem4("H8") == "black"

    for i in ["A1", "A8", "H1", "H8"]:
        print(problem4(i))

    problem5()
