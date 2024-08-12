def main():
    book_path = "books/frankenstein.txt"
    book_text = read_text(book_path)
    word_count = count_words(book_text)
    print(f"This book contains {word_count} words.")

def count_words(text):
    return len(text.split())

def read_text(path):
    with open(path) as f:
        return f.read()

main()
