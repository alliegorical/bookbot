def main():
    book_path = "books/frankenstein.txt" # maybe I'll allow custom inputs later
    book_text = read_text(book_path)
    word_count = count_words(book_text)
    print("========== Allie's Book Reporrrrrrrrt! ==========")
    print("Dum, tss, dum dum dum, tss... dum dum dum. dum. dum dum dum")
    print("Allie's book report!")
    print(f"This book contains {word_count} words.", end="")
    letter_count = count_each_letter(book_text)
    sorted_count = sort_letters(letter_count)
    for entry in sorted_count:
        print(f"\nThe letter {entry} appears {sorted_count[entry]} times.", end=" ")
    print("so few! very smol number ^.^")
    print("Thank you for reading Allie's book report!")

def sort_letters(dict):
    dict_list = []
    for key in dict:
        dict_list.append({key: dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    sorted_dict = {}
    for entry in dict_list:
        sorted_dict.update(entry)
    return sorted_dict

def sort_on(dict):
    return list(dict.values())[0]

def count_each_letter(text):
    letter_count = {}
    letter_count = init_alphabetized_letters(letter_count)
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter.isalpha() == True: # make sure the character is an actual letter
            letter_count[letter] += 1
    return letter_count

# initialize the keys in alphabetical order because we're tidy
#   well now that we're sorting them by frequency this bit's just pointless >_<
def init_alphabetized_letters(dict):
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    for letter in lower_alpha:
        dict[letter] = 0
    return dict
    
def count_words(text):
    return len(text.split())

def read_text(path):
    with open(path) as f:
        return f.read()

main()
