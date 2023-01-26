"""
Word guessing game

Finding all the primes

"""


def primes(number: int):
    """
    print all the primes up to number
    from lowest to highest
    """
    # Notably 1 isn't prime, so we will start with 2
    # also, range needs +1 to try the last number

    for each_number in range(2, number + 1):
        #     print(f"{each_number=}")
        #     is_it_prime(each_number)
        if is_it_prime(each_number):
            # print(is_it_prime(number))
            print(each_number)
        # if each_number is prime, then print in

    pass


def is_it_prime(number: int) -> bool:
    number_is_prime = True
    # we need to check if the number we get is divisible by each number less than it.
    for each_smaller_number in range(2, number):
        if number % each_smaller_number == 0:
            number_is_prime = False
    return number_is_prime


def word_guessing_game():
    """
    2 Parts:

    Part 1:
        make a game where a word is chosen
        then a player guesses a letter or the whole word
        if the word is right then the player wins
        otherwise,
        fill in the letter on the board
        if the player guesses a letter not in the word
        draw a picture on the screen using symbols
        if the picture is finished before the word is guessed
        then the computer wins
    """


if __name__ == "__main__":
    print("Welcome to the Lab")
    """ Uncomment one of these to run that program"""
