sample_data = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

sample = False

input = (sample_data if sample else open(__file__.split(".")[0] + ".txt", "r").read()).strip()
input = [[int(k) for k in i.split("\n")] for i in input.split("\n\n")]
sums = list(map(sum, input))
sums.sort()

def part1():
    return sums[-1]

def part2():
    return sum(sums[-3:])

print(f"part 1: {part1()}\npart 2: {part2()}")