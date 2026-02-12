# Advent of Code 2025 - Day 10

input_file = open("input", "r")
input = []

for line in input_file:
    parts = line.strip().split(" ")
    part1 = parts[0].replace("[", "").replace("]", "")
    part2 = [i.replace("(", "").replace(")", "") for i in parts[1:-1]]    
    part3 = parts[-1].replace("{", "").replace("}", "")
    element = []
    element.append(part1)
    element.append(part2)
    element.append(part3)
    input.append(element)

# part 1 
result = 0

for element in input:
    core = '.' * len(element[0])
    
    sol = element[0]
    used = []
    used.append(core)
    
    bfs_queue = []
    
    for part in element[1]:
        bfs_queue.append([core, part, 0])
        
    while len(bfs_queue) > 0:
        current = bfs_queue.pop(0)
        current_core = current[0]
        current_part = current[1]
        current_cnt = current[2]
        #print(current_core, current_part, current_cnt)
        
        if current_core in used:
            continue

        if current_core == sol:
            result += current_cnt
            continue

        for i in current_part:
            new_core = current_core[:]
            
            for j in i:
                if(j == ','):
                    continue
                if new_core[int(j)] == '.':
                    new_core = new_core[:int(j)] + '#' + new_core[int(j) + 1:]
                else:
                    new_core = new_core[:int(j)] + '.' + new_core[int(j) + 1:]

            if not new_core in used:
                used.append(new_core)
            else:
                for part in element[1]:
                    bfs_queue.append([new_core, part, current_cnt + 1])

print(result)


                    
        
        
    

