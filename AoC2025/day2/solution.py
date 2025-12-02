# Advent of Code - Day 2

input_file = open('input', 'r')
input_data = input_file.readline().strip()
input_file.close()

input_data = input_data.split(",")
input = []

for i in input_data:
    temp = i.split("-")
    input.append([int(temp[0]), int(temp[1])])
    
# Part 1    

result = 0
for i in input:
    for j in range(i[0], i[1] + 1):
        if len(str(j)) < 2:
            continue
        if len(str(j)) % 2 == 0:
            tmp_j = str(j)
            part1 = tmp_j[0:len(tmp_j)//2]
            part2 = tmp_j[len(tmp_j)//2:len(tmp_j)]
            if str(part1) == str(part2):
                result += j
            
print(result)

# Part 2

result = 0
for i in input:
    for j in range(i[0], i[1] + 1):
        if len(str(j)) < 2: # exclude one digit nums
            continue
        for prefix_len in range(len(str(j))//2):
            j_str = str(j)
            prefix = j_str[0:prefix_len+1]
            p_index = 0
            flag = True
            
            for k in range(len(j_str)):
                if j_str[k] == prefix[p_index]: # match prefix char with current char
                    p_index += 1
                else:
                    flag = False
                    break
                if p_index == len(prefix): # reset prefix index
                    p_index = 0
            
            if flag and p_index == 0:
                result += j
                break
            
print(result)