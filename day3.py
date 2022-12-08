import string

sample_data = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

sample = False

input = (sample_data if sample else open(__file__.split(".")[0] + ".txt", "r").read()).strip()
input = [([a for a in l[:len(l) // 2]], [a for a in l[len(l) // 2:]]) for l in input.splitlines()]

priorities = {a: b for a, b in zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))}


def part1():
    return sum([[priorities[a] for a in i[0] if a in i[1]][0] for i in input])


def part2():
    global input
    a = [(set(a + b)) for a, b in input]
    a = [a[c] & a[c + 1] & a[c + 2] for c in range(0, len(a), 3)]
    return sum([priorities[list(b)[0]] for b in a])


print(f"part 1: {part1()}\npart 2: {part2()}")
