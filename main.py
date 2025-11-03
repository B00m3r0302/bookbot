from stats import number_of_words, words_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents


def main():
    frankenstein_content = get_book_text("books/frankenstein.txt")

    word_count = number_of_words(frankenstein_content)
    print(f"Found {word_count} total words")

    word_dictionary = words_dictionary(frankenstein_content)
    print(word_dictionary)

main()
