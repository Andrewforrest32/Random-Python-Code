def count_words(string):
    split_string = string.split(" ")
    num_words = len(split_string)
    return num_words

def count_punctuation(string):
    punc = []
    for character in string:
        if character.isalnum() == False and character != ' ':
            punc.append(character)
    num_punc = len(punc)
    return num_punc, punc
    
def count_capital_letters(string):
    capitals = 0
    for char in string:
        if char.isupper():
            capitals += 1
    return capitals
    
string = input("Enter string: ")
num_words = count_words(string)
num_punc, punc = count_punctuation(string)
num_caps = count_capital_letters(string)
print(f"The inputted string has {num_words} word(s), {num_punc} punctuation(s) ({punc}), and {num_caps} capital letter(s).")
