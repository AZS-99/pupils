def loops():
    for i in range(2, 11):
        print(i ** 2)

def loops2():
    i = 2
    while i <= 10:
        print(i**2)

def loop3():
    piggybank = 0
    for i in range(1, 16):
        piggybank += i
    return piggybank

def loop4():
    piggybank = 0
    i = 1
    while i <= 15:
        piggybank += i
        i += 1
    return piggybank