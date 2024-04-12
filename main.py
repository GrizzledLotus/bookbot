def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_num_letters(text)
    sorted_letter_list = convert_dict_to_sorted_list(letter_dict)
    print_book_summary(book_path, num_words, sorted_letter_list)
    
    
def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letter_counts = {}
    alphabet_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    for c in list(text.lower()):
        if c not in alphabet_set:
            pass
        else:
            if c not in letter_counts:
                letter_counts[c] = 0
            letter_counts[c] += 1
    return letter_counts

def sort_on(dict):
    return dict["num"]

def convert_dict_to_sorted_list(dict):
    sorted_list =[]
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_book_summary(book_path, num_words, sorted_letter_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document.\n")
    for letter in sorted_letter_list:
        print(f"The {letter['char']} character was found {letter['num']} times.")
    print("--- End report ---")

    
main()