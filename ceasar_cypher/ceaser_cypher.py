import char_list

letter_list = char_list.alphabetical
number_list = char_list.numbers
spec_char_list = char_list.special_characters


def spliter(msg):
    return msg.split(' ')


def crytping_function(word_list, key, ltr_list):
    crypted_msg_array = []
    letter_list_len = len(ltr_list)
    
    for word in word_list:
        # return each word individually
        
        
        for i in range(0, len(word)):               
            # loop throught each letter
            
            letter_index = ltr_list.index(word[i])
            
            crypted_index = letter_index + key

            
            if crypted_index > letter_list_len - 1:
                crypted_index -= letter_list_len - 1

                        
            stored_letter = ltr_list[crypted_index]
            crypted_msg_array.append(stored_letter)
            
    
            
    crypted_message = ' '.join(crypted_msg_array).replace(' ', '')
    return crypted_message


def decrypting_function(crypted_msg, key, ltr_list):
    crypted_msg_array = []
    letter_list_len = len(ltr_list)
    
    for i in range(0, len(crypted_msg)):
        
        # go through the word and call the index of the letter 'n' at it's index
        # even when the letter appears multiple times
        # get the index
        letter_index = ltr_list.index(crypted_msg[i])
        
        crypted_index = letter_index - key
        
        if crypted_index < 0:
            crypted_index += letter_list_len - 1
            
        stored_letter = ltr_list[crypted_index]
        crypted_msg_array.append(stored_letter)
        
    decrypted_message = ' '.join(crypted_msg_array).replace(' ', '')
    return decrypted_message