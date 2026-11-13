# AdventOfCode 2015 Day 5
import hashlib

# Read input data

VOWELS =['a', 'e', 'i', 'o', 'u']
RESTRICTED = ["ab", "cd", "pq", "xy"]

data = []

with open("input") as f:
    data = f.readlines()
    
# Part 1

counter = 0

for word in data:
    
    #Check vowels
    
    vowel_cnt = 0
    for l in word:
        if l in VOWELS:
            vowel_cnt += 1
    if vowel_cnt < 3:
        continue
    
    # Check double char
    
    flag = False
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            flag = True
    if(flag == False):
        continue
    
    # Check restricted
    
    flag = False
    for res in RESTRICTED:
        if word.count(res):
            flag = True
    if flag:
        continue
    
    counter += 1

print(counter)
        

# Part 2

counter = 0

for word in data:
    
    flag = True
    for i in range(1, len(word)-1):
        if(word[i-1] == word[i+1]):
            flag = False
    if flag:
        continue
    
    flag = False
    for i in range(len(word)-1):
        if word.count(word[i:i+2]) > 1:
            flag = True
    if(flag == False):
        continue
    
    counter += 1

print(counter)
