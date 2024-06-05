def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def print_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    alpha_dict = {}

    for char in chars_dict:
        if char.isalpha():
            alpha_dict[char] = chars_dict[char]
        

    sorted_dict = dict(sorted(alpha_dict.items()))

    for char in sorted_dict:   
        print(f"The '{char}' character was found {sorted_dict[char]} times")

    print("--- End report ---")
    pass

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()