def binstr_expan(s):
    for char in s:
        if char != "1" and char != "0":
            print("This is not a binary string: " + s)
            return

    length = len(s) - 1
    currentLength = length
    totalConvert = 0
    while currentLength >= 0:
        exponent = length - currentLength
        binConvert = int(s[currentLength]) * 2 ** exponent
        totalConvert += binConvert
        currentLength -= 1
    print(totalConvert)


binstr_expan("10001")
binstr_expan("10001111")
binstr_expan("11")
binstr_expan("95210")