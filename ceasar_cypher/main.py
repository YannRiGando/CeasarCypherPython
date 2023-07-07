import char_list
import ceaser_cypher


letter_list = char_list.alphabetical
transition_list = []
while_state = True

print("Do you want to encrypt a message? Type 'yes' to encrypt, type 'no' to decrypt. ")

def loop_script():
    script_statement = input()
        
    if script_statement == "yes":
            
        text_input = input("Input your text to crypt: ")
        key_input = int(input("Input your crypting key: "))
    
        transition_list = ceaser_cypher.spliter(text_input)
        final_message = ceaser_cypher.crytping_function(transition_list, key_input, letter_list)

        print(final_message)
        while_state = False
            
    elif script_statement == "no":
        
        text_input = input("Input your text you want to decrypt: ")
        key_input = int(input("Input the crypting key: "))

        transition_list = ceaser_cypher.spliter(text_input)
        final_message = ceaser_cypher.decrypting_function(text_input, key_input, letter_list)
    
        print(final_message)
        while_state = False


    else:    
        print("Please type 'yes' or 'no': ")

    

while while_state == True:
    loop_script()