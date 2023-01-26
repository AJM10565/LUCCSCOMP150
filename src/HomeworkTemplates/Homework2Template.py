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


if __name__ == "__main__":
    """ Uncomment one of these to run/test that problem"""
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
