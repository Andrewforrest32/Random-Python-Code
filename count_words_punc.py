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
    
string = input("Enter string: ")
num_words = count_words(string)
num_punc, punc = count_punctuation(string)
print(f"The inputted string has {num_words} word(s) and {num_punc} punctuation(s), being {punc}.")

