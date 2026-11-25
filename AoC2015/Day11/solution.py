# AdventOfCode 2015 Day 11

# Read input data

data = ""

with open("input") as f:
    data = f.readline().strip()

# Part 1

password = list(data)

def recIncPass(password, x):
    flag = False
    
    if x == -1:
        if password[x] == 'z':
            flag = True
            password[x] = 'a'
        else:
            password[x] = chr(ord(password[x]) + 1)
        return password, flag
    else:
        password, flag = recIncPass(password, x+1)
        if flag:
            if password[x] == 'z':
                flag = True
                password[x] = 'a'
            else:
                password[x] = chr(ord(password[x]) + 1)
                flag = False
        return password, flag
    
    

def incPassword(password):
    out, _ = recIncPass(password, -len(password))
    return out
    
flag = False
while not flag:
    password = incPassword(password)
    
    cond1 = False
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 and ord(password[i]) == ord(password[i + 2]) - 2:
            cond1 = True
            break
    
    cond2 = False
    if not any(char in password for char in ['i', 'o', 'l']):
        cond2 = True
    
    cond3 = False
    cond3_cnt = 0
    i = 1
    while i < len(password):
        if password[i] == password[i-1]:
            cond3_cnt += 1
            i += 2
        else:
            i += 1
        
    if cond3_cnt >= 2:
        cond3 = True
        
    flag = cond1 and cond2 and cond3

print("".join(password))

# Part 2

flag = False
while not flag:
    password = incPassword(password)
    
    cond1 = False
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 and ord(password[i]) == ord(password[i + 2]) - 2:
            cond1 = True
            break
    
    cond2 = False
    if not any(char in password for char in ['i', 'o', 'l']):
        cond2 = True
    
    cond3 = False
    cond3_cnt = 0
    i = 1
    while i < len(password):
        if password[i] == password[i-1]:
            cond3_cnt += 1
            i += 2
        else:
            i += 1
        
    if cond3_cnt >= 2:
        cond3 = True
        
    flag = cond1 and cond2 and cond3

print("".join(password))