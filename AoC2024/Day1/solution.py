
list_a = []
list_b = []

with open("input", 'r') as file:
    for line in file:
        nums = line.replace("   ", ",").split(",")
        list_a.append(int(nums[0]))
        list_b.append(int(nums[1]))
        
# Part 1

list_a.sort()
list_b.sort()
result = 0

for i in range(len(list_a)):
    result += abs(list_a[i] - list_b[i])
    
print("Part 1: " + str(result))    

# Part 2

occurrence_dict = {}

for item in list_b:
    if occurrence_dict.get(item) == None:
        occurrence_dict[item] = 1
    else:
        occurrence_dict[item] += 1
    
result = 0

for item in list_a:
    if occurrence_dict.get(item) != None:
        result += item * occurrence_dict[item]
    
print("Part 2: " + str(result))
