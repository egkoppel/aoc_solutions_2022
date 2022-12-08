sample_data = '''A Y
B X
C Z'''

sample = False

input = (sample_data if sample else open(__file__.split(".")[0] + ".txt", "r").read()).strip()
input = [(i[0], i[2]) for i in input.splitlines()]

shapes = {'X': 1, 'Y': 2, 'Z': 3}

def total_score(round_data):
    shape_score = shapes[round_data[1]]
    if round_data[0] == 'A':
        if round_data[1] == 'X':
            return shape_score + 3
        elif round_data[1] == 'Y':
            return shape_score + 6
        else:
            return shape_score
    elif round_data[0] == 'B':
        if round_data[1] == 'X':
            return shape_score + 0
        elif round_data[1] == 'Y':
            return shape_score + 3
        else:
            return shape_score + 6
    else:
        if round_data[1] == 'X':
            return shape_score + 6
        elif round_data[1] == 'Y':
            return shape_score + 0
        else:
            return shape_score + 3

conversions = {
    'A' : { 'X': 'Z', 'Y': 'X', 'Z': 'Y' },
    'B' : { 'X': 'X', 'Y': 'Y', 'Z': 'Z' },
    'C' : { 'X': 'Y', 'Y': 'Z', 'Z': 'X' }
}

def convert(theirs, yours):
    return conversions[theirs][yours]

def part1():
    return sum(total_score(i) for i in input)

def part2():
    return sum(total_score((i[0], convert(*i))) for i in input)

print(f"part 1: {part1()}\npart 2: {part2()}")