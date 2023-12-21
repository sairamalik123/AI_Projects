import numpy as np

totalScore = 100
noOfTries =5
values = np.random.randint(10)
userInput =  int(input("Enter an integer: "))

if(userInput == values):
    print("Your guess is correct")
else:
    while(userInput != values):
        if(userInput > values):
            print("Your input is greater than the number, try again")
            totalScore = totalScore-5
            noOfTries -=1
            if(noOfTries ==0):
                print("You have lost")
                break
            userInput =  int(input("Enter an integer: "))
        else:
            print("Your input is lower than the number, try again")
            totalScore = totalScore-5
            noOfTries -=1
            if(noOfTries==0):
                print("You have lost")
                break
            userInput =  int(input("Enter an integer: "))
if(totalScore > 75):
    print("Your score is", totalScore)