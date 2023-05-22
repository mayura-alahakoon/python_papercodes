
hidden = 6
userInput = 0
while(userInput != hidden):
    userInput = int(input("Enter your guess: "))
    # if (userInput > 30 or userInput < 1):
    #     print("Out of bounds")
    if(userInput == hidden):
        print("You got it!")
    elif(userInput < hidden):
        print("Too low")
    else:
        print("Too high")
