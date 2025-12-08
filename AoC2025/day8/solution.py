# Advent of Code - Day 8

import sys
import math
import numpy as np

MAX_VAL = sys.maxsize * 2 + 1
input_file = open('input', 'r')
input = []

for line in input_file:
    box = line.strip().split(",")
    input.append(box)

# initialize distance matrix
dist_matrix = []

for box_a in range(len(input)):
    d_matrix_row = []
    for box_b in range(len(input)):
        if box_a == box_b:
            d_matrix_row.append(MAX_VAL)
        else:
            a = input[box_a]
            b = input[box_b]
            
            d_matrix_row.append(math.sqrt(
                (int(a[0]) - int(b[0]))**2 +
                (int(a[1]) - int(b[1]))**2 +
                (int(a[2]) - int(b[2]))**2
            ))
    
    dist_matrix.append(d_matrix_row)
    
dist_matrix = np.array(dist_matrix)
# Part 1

result = 0
cnt = 0
circuits = []

while True:
    min_ind = np.unravel_index(np.argmin(dist_matrix, axis=None), dist_matrix.shape)
    #print(min_ind, dist_matrix[min_ind[0]][min_ind[1]])
    
    # termination condition
    if(dist_matrix[min_ind[0]][min_ind[1]] >= MAX_VAL):
        break
    cnt += 1
    if cnt % 1000 == 0:
        print("Iteration:", cnt)
        break
    # process minimum
    dist_matrix[min_ind[0]][min_ind[1]] = MAX_VAL
    dist_matrix[min_ind[1]][min_ind[0]] = MAX_VAL
    
    flag = False
    merge_circuit = None
    for circuit in circuits:
        if min_ind[0] in circuit or min_ind[1] in circuit:
            circuit.add(min_ind[0])
            circuit.add(min_ind[1])
            flag = True
            merge_circuit = circuit
        if (min_ind[0] in circuit or min_ind[1] in circuit) and merge_circuit is not None:
            for item in circuit:
                merge_circuit.add(item)
            circuits.remove(circuit)
    if not flag:
        circuits.append({min_ind[0], min_ind[1]})
    
result = 1

circuits = sorted(circuits, key=len, reverse=True)
for i in range(min(3, len(circuits))):
    result *= circuits[i].__len__()

print(result)