# Read input data
data = ""
with open("input") as f:
    data = f.read().strip()

# Part 1

out = 0

for c in data:
    if (c == "("):
        out += 1
    elif (c == ")"):
        out -= 1

print(out)

# Part 2

out = 0
pos = 0

for c in data:
    pos += 1
    
    if (c == "("):
        out += 1
    elif (c == ")"):
        out -= 1
    
    if (out == -1):
        break

print(pos)