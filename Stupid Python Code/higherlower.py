import requests
import json
import sys
import math

URL = "http://www.higherlowergame.com/questions/get/general"

HEADERS = {"Accept":"*/*",
          "Accept-Encoding":"gzip, deflate",
          "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
          "apikey":"7e93a522-17f0-4789-930c-a5f3b4c1acfd",
          "Connection":"keep-alive",
          "Host":"www.higherlowergame.com",
          "Referer":"http://www.higherlowergame.com/",
          "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
          "x-requested-with":"XMLHttpRequest"}

try:
    r = requests.get(url = URL, headers = HEADERS) 
    data = r.json()
except:
    print("This game requires a network connection, please check if you have one.\
if you are experiencing this error with a working network connection, the servers\
 may be done, and we ask that you wait a while before retrying")
    sys.exit()

element = data[0]
item = element["keyword"]
count = int(element["searchVolume"])


print("""
Welcome to the Higher or Lower game! In this game you must attempt to guess
whether a search term has a greater or lesser number of searches compared to
the term preceeding it.

For every correct answer, your earnings increase by 20% of your current bet.
Effectively, you earn 10% compounded onto your bet everytime you win. 1.5 times 
your original bet will be deducted when you finally get an answer wrong

This code was written by Bill Wang
""")

money = 100

def main(money):
    global item
    global count
    x = 1
    bet = -1
    prompt = "Please enter your bet: "
    while(bet < 0):
        try:
            bet = int(input(prompt))
            if(bet > money):
                prompt = "You cannot bet more than what you have, please enter\
     your revised bet: "
                bet = -1
            elif(bet <= 0):
                prompt = "Bets must be greater than zero, please enter your revised\
     bet: "
        except ValueError:
            prompt = "A numeric value is required, please enter your revised bet: "
            
    print("\nStarting Game...\n")

    while(True):
        compare = data[x]
        term = compare["keyword"]
        searches = int(compare["searchVolume"])
        
        ans = input("Compared to \"%s\" which has %d searches, do you think \"%s\" has a higher or lower number of searches? " %
                  (item, count, term)).lower()
        while not("higher" in ans or "lower" in ans):
            ans = input("Please enter \"higher\" or \"lower\": ")
            
        if("higher" in ans and searches >= count):
            print("You were correct, \"%s\" has %d searches" % (term, searches))
        elif("lower" in ans and searches <= count):
            print("You were correct, \"%s\" has %d searches" % (term, searches))
        else:
            if("lower" in ans):
                print("You were incorrect, \"%s\" has a whopping %d searches" % (term, searches))
                print("You lost on round %d, try to get a higher score" % x)
                break
            else:
                print("You were incorrect, \"%s\" only has %d searches" % (term, searches))
                print("You lost on round %d, try again to get a higher score" % x)
                break
        item = term
        count = searches
        x += 1

    winnings = bet*(1+(0.2/x))**x
    winnings -= bet*1.5
    float(format(winnings, ".2f"))
    if(winnings > 0):
        print("You won %f last round" % winnings)
    else:
        print("You lost %f last round" % winnings)
    money += winnings

    prompt = "Would you like to play again? "
    while(True):
        answer = input(prompt)
        if("y" in answer):
            print("You currently have %f" % float(format(money, ".2f")))
            main(money)
        elif("n" in answer):
            print("Okay, you ended with %f dollars, have a good day" % float(format(money, ".2f")))
            sys.exit()
main(money)
