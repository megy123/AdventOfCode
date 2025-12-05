# Advent of Code - Day 5

input_file = open("input", 'r')

flag = False
input_ranges = []
input_ids = []

for line in input_file:
    if line.strip() == "":
        flag = True
        continue
    if flag:
        input_ids.append(int(line.strip()))
    else:
        tmp = line.strip().split("-")
        input_ranges.append([int(tmp[0]), int(tmp[1])])

# Part 1

result = 0

for id in input_ids:
    for id_range in input_ranges:
        if id_range[0] <= id <= id_range[1]:
            result +=1
            break

print(result)

# Part 2

result = 0

valid_ids = []
for i in range(len(input_ranges)):
    rang = input_ranges[i].copy()
    to_remove = []

    for id in valid_ids:
        if id[0] <= rang[0] and id[1] >= rang[1]:
            #id   |-----------------------|
            #rg         |---------|
            rang = None
            break
        if id[0] >= rang[0] and id[1] <= rang[1]:
            #id         |---------|
            #rg    |--------------------|
            to_remove.append(id)
            continue
        if id[1] < rang[0] or id[0] > rang[1]:
            # no overlap
            continue
        # partial overlaps:
        if id[1] >= rang[0] and id[0] <= rang[0]:
            #id   |---------|
            #rg         |---------|
            rang[0] = id[1] + 1
        if id[0] <= rang[1] and id[1] >= rang[1]:
            #id         |---------|
            #rg    |---------|
            rang[1] = id[0] - 1
        
    for rem in to_remove:
        valid_ids.remove(rem)
    if rang is not None:
        valid_ids.append(rang)

for id in valid_ids:
    result += id[1] - id[0] + 1 
print(result)


