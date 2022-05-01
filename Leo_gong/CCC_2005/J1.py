def cell_sell():
    daytime = int(input("Number of daytime minutes?"))
    evening = int(input("Number of evening minutes?"))
    weekend = int(input("Number of weekend minutes?"))

    # if daytime_a > 0:
    #     int(daytime_a) * 25
    # if daytime_b > 0:
    #     int(daytime_b) * 45

    evening_weekend_cost_a = evening * 15 + weekend * 20
    evening_weekend_cost_b = evening * 35 + weekend * 25
    daytime_a = daytime - 100
    daytime_b = daytime - 250

    a = daytime_a * 25
    b = daytime_b * 45

    print("Plan A costs", a)
    print("Plan B costs", b)
    print()