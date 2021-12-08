def countdown():
    print("Please enter any number")
    num = int(input())
    while num >= 0:
        print(str(num))
        num -= 1
    print("We finished! Yay!")

countdown()