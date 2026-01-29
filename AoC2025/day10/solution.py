# Advent of Code - Day 10
import copy
import collections

inpurt_file = open("input", 'r')
input = []

for line in inpurt_file:
    parsed_line = line.strip().replace("[", "").replace("]", "").replace(")", "").replace("(", "").replace("{", "").replace("}", "").split(" ")

    input_p_1 = [ c == '#' for c in parsed_line[0] ]
    input_p_2 = [[int(x) for x in row.split(",")] for row in parsed_line[1:-1]]
    input_p_3 = [ int(c) for c in parsed_line[-1].split(",") ]
    constructed_input = [input_p_1, input_p_2, input_p_3]
    input.append(constructed_input)
    break

# Part 1

result = 0

for exc in input:
    op_log = []
    op_sst = collections.deque()
    op_sst.append([[], exc[0]])
    choices = exc[1]
    flag = True
    while len(op_sst) != 0 and flag == True:
        current = op_sst.popleft()

        for x in choices:
            tmp_cur = [current[0][:], current[1][:]]

            # Update actions
            tmp_cur[0].append(choices.index(x))            

            # Create new state
            for i in x:
                tmp_cur[1][i] = not tmp_cur[1][i]
            
            # No duplicite states
            if tmp_cur[1] in op_log:
                continue

            # Check if correct
            if not any(tmp_cur[1]):
                #print(tmp_cur[0], "BINGO")
                result += len(tmp_cur[0])
                flag = False
                break
            
            op_log.append(tmp_cur[1])
            op_sst.append(tmp_cur)

print(result)

# Part 2