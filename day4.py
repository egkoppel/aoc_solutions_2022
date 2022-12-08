sample_data = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

sample = False

input = (sample_data if sample else open(__file__.split(".")[0] + ".txt", "r").read()).strip()
input = [[
	set(range(*(tuple(
		int(k) + a for k, a in zip(j.split("-"), [0, 1])
	))))
	for j in a.split(",")] for a in input.splitlines()]


def part1():
	global input
	y = [(len(c := (b[0] & b[1])) == len(b[0]), len(c) == len(b[1])) for b in input]
	y = sum(a[0] or a[1] for a in y)
	return y


def part2():
	global input
	y = sum(len(b[0] & b[1]) > 0 for b in input)
	return y


print(f"part 1: {part1()}\npart 2: {part2()}")
