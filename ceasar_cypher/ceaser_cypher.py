import random
import char_list

test_key = 9
test_message = 'hello world'

def text_spliter(msg):
    words_list = msg.split(' ')
    return words_list

def loop_throught_elem(word_list):
    for word in word_list:
        for letter in word:
            print(letter)

# def Shift_position(msg, key):
#     splitted_text = text_spliter(msg)
#     sample_letters = char_list.alphabetical
    
#     for index in range(splitted_text):
#         for letter in splitted_text[index]:
#             print(letter)            


# print(text_spliter(test_message))
loop_throught_elem(text_spliter(test_message))