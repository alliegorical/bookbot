def main():
    book_path = "books/frankenstein.txt" # will allow custom inputs later
    book_text = read_text(book_path)
    word_count = count_words(book_text)
    print(f"This book contains {word_count} words. What follows is a count of each letter:")
    print(count_each_letter(book_text))

def count_each_letter(text):
    letter_count = {}
    letter_count = init_alphabetized_letters(letter_count)
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in "qwertyuiopasdfghjklzxcvbnm": # make sure the character is an actual letter
            letter_count[letter] += 1
    return letter_count

# start by putting the keys in alphabetical order because we're tidy
def init_alphabetized_letters(dic):
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    for letter in lower_alpha:
        dic[letter] = 0
    return dic
    
def count_words(text):
    return len(text.split())

def read_text(path):
    with open(path) as f:
        return f.read()

main()
