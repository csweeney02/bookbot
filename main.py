def main():
    book = "books/frankenstein.txt"
    print(f"--- Begin Report of {book} ---")
    text = get_book_text(book)
    count = word_count(text)
    print(f"{count} words found in the document")
    print()
    characters = count_characters(text)
    list_characters = dict_to_list(characters)
    list_characters.sort(reverse=True,key=sort_on)
    for char in list_characters:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print ("--- End Report ---")
    

def count_characters(book_text):
    book_text = book_text.lower()
    char_dict = {}
    for character in book_text:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    
    return char_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(book_text):
    words = book_text.split()

    return len(words)

def dict_to_list(dict):
    list = []
    for d in dict:
        if d.isalpha():
            new_dict = {}
            new_dict["char"] = d
            new_dict["count"] = dict[d]
            list.append(new_dict)
    return list

def sort_on(dict):
    return dict["count"]

main()