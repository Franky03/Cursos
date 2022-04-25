from Day8 import encrypt, decrypt

while True:
    direction= str(input("Type 'encode' to encrypt, type 'decode' to decrypt: ")).lower()
    if direction=='encode' or direction=='decode':
        break
    else:
        print("ERROR")
if direction=='encode':
    while True:
        encode= str(input("Type the message: ")).lower()
        shift= int(input("Type the shift number: "))
        encrypt(encode, shift)
        resp= str(input("Want to continue? [S/N]: ")).upper().strip()[0]
        if resp=='N':
            break
if direction=='decode':
    while True:
        decode= str(input("Type the encrypted code: ")).lower()
        shift= int(input("Type the shift number: "))
        decrypt(decode, shift)
        resp= str(input("Want to continue? [S/N]: ")).upper().strip()[0]
        if resp=='N':
            break
