# Advent of Code - Day 7

inpurt_file = open("input", 'r')
input = []

for line in inpurt_file:
    input.append(line.strip())
    
input = [list(row) for row in input]
input2 = [row.copy() for row in input]
DEPTH = len(input) - 1

Start = 0

while True:
    if input[0][Start] == 'S':
        break
    Start += 1
    
# Part 1

Splits = 0

def beam(x, y):
    global Splits
    if input[y][x] == '|':
        return
    while y < DEPTH and (input[y][x] == '.'):
        if input[y][x] == 'P' or input[y][x] == '|':
            return
        y += 1
    if input[y][x] == '^':
        Splits += 1
        input[y][x] = 'P'
        beam(x + 1, y)
        beam(x - 1, y)
        

beam(Start, 1)
print(Splits)

# Part 2

result = 0
memo = {}

def beam_q(x, y):
    if (x, y) in memo:
        return memo[(x, y)]

    curr_x = x
    curr_y = y

    while curr_y < DEPTH and input2[curr_y][curr_x] == '.':
        curr_y += 1
    
    if curr_y == DEPTH:
        return 1

    total = 0
    if input2[curr_y][curr_x] == '^':
        total += beam_q(curr_x - 1, curr_y)
        total += beam_q(curr_x + 1, curr_y)
    
    memo[(x, y)] = total
    return total

result = beam_q(Start, 1)
print(result)