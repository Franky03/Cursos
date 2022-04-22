import random
from words import words
from hang_visual import lives_visual_dict

def app(lista, list2):
    for c in range(0, len(list2)):
        lista.append('_')

while True:
    life=6
    word= random.choice(words).upper()
    while '-' in word or ' ' in word:
        word= random.choice(words).upper()
    letters= []
    for l in word:
        letters.append(l)
    print(word)
    tabe=[]
    app(tabe, letters)
    print(tabe)
    while life>0:
        guess= str(input("Guess a letter: ")).upper()
        if guess in letters:
            pos= letters.index(guess)
            tabe[pos]= guess
            print(tabe)
        else:
            print(False)
    num= int(input('NUM: '))
    if num==0:
        break