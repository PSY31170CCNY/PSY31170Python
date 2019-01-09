#blackjack.py
from random import shuffle
#import random

# make a function that counts up the cards in a hand
def countup(hand):
    ace=False
    total = 0
    for card in range(len(hand)):
        # e.g. hand[card] could be ('Queen', ' of ', 'diamonds')
        cardnum = hand[card][0]
        if cardnum == "Ace" :
            num = 0
            ace = True
        elif cardnum in ("King","Queen","Jack","10"):
            num = 10
        else:
            num = int(cardnum)
        total = total + num
        if ace and total > 10:
            total = total + 1
        else:
            total = total + 11
    return total
        
    # -- return count of cards in a hand
    
    return 0
                   
# initialize variables
playerwins=0
playerloses =0
cards=[]
suits=["hearts","spades","diamonds","clubs"]
numbers=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
for suit in range(len(suits)):
    for num in range(len(numbers)):
        cards.append((numbers[num]," of ", suits[suit]))
        # cards.append(numbers[num]+" of "+suits[suit])
    
shuffle(cards)

gameover = False # flag to tell us if no more cards in the deck
startcard = 0
while not gameover:
    # check if the game is over: if there are fewer than 5 cards
    if startcard > 48:
        print("Game over! Player won ", playerwins, \
              " hands and lost ",playerloses)
        gameover= True
        break
    # starting a new hand
    playerhand = cards[startcard:startcard+2]
    startcard = startcard + 2 # or +=1
    print("Here is your starting hand: ", playerhand)
    # what if the player gets 21 right away?
    # --> add up the cards!!
    if countup(playerhand) == 21:
        # player wins automatically!!
        print("Congratulations, you win!")
        # continue the play loop
        playerwins +=1
        continue
        dealerhand = cards[startcard:startcard+2]
        startcard = startcard + 2 # or +=1   
    hitme='x'
    while hitme not in "YyNn":
        hitme = input("Another card? Y/N")
        # we have a valid user input now
        # is it hit me or stay?
        if (hitme not in 'YyNn'):
            print(" enter Y or N, please")
            continue
        # give player another card
        print("hitme is ",hitme)
        print('is hitme in Yy?', hitme in "Yy")
        if hitme in "Yy":
            playerhand.append(cards[startcard])
            startcard += 1 # or startcard = startcard + 1
            print(playerhand)
            # check the card totals
            # --> add up the cards
            total = countup(playerhand)
            if total > 21 :
                # player loses
                print ("You lost. ")
                playerloses +=1
                break
            if total == 21 : #player wins
                print("Blackjack! you win!")
                break
        else:
            print("hitme ",hitme," not in YyNn:" , (hitme not in "YyNn"))
        total = countup(playerhand)
    if total >= 21:
        gameover = False
        continue
    # No more cards dealt to player, see who won
    playertot = countup(playerhand)
    dealertot = countup(dealerhand)
    if playertot > dealertot:
        print("Player wins with total count of",\
              playercount, "greater than dealer's",dealercount)
    else:
        print("Player loses with ",playercount,\
              " less than dealer's",dealercount)
    
        




