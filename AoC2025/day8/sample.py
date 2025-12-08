# Advent of Code - Day 8

import sys
import math
import numpy as np

MAX_VAL = sys.maxsize * 2 + 1

# Read input
input_data = []
with open("input", "r") as f:
    for line in f:
        x, y, z = map(int, line.strip().split(","))
        input_data.append((x, y, z))

N = len(input_data)

# Build distance matrix
dist_matrix = np.zeros((N, N), dtype=float)

for i in range(N):
    x1, y1, z1 = input_data[i]
    for j in range(N):
        if i == j:
            dist_matrix[i, j] = MAX_VAL
        else:
            x2, y2, z2 = input_data[j]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            dist_matrix[i, j] = dist

# ---------- PART 1 ----------
circuits = []
connections = 0

# Copy matrix because Part 2 needs a fresh one later
dist_for_part2 = dist_matrix.copy()

while connections < 1000:
    a, b = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)

    if dist_matrix[a, b] >= MAX_VAL:
        break

    # Remove this edge
    dist_matrix[a, b] = MAX_VAL
    dist_matrix[b, a] = MAX_VAL
    connections += 1

    # Find circuits to merge
    found = []
    for i, c in enumerate(circuits):
        if a in c or b in c:
            found.append(i)

    if len(found) == 0:
        circuits.append({a, b})

    elif len(found) == 1:
        circuits[found[0]].update([a, b])

    else:
        base_idx = found[0]
        base = circuits[base_idx]
        base.update([a, b])

        for idx in reversed(found[1:]):
            base.update(circuits[idx])
            del circuits[idx]

# Compute Part 1 result
circuits.sort(key=len, reverse=True)
result1 = 1
for i in range(min(3, len(circuits))):
    result1 *= len(circuits[i])

print("Part 1:", result1)

# ---------- PART 2 ----------
# Reset circuits and matrix
circuits = []
dist_matrix = dist_for_part2.copy()

# We track the last merge that makes everything one circuit
last_a = None
last_b = None

while True:
    a, b = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
    if dist_matrix[a, b] >= MAX_VAL:
        break

    # Remove this pair
    dist_matrix[a, b] = MAX_VAL
    dist_matrix[b, a] = MAX_VAL

    # Merge logic again
    found = []
    for i, c in enumerate(circuits):
        if a in c or b in c:
            found.append(i)

    if len(found) == 0:
        circuits.append({a, b})

    elif len(found) == 1:
        circuits[found[0]].update([a, b])

    else:
        base_idx = found[0]
        base = circuits[base_idx]
        base.update([a, b])

        for idx in reversed(found[1:]):
            base.update(circuits[idx])
            del circuits[idx]

    # After merging, check if all boxes are in one circuit
    if len(circuits) == 1 and len(circuits[0]) == N:
        last_a = a
        last_b = b
        break

# Part 2 answer: multiply X coordinates (index 0 in tuple)
result2 = input_data[last_a][0] * input_data[last_b][0]
print("Part 2:", result2)
