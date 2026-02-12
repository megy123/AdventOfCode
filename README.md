# AdventOfCode

****[Advent of Code](https://adventofcode.com/)*** is an Advent calendar of small programming puzzles for a variety of skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.*

This repository contains my solutions for **Advent of Code**, a yearly coding challenge that runs during December. Each "day" presents a small programming puzzle to solve, usually with two parts, testing algorithmic thinking and problem-solving skills.

## Repository Structure

The code and resources are organized by day inside the `AoC` folder:

```
AoCXXXX/
├─ dayYY/
│ ├─ instructions # Puzzle description for the day
│ ├─ input        # Puzzle input
│ └─ solution.py  # Python solution
├─ dayYY/
│ ├─ instructions
│ ├─ input
│ └─ solution.py
...
└─ dayYY/
├─ instructions
├─ input
└─ solution.py
```

**Notes:**
- Each year(**XXXX**) is stored in a separate folder for better organization.
- Each day(**YY**) has its own folder within the year folder.
- `instructions` contains the puzzle text.
- `input` contains the personalized puzzle input.
- `solution.py` contains my Python solution for that day.

## How to Run Solutions

All solutions are implemented in **Python 3**. To run a specific day's solution:

```
python3 AoC2025/day1/solution.py
```