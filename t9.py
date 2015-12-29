import sys, re
from itertools import permutations

#last try was brutally unsuccessfull, let's try again

#brute force, this time

nodes = []

paths = {}

for line in open(sys.argv[1]).readlines():
	source, destination, distance = re.match(r'(.*) to (.*) = (.*)', line).group(1,2,3)

	if source not in nodes:
		nodes.append(source)
	if destination not in nodes:
		nodes.append(destination)

	paths.setdefault(source,dict())[destination] = int(distance)
	paths.setdefault(destination, dict())[source] = int(distance)

shortest = 999 #big number. FU sys.maxsize
longest = 0

	#python <3
for items in permutations(nodes):
	distance = sum(map(lambda x, y: paths[x][y], items[:-1], items[1:]))
	print distance
	shortest = min(shortest, distance)
	longest = max(longest, distance)

print "Shortest: " + str(shortest)

print "Longest: " + str(longest)

