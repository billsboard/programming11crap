import random as r
import sys
import math
import os


money = 100
multiplier = 1
minBet = 1;
playsSinceInc = 0

wins = 0
loss = 0




def main():
    answer = input("")
    if("y" in answer):
        print("You currently have $%d." % money, end=" ")
        bet = 1
        prompt = "Please enter your bet: "
        while(True): 
            try:
                bet = int(input(prompt))
                while(bet > money or bet <= 0):
                    if(bet <= 0):
                        print("The minimum bet is 1. ", end=" ")
                    elif(bet > money):
                        print("You cannot bet more that what you have.", end=" ")

                    bet = int(input("Please enter your revised bet: "))
                break;
            except ValueError:
                prompt = "Please enter a numeric value: "
                pass

        play(bet)
        print("Would you like to play again?", end = " ")
        main()
    elif("n" in answer):
        print("Goodbye, you played %d times, and finished with %d wins and %d losses"
              %((wins+loss), wins, loss))
        print("Saving game data...")
        save()
        sys.exit()
    elif("r" in answer):
        print("""\nBlackjack is a game of trying to achieve 21. without going over To achieve this
goal one must hit to be dealt another card, to achieve as close
to 21 as possible without exceeding it. Cards are face value
except for Aces, which can be 1 or 11, and face cards, which are
10. When you have achieved a close value, you may "stay", which
means you will recieve no more cards and your result will be
calculated. The player with the closer value will win.\n
Betting in this game works in the following way:

The player may place a bet at the beginning of each round. The final bet
is this value multipled by a multiplier starting at 1. The
more a player hits during the game, the higher the multiplier
becomes, incrementing by 1 for every 3 hits

Please note that if there is a tie, it will go to the house""")
        print("\nWelcome to the game of blackjack, would you like to play? ", end="")        
    else:
        print("Please enter a valid choice (yes, no or rules): ", end="")
    
    main()        

              
def play(bet):
    global money
    global multiplier
    global loss
    global wins
    cardList = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0}
    playerCards = [r.randint(1,13), r.randint(1,13)]
    AICards = [r.randint(1,13), r.randint(1,13)]
    redJacks = 0

    cardList[playerCards[0]] += 1
    cardList[playerCards[1]] += 1
    cardList[AICards[0]] += 1
    cardList[AICards[1]] += 1

    if(AICards[0] == 1):
        print("The dealer drew an ace")
    elif(AICards[0] == 11):
        print("The dealer drew a Jack")
    elif(AICards[0] == 12):
        print("The dealer drew a Queen")
    elif(AICards[0] == 13):
        print("The dealer drew a King")
    elif(AICards[0] == 8):
        print("The dealer drew an 8")
    else:
        print("The dealer drew a %d" % AICards[0])


    if(playerCards[0] == 11):
        if(r.randint(1,4-redJacks) <= 2):
            print("You drew a blackjack! This round is awarded to you and your winnings are multiplied by 1.5!")
            print("Your bet of %d was recieved! (bet %d x multipler %f)" % (bet*multiplier*1.5, bet, multiplier*1.5))
            money += bet*1.5
            wins += 1
            return
        redJacks += 1
    if(playerCards[1] == 11):
        if(r.randint(1,4-redJacks) <= 2):
            print("You drew a blackjack! This round is awarded to you and your winnings are multiplied by 1.5!")
            print("Your bet of %d was recieved! (bet %d x multipler %f)" % (bet*multiplier*1.5, bet, multiplier*1.5))
            money += bet*1.5
            wins += 1
            return
        redJacks += 1
    if(AICards[0] == 11):
        if(r.randint(1,4-redJacks) <= 2):
            print("The AI drew a blackjack! This round is awarded to the AI and all bets are multiplied by 1.5!")
            print("Your bet of %d was lost! (bet %d x multipler %f)" % (bet*multiplier*1.5, bet, multiplier*1.5))
            money -= bet*1.5
            loss += 1
            return
        redJacks += 1
    if(AICards[1] == 11):
        if(r.randint(1,4-redJacks) <= 2):
            print("The AI drew a blackjack! This round is awarded to the AI and all bets are multiplied by 1.5!")
            print("Your bet of %d was lost! (bet %d x multipler %f)" % (bet*multiplier*1.5, bet, multiplier*1.5))
            money -= bet*1.5
            loss += 1
            return
        redJacks += 1
    
    
    while(True):
        multiplier = math.floor((len(playerCards)+1)/3)
        totalSum = 0
        print("Your current cards are: ", end = "")
        ace = False
        for x in playerCards:
            if x == 1:
                print("A", end= " ")
                ace = True
                totalSum += x
            elif x == 11:
                print("J", end=" ")
                totalSum += 10
            elif x == 12:
                print("Q", end=" ")
                totalSum += 10
            elif x == 13:
                print("K", end=" ")
                totalSum += 10
            else: 
                print(x, end=" ")
                totalSum += x
        if totalSum > 21:
            loss += 1
            print("You busted with a total sum of %d" % totalSum)
            print("Your bet of $%d was lost. (bet $%d x multiplier %d)" %
                  (bet*multiplier, bet, multiplier))
            money -= bet*multiplier
            if(money <= 0):
                if(wins+loss == 1):
                    print("You lost all your money in %d round! You had %d wins and %d loss"%
                      (wins+loss, wins, loss))
                else:
                    print("You lost all your money in %d rounds! You had %d wins and %d losses"%
                          (wins+loss, wins, loss))
                sys.exit(0)
            return
        
        if ace:
            if not(totalSum + 10 > 21):
                print("Your total sum can be %d or %d" %(totalSum, totalSum + 10))
                totalSum += 10
            else:
                print("Your total sum is %d" % totalSum)
        else:
            print("\nYour total sum is %d" % totalSum)

        hit = input("Would you like to hit? ").lower()

        if ("y" in hit or "h" in hit) and not "st" in hit:
            temp = r.randint(1,13)
            while(cardList[temp] >= 4):
                temp = r.randint(1,13)
            if(temp == 11):
                if(r.randint(1,4-redJacks) <= 2):
                    print("You drew a blackjack! This round is awarded to you and your winnings are multiplied by 1.5!")
                    print("Your bet of %d was recieved! (bet %d x multipler %f)" % (bet*multiplier*1.5, bet, multiplier*1.5))
                    money += bet*multiplier*1.5
                    wins += 1
                    return
                redJacks += 1
            playerCards.append(temp)
        elif "n" in hit or "s" in hit:
            break;

    aiSum = 0;
    firstTime = True
    while(aiSum < 17):
        aiSum = 0
        if(not firstTime):
            temp = r.randint(1,13)
            while(cardList[temp] >= 4):
                temp = r.randint(1,13)
            AICards.append(r.randint(1,13))
        ace = False
        for x in AICards:
            if x == 1:
                ace = True
                aiSum += x
            elif x == 11:
                aiSum += 10
                if(r.randint(1,4-redJacks) <= 2):
                    print("The AI drew a blackjack! This round is awarded to the AI and all bets are multiplied by 1.5!")
                    print("Your bet of %d was lost! (bet %d x multipler %f)" % (bet*multiplier*1.5, bet, multiplier*1.5))
                    money -= bet*multiplier*1.5
                    loss += 1
                    return
                redJacks += 1
            elif x == 12:
                aiSum += 10
            elif x == 13:
                aiSum += 10
            else: 
                aiSum += x
        if ace and aiSum + 10 <= 21:
            aiSum += 10
        firstTime = False

    

    print("Your cards were: ", end="")
    for x in playerCards:
            if x == 1:
                print("A", end= " ")
            elif x == 11:
                print("J", end=" ")
            elif x == 12:
                print("Q", end=" ")
            elif x == 13:
                print("K", end=" ")
            else: 
                print(x, end=" ")  

    print("for a sum of %d" % totalSum)
            
    print("The AI had: ", end="")
    for x in AICards:
            if x == 1:
                print("A", end= " ")
            elif x == 11:
                print("J", end=" ")
            elif x == 12:
                print("Q", end=" ")
            elif x == 13:
                print("K", end=" ")
            else: 
                print(x, end=" ")

    if(aiSum > 21):
        print("and busted")
    else:
        print("for a sum of %d" % aiSum)

    if(totalSum > aiSum or aiSum > 21):
        print("You won! Bet of $%d recieved. (bet $%d x multiplier %d)" %(bet*multiplier, bet, multiplier))
        money += bet*multiplier
        wins += 1
    else:
        print("You lost, bet of $%d lost. (bet $%d x multiplier %d)"
              %(bet*multiplier, bet, multiplier))
        money -= bet*multiplier
        loss += 1

    if(money <= 0):
        if(wins+loss == 1):
            print("You lost all your money in %d round! You had %d wins and %d loss"%
              (wins+loss, wins, loss))
        else:
            print("You lost all your money in %d rounds! You had %d wins and %d losses"%
                  (wins+loss, wins, loss))
        sys.exit(0)

def save():
    f= open("saveData.txt","w+")
    f.write(str(money) + "\n" + str(wins) + "\n" + str(loss))
    f.close()

try:
    f = open("saveData.txt", "r")
    money = int(float(f.readline().rstrip()))
    wins = int(f.readline().rstrip())
    loss = int(f.readline().rstrip())
    f.close()
    os.remove("saveData.txt")
    print("Resuming saved game with %d wins and %d losses" % (wins,loss))
except:
    money = 100
    wins = 0
    loss = 0


    
print("Welcome to the game of blackjack, would you like to play? (Press r for rules) ", end = " ");

main()
