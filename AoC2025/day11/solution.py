# Advent of Code - Day 11
from collections import deque
import sys

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

sys.setrecursionlimit(2000)
graph = {item[0]: item[1] for item in input}
memo = {}

def count_required_paths(node, visited_dac, visited_fft):
    state = (node, visited_dac, visited_fft)

    # Return conditions
    if node == "out":
        return 1 if (visited_dac and visited_fft) else 0
    if state in memo:
        return memo[state]

    total_paths = 0
    
    # Search graphs
    for nxt in graph.get(node, []):
        new_dac = visited_dac or (nxt == "dac")
        new_fft = visited_fft or (nxt == "fft")
        
        total_paths += count_required_paths(nxt, new_dac, new_fft)
            
    memo[state] = total_paths
    return total_paths

result = count_required_paths("svr", False, False)
print(result)