# AdventOfCode 2015 Day 9
import sys

# Read input data

data = []
cities = []

with open("input") as f:
    for line in f:
        tmp = line.split(" = ")
        tmp_2 = tmp[0].split(" to ")
        
        data.append([tmp_2, int(tmp[1].strip())])

for d in data:
    for city in d[0]:
        if not city in cities:
            cities.append(city)

print(cities)
# 8! = 40,320. Possible using conventional alg.

# Part 1

def get_dist(a, b) -> int:
    for pair, dist in data:
        if a in pair and b in pair:
            return dist

def calc_rec(current, cities) -> int:
    if cities == []:
        return 0

    local_dist = []

    for city in cities:
        remaining = [c for c in cities if c != city]

        dist = get_dist(current, city)
        dist += calc_rec(city, remaining)

        local_dist.append(dist)

    return min(local_dist)

results = []

for city in cities:
    remaining = [c for c in cities if c != city]
    results.append(calc_rec(city, remaining))

print(min(results))

# Part 2

def calc_rec(current, cities) -> int:
    if cities == []:
        return 0

    local_dist = []

    for city in cities:
        remaining = [c for c in cities if c != city]

        dist = get_dist(current, city)
        dist += calc_rec(city, remaining)

        local_dist.append(dist)

    return max(local_dist)

results = []

for city in cities:
    remaining = [c for c in cities if c != city]
    results.append(calc_rec(city, remaining))

print(max(results))