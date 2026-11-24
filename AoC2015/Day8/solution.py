# AdventOfCode 2015 Day 8
import re

# Read input data

data = []

with open("input") as f:
    for line in f:
        data.append(line.strip())
        
# Part 1

result = 0

for line in data:
    tmpLine = line
    tmpLine = re.sub(r'\\x[0-9a-fA-F]{2}', 'x', tmpLine)
    tmpLine = tmpLine.replace(r'\\', 'x')
    tmpLine = tmpLine.replace(r'\"', 'x')
    result += len(line) - len(tmpLine) + 2

print(result)

# Part 2

result = 0

for line in data:
    tmpLine = line
    tmpLine = tmpLine.replace('\\', '\\\\')
    tmpLine = tmpLine.replace('"', '\\"')
    result += len(tmpLine) - len(line) + 2

print(result)