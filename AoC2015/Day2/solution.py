# Read input data

data = []

with open("input") as f:
    data = f.read().splitlines()
    
# Part 1

result = 0

for line in data:
    dimensions = line.split("x")
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    
    result += 2*l*w + 2*l*h + 2*w*h + min(l * w, l * h, h * w)
    
print(result)

# Part 2

result = 0

for line in data:
    dimensions = line.split("x")
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    
    result += l*w*h + min(2*(l+w), 2*(l+h), 2*(h+w))
    
print(result)