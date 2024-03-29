#Sophia Ritner encode function UFID:79993252
#loop setup
loop_play = True

#encode def
def encode(input_str):
    new_string0 = str(int(input_str[0]) + 3)
    new_string1 = str(int(input_str[1]) + 3)
    new_string2 = str(int(input_str[2]) + 3)
    new_string3 = str(int(input_str[3]) + 3)
    new_string4 = str(int(input_str[4]) + 3)
    new_string5 = str(int(input_str[5]) + 3)
    new_string6 = str(int(input_str[6]) + 3)
    new_string7 = str(int(input_str[7]) + 3)
    new_password = (new_string0 + new_string1 + new_string2 + new_string3
                    + new_string4 + new_string5 + new_string6 + new_string7)
    return(new_password)

#decode def
def decode(input_str):
    decoded = ""
    for digit in str(input_str):
        decoded += str(int(digit) - 3)
    return decoded

#menu loop
while loop_play:
    print('Menu')
    print('---------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

#choices
    choice = input('Please enter an option: ')
    if choice == '1':
        encode_password = input('Please enter your password to encode: ')
        password_to_decode = encode(encode_password)
        print('Your password has been encoded and stored!')
    if choice == '2':
        print(f'The encoded password is', password_to_decode, 'and the original password is', decode(password_to_decode), '.')
    if choice == '3':
        loop_play = False
