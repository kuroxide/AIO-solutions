import os
import math

with open("vasesin.txt", mode="r") as f:
	contents = int(f.readline())

if contents >= 6:
	answer = [math.floor(contents/3-1), math.floor(contents/3), math.floor(contents/3+1)+(contents % 3)]
else:
	answer = [0,0,0]

with open("vasesout.txt", mode="w") as g:
	text = ''
	for i in answer:
		text = text + str(i) + " "
	text = text[:-1]
	g.write(text)
