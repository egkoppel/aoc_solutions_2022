sample_data = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

sample = False

input = (sample_data if sample else open(__file__.split(".")[0] + ".txt", "r").read()).splitlines()
stack_count = (len(input[0]) + 1) // 4

movements = [(int((b := a.split(" "))[1]), int(b[3]) - 1, int(b[5]) - 1) for a in
			 filter(lambda x: x[0] == 'm' if len(x) else False, input)]


def part1():
	global input
	global movements
	stacks = [[] for _ in range(stack_count)]

	for l in filter(lambda x: x[0] != 'm' if len(x) else False, input):
		for i in range(stack_count):
			if l[i * 4 + 1] != ' ' and l[i * 4 + 1].isalpha():
				stacks[i].append(l[i * 4 + 1])

	for count, f, t in movements:
		for i in range(count):
			stacks[t].insert(0, stacks[f].pop(0))
	return "".join([a[0] for a in stacks])


def part2():
	global input
	global movements
	stacks = [[] for _ in range(stack_count)]

	for l in filter(lambda x: x[0] != 'm' if len(x) else False, input):
		for i in range(stack_count):
			if l[i * 4 + 1] != ' ' and l[i * 4 + 1].isalpha():
				stacks[i].append(l[i * 4 + 1])

	for count, f, t in movements:
		stacks[t] = stacks[f][0:count] + stacks[t]
		del stacks[f][0:count]
	return "".join([a[0] for a in stacks])


print(f"part 1: {part1()}\npart 2: {part2()}")
