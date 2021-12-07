def move_sub(line, forward, depth):
    operation, step = line.split()
    if operation == "forward":
        forward += int(step)
    elif operation == "down":
        depth += int(step)
    else:
        depth -= int(step)
    return (forward, depth)


def aim_move_sub(line, aim, forward, depth):
    operation, step = line.split()
    step = int(step)
    if operation == "forward":
        forward += step
        depth += step * aim
    elif operation == "down":
        aim += step
    else:
        aim -= step
    return (aim, forward, depth)


def position(file):
    forward = 0
    depth = 0
    input = open(file, "r").readlines()
    for line in input:
        forward, depth = move_sub(line, forward, depth)
    # print("Forward: ", forward, ", Depth: ", depth)
    return forward * depth


def aim_position(file):
    forward = 0
    aim = 0
    depth = 0
    input = open(file, "r").readlines()
    for line in input:
        aim, forward, depth = aim_move_sub(line, aim, forward, depth)
    return forward * depth


# print(position("test01.txt"))
print(position("input.txt"))
# print(aim_position("test01.txt"))
print(aim_position("input.txt"))
