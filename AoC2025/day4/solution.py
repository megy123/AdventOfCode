# Advent of Code - Day 4


input_file = open('input', 'r')
input = []

for line in input_file:
    input.append(list(line.strip()))    # CHANGED: string -> list of chars

# Part 1

def count_neighbours(y, x, grid):
    neighbours = 0

    # Upper row
    if x-1 >= 0 and y-1 >= 0 and grid[y-1][x-1] == '@':
        neighbours += 1
    if y-1 >= 0 and grid[y-1][x] == '@':
        neighbours += 1
    if x+1 < len(grid[y]) and y-1 >= 0 and grid[y-1][x+1] == '@':
        neighbours += 1

    # Same row
    if x-1 >= 0 and grid[y][x-1] == '@':
        neighbours += 1
    if x+1 < len(grid[y]) and grid[y][x+1] == '@':
        neighbours += 1

    # Lower row
    if x-1 >= 0 and y+1 < len(grid) and grid[y+1][x-1] == '@':
        neighbours += 1
    if y+1 < len(grid) and grid[y+1][x] == '@':
        neighbours += 1
    if x+1 < len(grid[y]) and y+1 < len(grid) and grid[y+1][x+1] == '@':
        neighbours += 1

    return neighbours

result = 0

for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] != '@':
            continue
        if count_neighbours(y, x, input) < 4:
            result += 1

print(result)


# Part 2

grid = [row[:] for row in input]
result = 0
flag = True

while flag:
    flag = False
    to_remove = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '@':
                continue

            neighbours = count_neighbours(y, x, grid)

            if neighbours < 4:
                to_remove.append((y, x))
                flag = True

    for y, x in to_remove:
        grid[y][x] = '.'

    result += len(to_remove)

print(result)
