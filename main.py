import sys
from stats import *


def main():
    ## book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = book_count_words(text)
    char_count = book_count_chars(text)
    chars_sorted_list = book_count_words_sorted(char_count)
    print_report(book_path, word_count, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def print_report(book_path, word_count,char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()