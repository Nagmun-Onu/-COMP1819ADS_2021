def weird_or_not(n):
    if n % 2 != 0 or n in range(10, 30):
        print("Weird")
    elif n in range(2, 9) or n > 30:
        print("Not Weird")


# driver code
weird_or_not(3)
weird_or_not(34)
weird_or_not(2)
weird_or_not(9)
weird_or_not(10)
weird_or_not(30)
weird_or_not(100)
