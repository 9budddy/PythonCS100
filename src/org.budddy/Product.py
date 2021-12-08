def product():
    print("Product of two numbers!")
    print("Please enter the First number")
    firstNumber = input()
    print("Please enter the Second number")
    secondNumber = input()
    print("Your product of " + firstNumber + "*" + secondNumber + " is " + str(int(firstNumber)*int(secondNumber)))

product()