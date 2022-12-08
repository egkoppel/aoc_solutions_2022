sample_data = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

sample = False

input = (sample_data if sample else open(__file__.split(".")[0] + ".txt", "r").read()).strip()


def part1():
	global input
	for i in range(4, len(input)):
		chars = input[i - 4:i]
		if len(set(chars)) == 4:
			return i


def part2():
	global input
	for i in range(14, len(input)):
		chars = input[i - 14:i]
		if len(set(chars)) == 14:
			return i


print(f"part 1: {part1()}\npart 2: {part2()}")
