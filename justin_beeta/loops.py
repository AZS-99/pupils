def power(base, exponent):
    total = 1
    for i in range(exponent):
        total = total * base
    print(total)