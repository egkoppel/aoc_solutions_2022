import pprint

sample_data = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

sample = False

input = (sample_data if sample else open(__file__.split(".")[0] + ".txt", "r").read()).strip().splitlines()

fs = {"/": {"_files": []}}

fs_back_stack = [fs]

for line in input:
	data = line.split(" ")
	if data[0] == "$":
		if data[1] == "cd":
			move_dir = data[2]
			print("move into dir", move_dir)
			if move_dir == "..":
				fs_back_stack.pop()
			else:
				fs_back_stack.append(fs_back_stack[-1][move_dir])
	elif data[0] == "dir":
		new_dir = data[1]
		print("create dir", new_dir)
		new_dir_data = {"_files": []}
		fs_back_stack[-1][new_dir] = new_dir_data
	else:
		sz = int(data[0])
		fname = data[1]
		fs_back_stack[-1]["_files"].append((fname, sz))


def calc_dir_size_recurse(dir_ptr):
	child_file_size = sum(a[1] for a in dir_ptr["_files"])
	child_dir_size = sum(calc_dir_size_recurse(val) for key, val in dir_ptr.items() if not key.startswith("_"))
	sz = child_file_size + child_dir_size
	dir_ptr["_sz"] = sz
	return sz


calc_dir_size_recurse(fs["/"])

pprint.pprint(fs)


def sum_dir_size_below_100k(dir_ptr):
	total = dir_ptr["_sz"] if dir_ptr["_sz"] <= 100000 else 0
	total += sum(sum_dir_size_below_100k(val) for key, val in dir_ptr.items() if not key.startswith("_"))
	return total


def part1():
	return sum_dir_size_below_100k(fs["/"])


def find_dir_size_between(dir_ptr, min_, max_):
	ret = dir_ptr["_sz"] if min_ <= dir_ptr["_sz"] < max_ else max_
	new_max = ret
	try:
		ret = min(find_dir_size_between(val, min_, new_max) for key, val in dir_ptr.items() if not key.startswith("_"))
	except ValueError:
		pass
	return ret


def part2():
	need_to_free = 30000000 - (70000000 - fs["/"]["_sz"])
	return find_dir_size_between(fs["/"], need_to_free, 70000000)


print(f"part 1: {part1()}\npart 2: {part2()}")
