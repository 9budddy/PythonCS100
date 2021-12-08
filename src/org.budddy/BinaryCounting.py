def binstr_count(s):
    for char in s:
        if char != "1" and char != "0":
            print("This is not a binary string: " + s)
            return

    while "0" in s:

        q = list(s)
        q.reverse()

        length = len(q) - 1

        i = 0
        remainder = 1
        while i <= length:
            num = int(q[i]) + remainder
            if num == 2:
                remainder = 1
                q[i] = str(0)
            else:
                remainder = 0
                q[i] = str(num)

            i += 1
        q.reverse()
        s = "".join(q)
        print(s)

binstr_count("0000")
