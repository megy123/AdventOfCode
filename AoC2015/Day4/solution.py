import hashlib

# Read input data

data = []

with open("input") as f:
    data = f.read().strip()
    
# Part 1

counter = 0
result = ""
constructed = ""

while True:
    constructed = data + str(counter)
    result = hashlib.md5(constructed.encode()).hexdigest()
    
    if(result.startswith("00000")):
        break
    
    if(counter % 100000 == 0):
        print("Counter: " + str(counter))
    
    counter +=1

print(result, constructed)
print("Result: " + str(counter))

# Part 2

counter = 0
result = ""
constructed = ""

while True:
    constructed = data + str(counter)
    result = hashlib.md5(constructed.encode()).hexdigest()
    
    if(result.startswith("000000")):
        break
    
    if(counter % 100000 == 0):
        print("Counter: " + str(counter))
    
    counter +=1

print(result, constructed)
print("Result: " + str(counter))
