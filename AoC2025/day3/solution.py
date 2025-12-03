# Advent of Code - Day 1

input_file = open("input", 'r')
input = []

for line in input_file:
    input.append(str(line.strip()))

# Part 1
result = 0

for l in input:
    line_max = 0
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if i == j:
                continue
            num = int(l[i]) * 10 + int(l[j])
            if num > line_max:
                line_max = num
    result += line_max
    
print(result)

# Part 2

result = 0

for l in input:
    partial = []
    rem_digits = 12
    last_idx = -1
    
    while rem_digits > 0:
        line_max = 0
        
        for i in range(last_idx+1, len(l)-rem_digits+1):
            if int(l[i]) > line_max:
                line_max = int(l[i])
                last_idx = i
            if line_max == 9:
                break
            
        partial.append(str(line_max))
        rem_digits -= 1
    
    result += int(''.join(partial))
                
    
print(result)