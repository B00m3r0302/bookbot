import sys
from stats import number_of_words, words_dictionary, format_word_count


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents


def main():

    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        word_count = number_of_words(get_book_text(arguments[1]))
        header = """
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------"""
        print(header)
        print(f"Found {word_count} total words")

        word_dictionary = words_dictionary(get_book_text(arguments[1]))

        print("--------- Character Count -------")
        format_word_count(word_dictionary)
        print("============= END ===============")

main()
