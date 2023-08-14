#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

# N is the number of notes.
N = None

# K is the largest number which could be a note.
K = None

# S contains the sequence of notes forming the song.
S = []
answer = 0

# Open the input and output files.
input_file = open("melodyin.txt", "r")
output_file = open("melodyout.txt", "w")

# Read the value of N and K.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())

# Read each note in the song.
segmentcounter = 0
segments = []

for i in range(0, N):
    S.append(int(input_file.readline().strip()))
    segmentcounter += 1
    if segmentcounter % 3 == 0:
        segments.append(S)
        S = []

for i in range(3):
    counts = []
    for l in range(K+1):
        counts.append(0)

    for j in range(len(segments)):
        value = segments[j][i]
        counts[value] += 1
    answer += sum(counts) - max(counts)

# Write the answer to the output file.
output_file.write(str(answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
