from typing import List


def load_file(path_to_file) -> list[str]:
    with open(path_to_file) as f:
        return f.readlines()


if __name__ == "__main__":
    text = load_file('/Users/ajm10565/IdeaProjects/LUCCSCOMP150/src/texts/book.txt')

    print(text)

