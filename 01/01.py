def increased(file):
    increase_cnt = 0
    input_file = open(file, "r")
    string_list = input_file.read().split()
    int_map = map(int, string_list)
    readings = list(int_map)

    for i in range(1, len(readings)):
        if readings[i] > readings[i - 1]:
            increase_cnt += 1
    input_file.close()
    return increase_cnt


def sliding_window(file):
    increase_cnt = 0
    input_file = open(file, "r")
    string_list = input_file.read().split()
    int_map = map(int, string_list)
    readings = list(int_map)

    for i in range(len(readings) - 3):
        this_window = sum(readings[i : i + 3])
        next_window = sum(readings[i + 1 : i + 4])
        if next_window > this_window:
            increase_cnt += 1
        # print(this_window, next_window, increase_cnt)
    input_file.close()
    return increase_cnt


# print(increased("test01.txt"))
print(increased("input.txt"))
# print(sliding_window("test02.txt"))
print(sliding_window("input.txt"))
