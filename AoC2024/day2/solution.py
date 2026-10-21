
data = []

with open("input", 'r') as f:
    for line in f:
        temp_arr = []
        for item in line.split():
            temp_arr.append(int(item))
        data.append(temp_arr)

# Part 1

result = 0

for item in data:
    valid = True
    current = item[0]
    
    c_type = "none"
    if item[1] < item[0]:
        c_type = 'desc'
    elif item[1] > item[0]:
        c_type = 'inc'
    else:
        continue
    
    for i in range(1, len(item)):
        if abs(item[i-1] - item[i]) > 3 or abs(item[i-1] - item[i]) < 1:
            valid = False
            break
        
        if c_type == 'inc' and item[i-1] >= item[i]:
            valid = False
            break
        if c_type == 'desc' and item[i-1] <= item[i]:
            valid = False
            break
    if valid == True:
        result +=1
        

print("Part 1: " + str(result))

# Part 2

result = 0

for item in data:
    valid = True
    error = -1
    current = item[0]
    
    c_type = "none"
    if item[1] < item[0]:
        c_type = 'desc'
    elif item[1] > item[0]:
        c_type = 'inc'
    else:
        continue
    
    for i in range(1, len(item)):
        if abs(item[i-1] - item[i]) > 3 or abs(item[i-1] - item[i]) < 1:
            valid = False
            break
        
        if c_type == 'inc' and item[i-1] >= item[i]:
            valid = False
            break
        if c_type == 'desc' and item[i-1] <= item[i]:
            valid = False
            break
    if valid == True:
        result +=1

print("Part 2: " + str(result))