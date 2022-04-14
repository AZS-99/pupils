def price_plan():
    day_time = int(input("Number of daytime minutes?"))
    evening_time = int(input("Number of evening minutes?"))
    weekend_time = int(input("Number of weekend minutes?"))

    plan_a = 0
    if day_time > 100:
        plan_a += (day_time - 100) * 25
    plan_a += evening_time * 15
    plan_a += weekend_time * 20

    plan_b = 0
    if day_time > 250:
        plan_b += (day_time - 250) * 45
    plan_b += evening_time * 35
    plan_b += weekend_time * 25

    print("Plan A costs", plan_a)
    print("Plan B costs", plan_b)
    if plan_a > plan_b:
        print("Plan B is cheapest.")
    elif plan_b > plan_a:
        print("Plan A is cheapest.")
    else:
        print("Plan A and plan B are the same price.")



