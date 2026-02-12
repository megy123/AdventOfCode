# Advent of Code - Day 8

input_file = open('input', 'r')
input = []

for line in input_file:
    input.append([int(i) for i in line.strip().split(",")])

# Part 1
result = 0

for i in range(len(input)):
    for j in range(len(input)):
        if i == j:
            continue
        
        a = input[i]
        b = input[j]
        rect = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if rect > result:
            result = rect

print(result)

# Part 2

result = 0

for i in range(len(input)):
    for j in range(len(input)):
        if i == j:
            continue
        
        a = input[i]
        b = input[j]
        rect = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if rect > result:
                                
                    
            result = rect
            # TODO

print(result)