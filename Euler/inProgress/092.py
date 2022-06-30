def checkSeq(number=0):
    # count = 0
    # number_start = number
    while number!=89 and number!=1:
        number = sum([int(i)*int(i) for i in str(number)])
        # count += 1
    return number

print([checkSeq(i) for i in range(1, 1000)])