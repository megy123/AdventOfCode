# Advent of Code - Day 11
from collections import deque


innput_file = open("input", "r")
input = []

for line in innput_file:
    record = line.split(":")
    record[1] = record[1].strip().split(" ")
    input.append(record)
    
# Part 1

start = next(item for item in input if item[0] == "you")
result = 0
processed = []
stack = deque()
stack.append(start)

while stack:
    item = stack.pop()
    for follower in item[1]:
        if follower == "out":
            result += 1
        if not follower in processed:
            #processed.append(follower)
            a_item = next((item for item in input if item[0] == follower), None)
            if a_item:
                stack.append(a_item)


print(result)

# Part 2
import sys
# Increase recursion limit for deep DFS/memoization
sys.setrecursionlimit(2000)

# --- Assuming 'input' list of lists is correctly populated from file ---
# This dictionary creation is necessary to use the input data
graph = {item[0]: item[1] for item in input}

# Memoization table: 
# Key: (current_node, visited_dac, visited_fft)
# Value: The count of paths from current_node to "out" 
# satisfying the remaining constraints.
memo = {}

def count_required_paths(node, visited_dac, visited_fft):
    """
    Recursively counts the number of paths from 'node' to 'out' 
    that visit the remaining required nodes.
    """
    # The state for memoization only needs to know the current node 
    # and whether 'dac' and 'fft' have been visited *already*.
    state = (node, visited_dac, visited_fft)
    
    # 1. Base Case: Reached the destination
    if node == "out":
        # Only count this path if both required nodes were visited
        return 1 if (visited_dac and visited_fft) else 0

    # 2. Check Cache
    if state in memo:
        return memo[state]

    # 3. Recurse
    total_paths = 0
    
    # NOTE: We DO NOT track 'path' here to avoid cycles because the 
    # problem implies path enumeration is too complex. If the problem 
    # requires *simple* paths, this approach is technically incorrect 
    # in a general cyclic graph. However, for these puzzles, avoiding 
    # path tracking is usually the intended optimization.
    
    for nxt in graph.get(node, []):
        # Update the constraint flags for the next step
        new_dac = visited_dac or (nxt == "dac")
        new_fft = visited_fft or (nxt == "fft")
        
        # Recursively call and sum the results
        total_paths += count_required_paths(nxt, new_dac, new_fft)
            
    # 4. Store and Return
    memo[state] = total_paths
    return total_paths


# The result for Part 2
result = count_required_paths("svr", False, False)

print(result)