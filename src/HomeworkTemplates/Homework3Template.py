"""
Homework #3 Instructions:
Submit final solution on sakai. Use this file as a template, rename according to the class convention: UVIDHomework3.py
To the best of your ability complete problems 1,2 and 3. If you use a resource, be sure to leave a link inside the
function documentation for that problem.
"""


def problem1(board: list) -> bool:
    """
    Write a Python function called problem1() that takes a single argument board, a list of integers. The function
    should check if the given board represents a correct solution of a sudoku puzzle.

    A sudoku board is a 9x9 grid of numbers such that each row, column, and 3x3 sub-grid contains all the numbers from
     1 to 9 exactly once. The input board list may have an arbitrary length, but should be a perfect square,
     representing a sudoku board of size x size grid, where size = sqrt(len(board)).

    The function should return True if the given board represents a correct solution of a sudoku puzzle,
    and False otherwise.
    """


def problem2(size: int) -> list:
    """
    Write a Python function called problem2() that takes a single argument size, an integer representing the size
    of the sudoku board. The function should generate and return a partially filled sudoku board of size x size grid,
    with enough digits filled in, so that it can be solved using the rules of sudoku.

    A sudoku board is a grid of numbers such that each row, column, and 3x3 sub-grid contains all the numbers from 1 to
    size exactly once. The generated sudoku board should contain a sufficient number of filled in digits, so that a
    solution to the puzzle can be found using the rules of sudoku. The board should be represented as a list
    of integers.

    The function should return the partially filled sudoku board as a list of integers, with empty spaces filled in
     with 0's.
    """


def problem3(board: list)-> bool:
    """
    Write a Python function called check_unique_solution that takes a single argument board, a list of integers
    representing a partially filled sudoku board. The function should check if there is a single unique solution to the
     sudoku puzzle represented by the board, or if there are multiple solutions.

    A sudoku board is a grid of numbers such that each row, column, and 3x3 sub-grid contains all the numbers from 1 to
     size exactly once. The input board list may have an arbitrary length, but should be a perfect square, representing
      a sudoku board of size x size grid, where size = sqrt(len(board)).

    The function should return True if there is a single unique solution to the sudoku puzzle represented by the board,
     and False otherwise, i.e., if there are multiple solutions to the puzzle.
    """


if __name__ == "__main__":
    """ Uncomment one of these to run/test that problem"""
    # problem1([1,2,3,3,2,1,2,1,3])
    # problem2(9)
    # problem3(problem2(9))
