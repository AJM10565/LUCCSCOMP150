"""
Implement the following functions and then fill out the __main__ to have them executed as described below:

"""
from typing import List, Dict
import turtle

t = turtle.Turtle()
t.penup()
colors = ["red", "orange", "yellow", "green", "blue", "deep pink", "purple", "black"]
color_index = 0


def draw_word(word, frequency, color):
    t.color(color)
    font_size = frequency + 3
    t.write(word, font=("Arial", font_size, "normal"), align="center")
    t.forward(font_size * len(word))
    t.left(80)


def draw_words_from_list(word_list: List[str]):
    """
    Here is an example function that draws a word diagram based on a list of words. In this case, the diagram uses the
    length of the word to determine the size of the word, and the color of the word, is random.
    :param word_list: a list of words
    :return: draws a word diagram
    """
    global color_index, colors
    for i in range(len(word_list)):
        color_index += 1
        if color_index >= len(colors):
            color_index = 0
        color = colors[color_index]
        word = word_list[i]
        frequency = len(word)
        draw_word(word, frequency, color)


# Part I: reading files and writing data
def load_file_from_path(file_path: str) -> str:
    """
    Create a function that, given a relative file path, opens a file, and returns a string with its contents
    :param file_path:
    :return:
    """
    return ""


def write_data_to_file(file_path: str, data: str):
    """
    create a function that, given a relative file path, opens a file, and writes a given string to that file
    :param file_path:
    :param data:
    :return:
    """
    pass


# Part II: Morse Code
def build_morse_code_dictionary(encoding: str) -> dict:
    """
    Create the morse code dictionary from an encoding string
    :param encoding: this is a something we get from a file
    :return: an encoding we can use to encrypt and decrypt messages
    """
    encoding_dictionary: dict = {}
    return encoding_dictionary


def encode_data(data: str, encoding: dict) -> str:
    """
    encode the hidden data using the encoding dictionary
    :param data:
    :param encoding:
    :return:
    """
    return ""


def decode_data(hidden_data: str, encoding: dict) -> str:
    """
    decode the hidden data using the encoding dictionary
    :param hidden_data:
    :param encoding:
    :return:
    """
    return ""


# Part III: Word Cloud
def create_word_cloud_dictionary(story: str) -> Dict[str:int]:
    """
    Using the story text as a guide, first:
    1. replace any "-" character with the space(" ") character
    2. replace any "(" character with the space(" ") character
    3. replace any ")" character with the space(" ") character
    4. make sure all the words are lower case
    5. remove any numbers
    6. split the story on space(" ") characters into a list, assign the variable word_list to this list
    7. create a second list of just the unique words in word_list, assign the variable unique_word_list to this list
    8. create a dictionary, call it wordcloud.
    9. add each word in the unique_word_list to the wordcloud, with a value equal to its frequency in word_list
        i. use the get_word_frequency function to get the frequency of the word in the list
    10. return wordcloud

    :param story:
    :return:
    Example wordcloud
    {
    "and": 4,
    "but": 12,
    "forget": 1
    }
    """
    return {}


def get_word_frequency(word_list: list, word: str) -> int:
    """
    The goal of this function is to return a number which represents the frequency with which a word appears in a list.
    :param word_list: a list of words, some words appear more than once
    :param word: a word
    :return: a number, which represents the number of times the word appears in the list
    """
    return 0


def draw_turtle_word_cloud(wordcloud: dict):
    """
    Your task is to create a word cloud. Instead of the length of the word, you will make words larger depending on their
    frequency in the provided text. You will also use a specific color, depending on the frequency of the word.\

    Use draw_words_from_list as a guide!!!
    :param wordcloud: a dictionary of {word:frequency} that captures the frequency with which words appear in a text.
    :return: draws a color coded word cloud, where the size and color of the word, depend on the frequency with which it
    appears in the text
    """
    pass


if __name__ == "__main__":
    # some Demo code
    words = ['one', 'dollar', 'and', 'eighty-seven', 'cents', '', 'that', 'was', 'all', 'sixty', 'of', 'it', 'in',
             'pennies', 'saved', 'two', 'at', 'a', 'time', 'by', 'bulldozing', 'the', 'grocer', 'vegetable', 'man',
             'butcher', 'until', 'ones', 'cheeks', 'burned', 'with', 'silent', 'imputation', 'parsimony', 'such',
             'close', 'dealing', 'implied', 'three', 'times', 'della', 'counted', 'next', 'day', 'would', 'be']
    draw_words_from_list(words)
    turtle.done()  # keep the turtle window open if working on your local machine
    # Part IV: Putting it all together
    # read in the decode file and create a morse code encoder from the file
    # read in the message file, and encrypt it using the encoder
    # write the encrypted message to the allthefilesarebelongtous directory
    # read in the encrypted message from the allthefilesarebelongtous directory and decrypt it
    # write out the decrypted message to the Home directory
    # Part V: Word cloud stuff
    # read in the termsofservice.txt file
    # create a word cloud dictionary based on the frequency of words in the text
    # draw the word cloud using the dictionary you just created
