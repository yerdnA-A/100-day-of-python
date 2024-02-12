def encrypt(msg,num_code):
    for i in msg:
        encrypt_msg = chr((ord(i) - ord('a') + num_code) % 26 + ord('a'))
        print(encrypt_msg, end='')
    print()

def decrypt(msg, num_code):
    for i in msg:
        decrypt_msg = chr((ord(i) - ord('a') - num_code) % 26 + ord('a'))
        print(decrypt_msg, end='')
    print()

while True:
    choice = input("Type 'encode' to encrypt, type 'desencode' to decrypt:\n")
    if choice == 'e':
        msg = input("Type your message:\n")
        num_code = int(input("Type the shift number:\n"))
        encrypt(msg=msg, num_code=num_code)
    else:
        msg = input("Type your message:\n")
        num_code = int(input("Type the shift number:\n"))
        decrypt(msg=msg, num_code=num_code)

    repeat = input("Do you wanna try again? (Y/N)").upper().strip()
    
    if repeat != 'Y':
        break
    else:
        continue