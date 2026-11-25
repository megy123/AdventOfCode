# AdventOfCode 2015 Day 12
import re
import json

# Read input data

data = []

with open("input") as f:
    data = f.readlines()

# Part 1


def getNumbers(str):
    array = re.findall(r'-?[0-9]+', str)
    return array

numbers = getNumbers(data[0])

result = 0

for number in numbers:
    result += int(number)    

print(result)

# Part 2

def getSum(obj):
    if isinstance(obj, int):
        return obj

    if isinstance(obj, list):
        return sum(map(getSum, obj))

    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0

        return sum(map(getSum, obj.values()))

    return 0

print(getSum(json.loads(data[0])))
