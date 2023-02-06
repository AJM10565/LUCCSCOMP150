from typing import List


def load_file(path_to_file) -> str:
    with open(path_to_file) as f:
        return f.read()


def write_file(path_including_file_name, text):
    with open(path_including_file_name, 'w') as file:
        file.write(text)


def fix_author(author):
    """
    Fixes First Last\n\nThe Title to be
    The_Title_by_First_Last
    """
    data = author.split("\n\n")
    name = data[0]
    title = data[1]
    name = name.replace(" ", "_")
    title = title.replace(" ", "_")
    return f"{title}_by_{name}"


if __name__ == "__main__":
    import pathlib

    path = pathlib.Path(__file__).parent.resolve()
    resolve = pathlib.Path().resolve()
    full_text = load_file('./book.txt')
    multiple_texts = full_text.split("\n\n\n")
    print(f"{len(multiple_texts)=}")
    count = 0
    byline = ""
    text = ""
    books_dict = {}
    while count != len(multiple_texts):
        each_book = multiple_texts[count]
        passage_length = len(each_book)
        if passage_length <= 100:
            # write author, text to dictionary, reset author and text
            books_dict[byline] = text
            byline = each_book.strip()
            byline = fix_author(byline)
            text = ""
            print(f"{byline=}")
        else:
            text += each_book
            print("book part")
        count += 1
    print(books_dict.keys())

    for byline, text in books_dict.items():
        path_to_new_book = f"{path}/books/{byline}.txt"
        print(f"{path_to_new_book=}")
        write_file(path_to_new_book, text)
