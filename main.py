with open("books/frankenstein.txt") as f:
    file_contents = f.read()

wc = file_contents.split()

def word_count(words: list):
    return len(words)


def letter_count(letters):
    lc = {}
    for letter in letters:
        if letter.isalpha():
            if letter.lower() in lc:
                lc[letter.lower()] += 1
            else:
                lc[letter.lower()] = 1
    return lc


def report(file , fn):
    
    print(f"--- Begin report of {fn.name} ---")
    print(f"{word_count(wc)} words found in document")

    letters = letter_count(file)
    sort_letters = list(letters)
    sort_letters.sort()
    
    for letter in sort_letters:
        print(f"The {letter} character has been found {letters[letter]} times")


report(file_contents, f)