from stats import word_count, character_count , sorter
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) <= 1:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        word_counter = word_count(get_book_text(sys.argv[1]))
    
        character_dict = character_count(get_book_text(sys.argv[1]))
        result = sorter(character_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(word_counter)
        print("--------- Character Count -------")
        for dictionary in result:
            print(f'{dictionary['char']}: {dictionary['num']}')
        print("============= END ===============")

main()