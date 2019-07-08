# Prime Number Finder!

# Converted from my Khan Academy code to Python on June 19
# 2019 June 30, added user input in program, error checking and program restart

run = True


def restartProgram():
    global run

    while True:
        print("New prime?  y / n")
        choice = input()
        
        if choice == "y":
            print("Hit me, baby.  One more prime!")
            break
            
        elif choice == "n":
            print("Laters!  Prime out.")
            run = False
            break
            
        else:
            continue


while run == True:

    #23,975,513,184,784,943,783
    print("Enter a number, like 23975513184784943783")

    userInput = input()

    if userInput == "ok":
        userInput = 23975513184784943783
        
    try:
        x = abs(int(userInput))
        if int(userInput) == 0 or int(userInput) == 1:
            print("Not a valid number")
            continue
    except:
        print("Not a valid number")
        continue
    
        
    print("Thinking...")
    
    xSqrt = int(x ** 0.5)

    prime = True
    i = 3
    divisibleBy = int()

    if x != 2 and x % 2 == 0:
        prime = False
        divisibleBy = 2
    else:
        while prime is True and i <= xSqrt:
            # print("Test: " + str(int((i - 1) / 2)))
            if x % i == 0:
                prime = False
                divisibleBy = i
            i += 2

    if prime is True:
        print(str(x) + " is a prime!")
        restartProgram()
    else:
        print(str(x) + " is divisible by " + str(divisibleBy))
        print("Tested " + str(int((i - 1) / 2)) + " times.")
        restartProgram()
