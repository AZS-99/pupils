def sample_input():
    x = float(input("Number of daytime minutes? "))
    y = float(input("Number of evening time minutes? "))
    z = float(input("Number of weekend minutes? "))
    total_price_plan_a = 0
    total_price_plan_b = 0
    if x > 100:
        total_price_plan_a += (x - 100) * 25

    total_price_plan_a += y * 15

    total_price_plan_a += z * 20

    if x > 250:
        total_price_plan_b += (x-250) * 25

    total_price_plan_b += y * 35

    total_price_plan_b += z * 25

    print("Plan A costs", total_price_plan_a)
    print("Plan B costs", total_price_plan_b)

    if total_price_plan_a < total_price_plan_b :
        print("Plan A is the chespest")
    elif total_price_plan_a > total_price_plan_b:
        print("Plan B is the cheapest")
    else:
        print("Plan A and Plan B are the same price")



