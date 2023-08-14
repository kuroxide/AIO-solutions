#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

# N is the number of meals.
N = None

# K is the minimum distance between hippos.
K = None

# D contains the locations of the meals.
D = []

# Open the input and output files.
input_file = open("distin.txt", "r")
output_file = open("distout.txt", "w")

# Read the value of N and K.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())

# Read the locations of the meals.
for i in range(0, N):
	D.append(int(input_file.readline().strip()))

D = sorted(D)
print(D)

answer = 1
prevNumber = D[0]

for i in D:
	if i - prevNumber >= K:
		answer += 1
		prevNumber = i
	else:
		pass

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
