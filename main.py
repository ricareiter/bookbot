def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words_counter = len(file_contents.split())
        return words_counter
        

def letter_counter():
    unique_letters = []
    split_word = [" "]
    symbols_dic = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_string = file_contents.lower()
        remove_space = lower_string.split()
        for word in remove_space:
            for letter in word:
                split_word.append(letter)
        for letter in split_word:
            if not letter in unique_letters:
                unique_letters.append(letter)
        for symbol in unique_letters:
            letter_counter = 0
            for letter in lower_string:
                find_letter = letter.count(symbol)
                letter_counter = letter_counter + find_letter
            symbols_dic.update({symbol:letter_counter})
    return symbols_dic


def report(dic, words_counter):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_counter} words found in the document")
    for key, value in dic.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

report(letter_counter(), main())