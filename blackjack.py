#blackjack.py
from random import shuffle
#import random
cards=[]
suits=["hearts","spades","diamonds","clubs"]
numbers=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
for suit in range(len(suits)):
    for num in range(len(numbers)):
        cards.append((numbers[num]," of ", suits[suit]))
    
shuffle(cards)

gameover = False
startcard = 0
while not gameover:
    playerhand = cards[startcard:startcard+2]
    startcard = startcard + 2 # or +=1
    print(playerhand)
    hitme='x'
    while hitme not in ["YyNn"]:
        hitme = input("Another card? Y/N")
        # we have a valid user input now
        # is it hit me or stay?
        while hitme in "Yy":
            # give player another card
            playerhand.append(cards[startcard])
            startcard += 1 # or startcard = startcard + 1
            print(playerhand)
        
        

