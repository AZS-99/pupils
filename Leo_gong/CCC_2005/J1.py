def cell_sell():
    daytime = int(input("Number of daytime minutes?"))
    evening = int(input("Number of evening minutes?"))
    weekend = int(input("Number of weekend minutes?"))

    a = 0
    b = 0

    if daytime > 100:
        a += (daytime - 100) * 25

    if daytime > 250:
        b += (daytime - 250) * 45
    a += evening * 15 + weekend * 20
    b += evening * 35 + weekend * 25

    print("Plan A costs", (round(a, 2) / 10))
    print("plan B costs", round(b, 2))
    print("Plan A is cheapest." if a < b else "Plan B is cheapest.")