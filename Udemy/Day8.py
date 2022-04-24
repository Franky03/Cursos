alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shif):
    letters=[]
    new= []
    for l in text:
        if l != ' ':
            letters.append(l)
    for i in range(0, len(letters)):
        pos= alphabet.index(letters[i])
        pos += shif
        new.append(alphabet[pos])
    print("--"*20)
    print(f"The text is: {text}")
    print('The encoded text is: ', end='')
    for c in new:
        print(f"{c}", end='')
    print()


#Programa principal
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
