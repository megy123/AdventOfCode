# Read input data

data = []

with open("input") as f:
    data = f.read().strip()
    
# Part 1

visited = [(0, 0)]
x = 0
y = 0

for c in data:
    if (c == "<"):
        x-=1
    elif (c == ">"):
        x+=1
    elif (c == "^"):
        y+= 1
    elif (c == "v"):
        y-=1
    
    if not ((x,y) in visited):
        visited.append((x, y))

print(len(visited))

# Part 2

visited = [(0, 0)]
x = 0
y = 0
r_x = 0
r_y = 0
switch = True

for c in data:
    if (c == "<"):
        if switch:
            x-=1
        else:
            r_x-=1
    elif (c == ">"):
        if switch:
            x+=1
        else:
            r_x+=1
    elif (c == "^"):
        if switch:
            y+= 1
        else:
            r_y+=1
    elif (c == "v"):
        if switch:
            y-=1
        else:
            r_y-=1
    
    if switch:
        if not ((x,y) in visited):
            visited.append((x, y))
    else:
        if not ((r_x,r_y) in visited):
            visited.append((r_x, r_y))

    switch = not switch
    
print(len(visited))