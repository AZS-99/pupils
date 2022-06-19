def is_identical(differences, cycle_len):
    for i in range(cycle_len):
        if differences[i] != differences[cycle_len + i]:
            return False
    return True

def temperature():
    file = open("CCC_2010/J4", "r")
    num = 1
    while num != '0':
        num = file.readline()
        if num != '0':
            temperatures = [int(x) for x in num.split(" ")]
            differences = []
            num_temperatures = temperatures[0]
            temperatures = temperatures[1:]
            for i in range(num_temperatures - 1):
                differences.append(temperatures[i + 1] - temperatures[i])

            flag = True
            for cycle_len in range(1, (len(differences) // 2) + 1):
                if is_identical(differences, cycle_len):
                    print(cycle_len)
                    flag = False
                    break
            if flag: print(len(differences))
