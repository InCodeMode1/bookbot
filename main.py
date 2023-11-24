with open("books/frankenstein.txt") as f:
    file_contents = f.read()

wc = file_contents.split()


def word_count(words: list):
    print(len(words))


def char_count(letters: str):
    lc = {}
    for character in letters:
        if character.lower() in lc:
            lc[character.lower()] += 1
        else:
            lc[character.lower()] = 1
    return lc



word_count(wc)
print(char_count(file_contents))