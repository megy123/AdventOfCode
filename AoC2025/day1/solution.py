# Advent of Code - Day 1

# Part 1
input_file = open('input', 'r')
formateed_input = []

for line in input_file:
    record = [line[0], int(line.strip()[1:])]
    formateed_input.append(record)

init_state = 50
password = 0

for record in formateed_input:
    if record[0] == 'R':
        init_state += record[1] % 100
        init_state %= 100
    else:
        init_state -= record[1] % 100
        if init_state < 0:
            init_state += 100
        
    
    # Update password
    if init_state == 0:
        password += 1
        
print("Part 1 solution:", password)

# Part 2

password = 0
init_state = 50

for record in formateed_input:
    if record[0] == 'R':
        for _ in range(record[1]):
            init_state += 1
            if init_state >= 100:
                init_state = 0
            if init_state == 0:
                password += 1  
    else:
        for _ in range(record[1]):
            init_state -= 1
            if init_state < 0:
                init_state = 99
            if init_state == 0:
                password += 1
            
print("Part 2 solution:", password)