def is_binstr(s):
    for char in s:
        if char != "1" and char != "0":
            print("This is not a binary string: " + s)
            return

    print("This is a binary string: " + s)


is_binstr("101010111")
is_binstr("15101410")
is_binstr("99428192")
is_binstr("000000000")
is_binstr("11111111")
