import random
import char_list

test_key = 9
test_message = 'hello world'

letter_list = char_list.alphabetical
number_list = char_list.numbers
spec_char_list = char_list.special_characters
crypted_message = []

def text_spliter(msg):
    words_list = msg.split(' ')
    return words_list

def loop_throught_elem(word_list, key):
    for word in word_list:              # return each word individually
        for i in range(0, len(word)):   # loop throught each letter
            for r in letter_list:
               if word[i] == r:
                   
                   crypted_message.append(letter_list.index[r + key])                   
    print(crypted_message)

# print(text_spliter(test_message))
loop_throught_elem(text_spliter(test_message), test_key)