import os
os.system("pip install RandomWords")
import random_words as rw
from module import algorithm

while True:
    word = rw.RandomWords().random_word()
    if word[-1] != 's' and len(word) > 5:
        break

chance=6
ansBox = ['_' for i in range(len(word))]
word=[i for i in word] 
usedWords = set({})

print(' '.join(ansBox))

while chance != 0:
    print('%s chances left'%chance)
    OK = True
    while OK:
        guess = input('Enter a character : ')
        if guess.isalpha() == True:
            OK = False
        else:
            print('Please do not enter numbers or other signs ')
    usedWords.add(guess)

    if guess in word:
        index = algorithm.countIndex(word,guess)
        for i in index:
            ansBox[i] = guess
    else:
        chance-=1
    print(' '.join(ansBox))
    wordslist = [i for i in usedWords]
    print(','.join(wordslist))

    count = 0
    
    for i in ansBox:
        if i != '_':
            count+=1
    
    if count == len(word):
        print('\nCongrats ! You did it !')
        break

if chance == 0 and count != len(word):
    print('\nYou Lost @@')

print('\n'+''.join(word))
