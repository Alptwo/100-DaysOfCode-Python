from random import randint, random
from tkinter import Y

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,10, 10 ,10]

player_hand = []
dealer_hand = []

sum_of_player = 0
sum_of_dealer = 0

would_you_like_to_play = input("Welcome to the table, would you like to play a game of Blackjack? (y or n)\n")

def game_start():
    for i in range(0,2):
        player_hand.append(cards[randint(0,12)])
        dealer_hand.append(cards[randint(0,12)])

    print("Dealers cards: ["+str(dealer_hand[0])+", *]") 

    print("Your cards: "+str(player_hand))

    return player_hand, dealer_hand


take_another_card = "y"
if(would_you_like_to_play == "y"):
    player_hand, dealer_hand = game_start()
    for i in range(0,2):
        sum_of_player = player_hand[i] + sum_of_player
        sum_of_dealer = dealer_hand[i] + sum_of_dealer

        if(sum_of_player >= 21):
            if (sum_of_player == 21 and sum_of_dealer != 21):
                print("Congrats you won!")
            elif (sum_of_player > 21):
                print("Bummer you lost :(")

    take_another_card = input("Would you like to take another card? (y or n)\n")
    sum_of_dealer = 0
    sum_of_player = 0

    if(take_another_card == "y"):
        print("")
    else:
        print("Your cards was: "+player_hand)
        print("Dealers cards was: "+dealer_hand)
        for i in player_hand:
            sum_of_player = player_hand[i] + sum_of_player
        
        for i in dealer_hand:
            sum_of_dealer = dealer_hand[i] + sum_of_dealer
        
        #devam edilecek


    


else:
    print("Okay maybe later than goodbye")  
