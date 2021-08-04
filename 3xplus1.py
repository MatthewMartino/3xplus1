def calcsingle():
    steps = 0
    x = int(input("\nEnter a number: "))
    original = x

    print("\nInput was:", x, "\n")

    while x != 1:

        # Check if Number is even
        if x % 2 == 0:
            x = int(x / 2) # Even Equation (Divide X by 2)
            print(x)
            steps += 1

        # Check if Number is odd
        elif x % 2 != 0 and x != 1:
            x = int((x * 3) + 1) # Odd Equation (Multiply by 3 and add 1)
            print(x)
            steps += 1

    print("\n------------------------")
    print("All Done!")
    print("Total steps for", original, "to reach 4,2,1 loop is:", steps, "\n\n")

def calcmultiple():
    steps = 0
    start = int(input("\nWhere does the range start?: "))
    end = int(input("\nAnd where does it end?: "))
    current = start

    x = start

    print("\n")
    while current >= start and current <= end:

        # Check if Number is even
        if x % 2 == 0 and x != 1:
            x = int(x / 2) # Even Equation (Divide X by 2)
            steps += 1

        # Check if Number is odd
        elif x % 2 != 0 and x != 1:
            x = int((x * 3) + 1) # Odd Equation (Multiply by 3 and add 1)
            steps += 1

        # Check if the number is 1
        elif x == 1:
            print("Total steps for", current, "was", steps)
            current += 1
            x = current
            steps = 0

    2
    print("Done Looping!")

def intro():
    valid = False

    while valid == False:
        print("\n1) Calculate a range of numbers\n2) Calculate one number\n3) Exit")
        io = int(input("\nChoose Option: "))

        if io == 1: # Calculate Range
            calcmultiple()

        elif io == 2: # Calculate single number
            calcsingle()

        elif io == 3: # Calculate single number
            print("\nGoodbye!")
            valid = True

        else:
            print("Input not valid, please input a choice again.")

print("------------------------")

intro()