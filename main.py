def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_word = count_string(text)
    duplicate_word_count = duplicate_word(text)
    for item in duplicate_word_count:
        if item["letter"].isalpha():
            print(f"The letter '{item["letter"]}' was found {item["num"]} time.")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_string(c):
   return len(c.split())

def sort_key(dic):
    return dic["num"]
def duplicate_word(c):
    lower_text = c.lower()
    word_count = {}
    word_list  = []
    for word in lower_text:
        word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.items():
        dic_for_list = {}
        dic_for_list["letter"] = key
        dic_for_list["num"] = value
        word_list.append(dic_for_list)
        word_list.sort(reverse=True, key=sort_key)
    return word_list
  


main()