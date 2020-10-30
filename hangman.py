from random import *
from time import sleep
readytostart=False
lista=['horse','giraffe','cow','dog','rhino','elephant','mouse','hamster','cheetah','lion']
listb=['tortilla','salami','pizza','ramen','sushi','noodles','rice','soup','cheese','onion']
listc=['corn','apple','evergreen','maple','yew','mulberry','basil','sunflower','rose','daisy']
listd=['corn','apple','evergreen','maple','yew','mulberry','basil','sunflower','rose','daisy','horse','giraffe','cow','dog','rhino','elephant','mouse','hamster','cheetah','lion','tortilla','salami','pizza','ramen','sushi','noodles','rice','soup','cheese','onion']
print('Welcome to Hangman!\nYou, the player, will have 5 lives.\nOnce you run out of lives, you die.\nIn this game, you guess the letters of a word. If you guess the word correctly, you win!\nIf you want a hint, type in hint when the system asks you for a letter or word\n')
no=int(input('Choose the topic of your words.\n1. Animals\n2. Food and Beverage\n3. Plants\n4. Random\n'))
if no==1:
    print('\nYou have chosen Animals as your subject')
    readytostart=True
elif no==2:
    print('\nYou have chosen Food and Beverage as your subject')
    readytostart=True
elif no==3:
    print('\nYou have chosen Plants as your subject')
    readytostart=True
elif no==4:
    print('\nYou have chosen Random as your subject')
    readytostart=True
elif no==123456789:
    print('\nYou have unlocked the Easter Egg! Read this!')
    print('\nooo.o.o.ooo.o.o\noo..o.o.o...oo.\no...ooo.ooo.o.o')
else:
    print('ERROR 404. Your choice was not a valid answer. Please restart the game and fill in your choice again.')
if readytostart==True:
    global guessable
    if no==1:
        guessable=lista[randint(0,9)]
    elif no==2:
        guessable=listb[randint(0,9)]
    elif no==3:
        guessable=listc[randint(0,9)]
    else:
        guessable=listd[randint(0,9)]
guess=list()
life=list()
for a in range(len(guessable)):
    guess.append('?')
life=[u'\u2764',u'\u2764',u'\u2764',u'\u2764',u'\u2764']
notguess=True
hint=False
derp=0
while notguess==True:
    print('\n',guess,'\n')
    print('Your Lives:',life)
    guessed=input('\nGuess a letter or the whole word:')
    if len(guessed)!=1:
        if guessed==guessable:
            notguess=False
        else:
            print('Sadly,',guessed,'is not the word. Try again!')
            life.pop(0)
            derp=derp+1
    else:
        if guessed in guessable:
            lettercount=0
            while lettercount<len(guessable):
                if str(guessed)==guessable[lettercount]:
                    guess[lettercount]=guessed
                lettercount=lettercount+1
        else:
            print('Sadly,',guessed,'is not in the word. Try again!')
            life.pop(0)
            derp=derp+1
    yeet=0
    for q in range(0,len(guessable)):
        if guess[q]==guessable[q]:
            yeet=yeet+1
        if yeet==len(guessable):
            notguess=False
    if derp==5:
        print('\nYou have used up all your lives! The word you were guessing was',guessable,'. Goodbye!')
        notguess=False
if derp!=5:
    print('\nCongratulations on guessing the word',guessable,'! Your score was',len(life))

    

