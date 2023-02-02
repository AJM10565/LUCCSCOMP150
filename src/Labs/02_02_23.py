"""
The plan for today's lab is to spend time exploring using lists and dictionaries to model planar grids
The end goal will be to create a crossword puzzle generator, where a crossword puzzle is created based on the words in
a text file.

I'm going to break down this lab into parts, and everyone will have time to work in groups, and then we'll discuss a
solution and go to the next part together. As is usually the case, solving the lab will be beneficial in solving the
homework problems.

Then you're going to build a modified crossword puzzle player. The game will be similar to the word_guessing_game from
last weeks lab, except instead of a single word, the player will be trying to solve the whole puzzle. The "clues", will
be sentences from the story where the word is missing, kind of like a madlib.

stories pulled from: https://www.gutenberg.org/files/20831/20831.txt


"""
from typing import List, Dict


def load_from_filepath(filepath: str) -> str:
    """
    The goal of this function is to successfully load a file given its relative or absolute path and return it as one
    big long string.
    """
    return ""  # your code goes here


def get_uniques(story: str) -> List[str]:
    """
    The goal of this function, is to take in a long text string, and return a list of only the unique words.
    While this is seemingly a silly goal, in data science and other fields, it is useful to be able to study uniqueness.
    """
    return []  # replace this with your code


def create_crossword_puzzle(
        unique_words: List[str],
        story: str,
        maximum_shared_letters_count: int = 1,
        minimum_shared_letters_count: int = 2,
        minumum_word_length: int = 3,
        maximum_word_length: int = 5
) -> List[str]:
    """
    In a cross word puzzle, words share one or more letters with each other. For now, let's say each word should
    share either 1 or 2 characters with another word.

    :param unique_words:
    :return:
    """
    minimum_shared_letters_count = 1
    maximum_shared_letters_count = 2

    return []  # replace this with your code


def do_these_words_share_a_letter(word1, word2) -> (bool, str):
    """
    Sometimes you need a function that does multiple things, in this case, you can have it return items in a comma
    separated fashion
    :param word1:
    :param word2:
    :return:
    shared: bool
    which_letter_is_shared: str
    """
    shared = False
    which_letter_is_shared = ""
    return shared, which_letter_is_shared


def format_crossword_puzzle(puzzle: List[str]) -> str:
    """
    So we're going to be printing the crossword puzzle in 2 steps:
    1. We're going to format the puzzle so that it looks nice (this function)
    2. We're going to print the formatted puzzle
    """

    return puzzle  # this probably won't look correct, so you're going to need to fix it


def is_puzzle_completed(puzzle: List[str]) -> bool:
    return False  # probably you're going to need to check something about the puzzle List


def generate_clues(puzzle: List[str], story: str) -> Dict[str, str]:
    """
    We're going to get a puzzle list, and the story, and we're going to need to generate clues for each word in the list
    :param puzzle:
    :param story:
    :return:
    """

    return {"": ""}


def guess_a_word():
    """
    Use a while loop, to make sure the word guessed meets the criteria (perhaps we tell the player the min and max
    length) of words in our puzzle, and only count guesses inside the range.
    :return:
    """
    return ""


def give_a_clue(clues: Dict[str, str],
                clues_guessed_correctly: int,
                bad_guesses_remaining: int,
                clues_given: List[str]) -> str:
    """
    Maybe, depending on some criteria, like number of bad guesses remaining, we tell them the give them all the clues
    Otherwise, we give them a random clue. Maybe if they guess a clue right, and not just a word right, we show them
    extra clues???
    Maybe under certain conditions we tell them the number of letters in the answer of a clue.
    :return:
    """
    return ""


def load_saved_game(puzzle_file_path):
    """
    If we get a file path, with a partially completed puzzle, we can load that game and play it instead of a new one.
    """
    clues_guessed_correctly = 0
    bad_guesses_remaining = 5
    puzzle = ""
    clues = {"": ""}
    clues_given = [""]

    return puzzle, clues, bad_guesses_remaining, clues_guessed_correctly, clues_given


def save_game_to_file(puzzle, clues, bad_guesses_remaining, clues_guessed_correctly, filepath):
    """
    We don't have time to play the game anymore, so instead we choose to save the game for later.
    """


def play_new_game_or_load_saved_game() -> str:
    """
    Ask the player if they want a "new" game or play a "load" a saved game
    """

    load = "load"
    new = "new"
    return new


def randomly_select_a_file_path(stories_file_paths: List[str]) -> str:
    return ""


def get_saved_game_file_path():
    """
    Ask the player for the file path to the saved game
    """
    return ""


def does_puzzle_contain_word(puzzle, word) -> bool:
    pass


def add_puzzle_to_word(puzzle, word) -> List[str]:
    """
    1. Modify the puzzle to contain the word
    2. return the new puzzle with the word filled in

    """
    return puzzle


def format_score_for_printing(puzzle: List[str],
                              clues_guessed_correctly: int,
                              bad_guesses_remaining: int) -> str:
    return ""


def wrong_choice_message(choice):
    """make this string return more descriptive"""
    return f"{choice}"


def clues_given_formatted_for_printing(clues_given) -> str:
    return ""


def play_crossword_puzzle():
    """
    This is the main function of our application, this week, I've started us off, in the future, you might get less code
    from me.
    """
    stories_file_paths = []

    if play_new_game_or_load_saved_game() == "new":
        story_file_path = randomly_select_a_file_path(stories_file_paths)
        story = load_from_filepath(story_file_path)
        unique_words = get_uniques(story)
        puzzle = create_crossword_puzzle(unique_words, story, 1, 2, 3, 5)
        clues = generate_clues(puzzle, story)
        bad_guesses_remaining = 5
        clues_guessed_correctly = 0
        clues_given = [""]
    else:
        saved_game_file_path = get_saved_game_file_path()
        puzzle, clues, bad_guesses_remaining, clues_guessed_correctly, clues_given = load_saved_game(
            saved_game_file_path)

    while not is_puzzle_completed(puzzle):
        print(format_crossword_puzzle(puzzle))
        clues_given.append(give_a_clue(clues, clues_guessed_correctly, bad_guesses_remaining, clues_given))
        print(clues_given_formatted_for_printing(clues_given))
        word = guess_a_word()
        if does_puzzle_contain_word(puzzle, word):
            puzzle = add_puzzle_to_word(puzzle, word)
        else:
            print(wrong_choice_message(word))
            print(format_score_for_printing(puzzle, bad_guesses_remaining, clues_guessed_correctly))
