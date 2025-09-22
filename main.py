import sys
from stats import get_num_words
from stats import get_chars_dict
from stats import sort_dict


def main():
    if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      return sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict_list = sort_dict(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for v in sorted_dict_list:
        if v["char"].isalpha():
          print(f"{v["char"]}: {v["num"]}")
    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
