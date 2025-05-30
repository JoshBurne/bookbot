from stats import word_count, character_count 

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    #print(get_book_text("/home/joshburne/workspace/boot.dev/bookbot/books/frankenstein.txt"))
    print(word_count(get_book_text("/home/joshburne/workspace/boot.dev/bookbot/books/frankenstein.txt")))
    
    print(character_count(get_book_text("/home/joshburne/workspace/boot.dev/bookbot/books/frankenstein.txt")))



main()



