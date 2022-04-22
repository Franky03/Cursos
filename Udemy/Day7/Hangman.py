from random import *

while True:
    index= randint(0, 300)
    file= open("palavras.txt", 'rt')
    l= file.readlines()
    selected= l[index].strip().split('\n')
    print(selected)
    n=int(input('Num: '))
    if n==1:
        break
