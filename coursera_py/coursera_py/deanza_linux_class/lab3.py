#Name: Gregory Tuayev-Deane
# Description: Play a "guess a number" game

import random

def getInput():
    while True:
        guess = int(input("Enter a guess for a number between 1 and 20: "))
        if guess<=20 and guess>=1:
            return guess
        else:
            break

def checkNum(guess:int,target:int):
    if guess > target:
        ret_str = "Too high"
    elif guess <target:
        ret_str = "Too low"
    elif guess == target:
        ret_str = "You got it"
    return ret_str

if __name__ == "__main__":
    
    for i in range(1,6):
        print("------------------------------------------")
        print("This is attempt: " + str(i) + "  out of 5")
        randNum = random.randint(1,20)
        
        ret_str = ""
        while ret_str != "You got it":
            guess = getInput()
            ret_str = checkNum(guess=guess, target=randNum)
            print(ret_str)

            if ret_str == "You got it":
                break


    

