from os import read


def load_input_file(filename):
    file = open(filename, "r")
    return file.read().split()


def diagnostics(filename="input.txt"):
    input = load_input_file(filename)
    epsilon = 0
    gamma = 0
    for bit in range(len(input[0])):
        ones = 0
        zeroes = 0
        for i in input:
            if int(i[bit]) == 1:
                ones += 1
            else:
                zeroes += 1
        if ones > zeroes:
            gamma = ((gamma << 1) + 1)
        else:
            gamma = gamma << 1
    epsilon = gamma ^ (2 ** len(input[0]) - 1)
    return gamma * epsilon


def most_common(bits_on_index, precedence):
    res = {}
    for i in bits_on_index:
        res[i] = res.get(i, 0) + 1
    if res[0] > res[1]:
        return 0
    # if res[1] > res[0]:
    return 1
    # return precedence


def bitlist(l):
    return [int(n) for n in l]


def rating(readings, precedence, length):
    for i in range(length):
        if len(readings) == 1:
            break
        mc = most_common([x[i] for x in readings.values()], precedence)
        if precedence:
            readings = {x: readings[x]
                        for x in readings if readings[x][i] == mc}
        else:
            readings = {x: readings[x]
                        for x in readings if readings[x][i] != mc}
        # print(readings)
    return list(readings.keys())[0]


def life_support(filename="input.txt"):
    input = load_input_file(filename)
    num_list = list(map(lambda x: int(x, 2), input))
    bit_list = list(map(bitlist, input))
    readings = {num_list[i]: bit_list[i] for i in range(len(num_list))}
    # rating(readings.copy(), 1, len(input[0]))
    return rating(readings.copy(), 1, len(input[0])) * rating(readings.copy(), 0, len(input[0]))


# print(diagnostics("test01.txt"))
# print(diagnostics())
# print(life_support("test01.txt"))
print(life_support())
