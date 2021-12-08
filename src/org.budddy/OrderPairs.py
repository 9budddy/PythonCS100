def lessThanOrEqual():
    print("Ordered Pair (# < #)")
    print("Please give the First number!")
    firstNum = input()
    print("Please give the Second number!")
    secondNum = input()

    if firstNum <= secondNum:
        print("Your ordered pair is (" + firstNum + "," + secondNum + ")")
    else:
        print("Your ordered pair is (" + secondNum + "," + firstNum + ")")

lessThanOrEqual()