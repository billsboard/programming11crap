import time
import random
import sys

answer= input("Welcome, for copyright purposes, this game is called 'The Lower or Higher Game! Do you want to play? ")
while (not ("y" in answer)) :
    if ("N" in answer or "NO" in answer or "n" in answer):
        answer = input ("I don't take no for an answer. Do you want to play? ")
    else:
        answer = input ("How about you answer that question again? Either you didn't say 'yes' or you understand the question!~ ")
print ("Alrighty, that’s great news. I, your friendly Bill-programmed AI machinery that comes in the form of a computer, will come up with a number between 0 and 100 and YOU will have to guess it.")
name= input ("By the way, I don’t particularly care for you name, but I might as well learn it to be a polite person… something that’s pretty uncommon these days. So what is it? ")

if len(name) > 5:
    print("Your name is too long, your name will now be Bob. Alright Bob, I’ll continue with the instructions. ")
    name = "Bob"

else:
    print ("Nice! You have an adequate name, short and sweet. Alright " +name + ", I’ll continue with the instructions. ")

money= 100
print("You have $" + str(money) + ". Honestly, I feel like that's too much, but who am I to complain. I'll tell you if your guess is [ HIGHER ] or [ LOWER ] than my number.")
print("If you get my number in less than 5 gueses, I'll double your bet. Honestly, what a steal! ")
  
print("If you take more than 5 guesses, then sorry bud. It sucks to be you. So capiche? ")




def play():
    global money
    numb = random.randint(1,100)
    bet=input("Now much do you want to bet? ")
    while not bet.isnumeric():
        bet = input("I know people are getting dumber, but at least enter a positive numerical value please: ")

    if int(bet) == 0:
        print("I guess you thought you found a loophole. As a punishment, I'm making you go all in")
        bet = money
    if int(bet) > money:
        print("... ")
          
        print("Seriously? How dumb are you? Has the intelligence of humans degraded to such a stage? I guess I'll just auto-correct your bet")
        print("Oh, and also I'm making it impossible to win this round")
        numb = 101
        bet = money

    answer= input("Are you ready? ")
    while (not ("y" in answer)):
        if ("N" in answer or "NO" in answer or "n" in answer):
            print("Fine. You have five seconds, " + name + ". ")
            answer = input ("No w are you ready to play? ")
        else:
            answer = input ("How about you answer that question again? Either you didn't say 'yes' or you understand the question!~ ")
        
    guessesnumb = 5


    while guessesnumb > 0 and numb != 101:
        guess= input("C'mon hurry up. Take a guess, " + name + ". ")
        while not guess.isnumeric():
            guess= input("You need to enter a number, " + name + ". ")
        while int(guess) > 100 or int(guess) <= 0:
            guess = input("The bounds of this game are 1 to 100 inclusive. Enter a valid value: ")
            while not guess.isnumeric():
                guess= input("You need to enter a number, " + name + ". ")
        if int(guess) < numb:
            if(guessesnumb > 1):
                print("Your guess is too low, fam. Shoot [ HIGHER ]. ")
            guessesnumb= guessesnumb - 1
        if int(guess) > numb:
            if(guessesnumb > 1):
                print("You're shooting too high. Tone it down a little. You need to go [ LOWER ] ")
            guessesnumb= guessesnumb - 1
        if (int(guess) == (numb)):
            print("Nice. You're actually going to profit from this, " + name + ". ")
            money= money + int(bet)*2
            print("You have $" + str(money) + ".")
            answer= input("Play again? ")
            if "n" or "N" in answer:
                answer = input ("I don't take no for an answer. Do you want to play? ")

    
    
    if(numb != 101):
        print("Nope, sorry bad luck. The number was " + str(numb) + ". Kiss goodbye to your dreams of becoming rich and famous. ")
    else:
        print("Well, you didn't win, in fact you didn't even get to play. How sad.")
    money= money - int(bet)
    print("You have $" + str(money) + ".")
    if(money <= 0):
        print("Sorry man. Get outta here. Thanks for the money. You're broke now. Cya later alligator. ")
        sys.exit()
    answer= input("Play again? ").lower()
    while"n" in answer:
        answer = input ("I don't take no for an answer. Do you want to play? ")
    
    play()
    

       

play()


