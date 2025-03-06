from stats import count_num_of_words, count_characters, sort_characters
import sys, fileinput

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def print_report(path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        book_as_string = get_book_text(book_path)
        num_words = count_num_of_words(book_as_string)
        counted_characters = count_characters(book_as_string)
        sorted_list = sort_characters(counted_characters)
        print_report(book_path, num_words, sorted_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()