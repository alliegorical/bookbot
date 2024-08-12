def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    words = file_contents.split()
    word_total = len(words)
    print(f"This book contains a total of {word_total} words.")

main()
