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

    for each_number in range(2,number+1):
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
    for each_smaller_number in range(2,number):
        if number % each_smaller_number == 0:
            number_is_prime = False
    return number_is_prime


    # return True


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
    words_list = ["car", "bar", "star", "barperson"]
    chosen_word = words_list[3]
    word_presentation = "_" * len(chosen_word)
    game_engine = True
    number_of_guesses = 4
    while game_engine:
        print(word_presentation)
        print(f"You have {number_of_guesses} guesses left")
        player_guess = input("Enter a symbol or a phrase: ")
        if len(player_guess) > 1:
            if player_guess == chosen_word:
                print("You guessed the phrase! You win the game.")
                game_engine = False
        else:
            if player_guess in chosen_word:
                print(f"Your guess: {player_guess} is in the randomly chosen word.")
                character_list = []
                index = 0
                for each_letter in chosen_word:
                    if player_guess == each_letter:
                        character_list.append(index)
                    index += 1  # equivalent to index = index + 1
                word_presentation_list = list(word_presentation)
                for each_index in character_list:
                    word_presentation_list[each_index] = player_guess
                word_presentation = "".join(word_presentation_list)
            else:
                print(f"Your guess: {player_guess} is not in the randomly chosen word.")
                number_of_guesses -= 1
                print(f"You have {number_of_guesses} guesses left")
        if number_of_guesses == 0:
            print("You have no more guesses you lose the game")
            game_engine = False
        if "_" not in word_presentation:
            print(f"You guessed all the letters in the word: {chosen_word}. You win!")
            game_engine = False

def word_guessing_game_for_loop():
    words_list = ["car", "bar", "star", "barperson"]
    chosen_word = words_list[3]
    word_presentation = "_" * len(chosen_word)
    number_of_guesses = 4
    number_of_unique_characters = len(set(list(chosen_word)))
    max_guesses = number_of_guesses + number_of_unique_characters
    for each_guess in range(max_guesses):
        print(word_presentation)
        print(f"You have {number_of_guesses} guesses left")
        player_guess = input("Enter a symbol or a phrase: ")
        if len(player_guess) > 1:
            if player_guess == chosen_word:
                print("You guessed the phrase! You win the game.")
                break
        else:
            if player_guess in chosen_word:
                print(f"Your guess: {player_guess} is in the randomly chosen word.")
                character_list = []
                index = 0
                for each_letter in chosen_word:
                    if player_guess == each_letter:
                        character_list.append(index)
                    index += 1  # equivalent to index = index + 1
                word_presentation_list = list(word_presentation)
                for each_index in character_list:
                    word_presentation_list[each_index] = player_guess
                word_presentation = "".join(word_presentation_list)
            else:
                print(f"Your guess: {player_guess} is not in the randomly chosen word.")
                number_of_guesses -= 1
                print(f"You have {number_of_guesses} guesses left")
        if number_of_guesses == 0:
            print("You have no more guesses you lose the game")
            break
        if "_" not in word_presentation:
            print(f"You guessed all the letters in the word: {chosen_word}. You win!")
            break

if __name__ == "__main__":
    print("Welcome to the Lab")
    """ Uncomment one of these to run that program"""
    # Example execution
    # primes(10)
    # 2,3,5,7
    # word_guessing_game()
    # word_guessing_game_for_loop()