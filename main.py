def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_word = count_string(text)
    duplicate_word_count = duplicate_word(text)
    print(duplicate_word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_string(c):
   return len(c.split())


def duplicate_word(c):
    lower_text = c.lower()
    word_count = {}
    for word in lower_text:
        word_count[word] = word_count.get(word, 0) + 1
    remove_duplicates = dict(set(word_count.items()))
    return remove_duplicates


main()