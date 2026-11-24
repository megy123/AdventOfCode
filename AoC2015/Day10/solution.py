# AdventOfCode 2015 Day 10

# Read input data

ITERATIONS = 40
data = ""

with open("input") as f:
    data = f.readline().strip()

# Part 1

def lookAndSay(iterations, data):
    result = data

    for i in range(iterations):
        newResult = ""
        
        current = result[0]
        counter = 0
        for c in result:
            if current != c:
                newResult += str(counter) + current
                counter = 1
                current = c
            else:
                counter += 1
                
        newResult += str(counter) + current
        result = newResult
        
    return result
    
print(len(lookAndSay(ITERATIONS, data)))


# Part 2

print(len(lookAndSay(50, data)))