import random
import char_list
import math

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
    
    letter_list_len = len(letter_list)
    
    for word in word_list:
        # return each word individually
        
        
        for i in range(0, len(word)):               
            # loop throught each letter
            
            
            letter_index = letter_list.index(word[i])
            
            crypted_index = letter_index + key
            # print(crypted_index)
            
            if crypted_index > letter_list_len - 1:
                crypted_index -= letter_list_len - 1
            
            # print(crypted_index)
            
            stored_letter = letter_list[crypted_index]
            crypted_message.append(stored_letter)
            
    print(crypted_message)

    

    

clean_text = text_spliter(test_message)
loop_throught_elem(clean_text, test_key)