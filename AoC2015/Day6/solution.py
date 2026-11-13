# AdventOfCode 2015 Day 6
import re

# Read input data

data = []

with open("input") as f:
    data = f.readlines()

# Process input

parsed_data = []

for line in data:
    line = line.strip()
    cords = [int(x) for x in re.findall(r'-?\d+', line)]
    
    if line.startswith("turn on "):
        parsed_data.append((1, (cords[0], cords[1]), (cords[2], cords[3])))
    elif line.startswith("turn off "):
        parsed_data.append((2, (cords[0], cords[1]), (cords[2], cords[3])))
    elif line.startswith("toggle "):
        parsed_data.append((3, (cords[0], cords[1]), (cords[2], cords[3])))
    else:
        print("Invadil Input: ", line)
        exit(1)
        
# Part 1

arr = [False] * 1000 * 1000

for inst in parsed_data:
    for y in range(inst[1][1],inst[2][1]+1):
        for x in range(inst[1][0], inst[2][0]+1):
            if inst[0] == 1:
                arr[y*1000+x] = True
            elif inst[0] == 2:
                arr[y*1000+x] = False
            elif inst[0] == 3:
                arr[y*1000+x] = not arr[y*1000+x]
                
result = sum(arr)
print(result)

# Part 2

arr = [0] * 1000 * 1000

for inst in parsed_data:
    for y in range(inst[1][1],inst[2][1]+1):
        for x in range(inst[1][0], inst[2][0]+1):
            if inst[0] == 1:
                arr[y*1000+x] += 1
            elif inst[0] == 2:
                arr[y*1000+x] -= 1
                if arr[y*1000+x] < 0:
                    arr[y*1000+x] = 0
            elif inst[0] == 3:
                arr[y*1000+x] += 2
                
result = sum(arr)
print(result)
