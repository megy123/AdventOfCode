# Advent of Code - Day 6

ROWS = 4
input_file = open('input', 'r')
input = []
input2 = []

for line in input_file:
    input.append(line.strip().split())
    input2.append(line.rstrip('\n'))
    
# Part 1

result = 0

for i in range(len(input[0])):
    operator = input[4][i]
    if operator == '+':
        result += int(input[0][i]) + int(input[1][i]) + int(input[2][i]) + int(input[3][i])
    elif operator == '*':
        result += int(input[0][i]) * int(input[1][i]) * int(input[2][i]) * int(input[3][i])
    
print(result)

# Part 2
def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

input2 = trans(input2)
result = 0

for i in range(len(input2)):
    if input2[i][4] == '+' or input2[i][4] == '*':
        operator = input2[i][4]
        
        if operator == '+':
            partial = 0
            k = 0
            while True:
                partial += int(('0' if input2[i+k][0] == ' ' else input2[i+k][0]) + 
                               ('0' if input2[i+k][1] == ' ' else input2[i+k][1]) + 
                               ('0' if input2[i+k][2] == ' ' else input2[i+k][2]) + 
                               ('0' if input2[i+k][3] == ' ' else input2[i+k][3]))
                if i < 30:
                    print(int(('0' if input2[i+k][0] == ' ' else input2[i+k][0]) + 
                               ('0' if input2[i+k][1] == ' ' else input2[i+k][1]) + 
                               ('0' if input2[i+k][2] == ' ' else input2[i+k][2]) + 
                               ('0' if input2[i+k][3] == ' ' else input2[i+k][3])))
                k+=1
                if i+k == len(input2) or (input2[i+k][4] == '+' or input2[i+k][4] == '*'):
                    if i < 30:
                        print("+:",partial)
                        print("-"*20)
                    result += partial
                    break

        elif operator == '*':
            partial = 1
            k=0
            while True:
                tmp = int(('0' if input2[i+k][0] == ' ' else input2[i+k][0]) + 
                               ('0' if input2[i+k][1] == ' ' else input2[i+k][1]) + 
                               ('0' if input2[i+k][2] == ' ' else input2[i+k][2]) + 
                               ('0' if input2[i+k][3] == ' ' else input2[i+k][3]))
                if input2[i+k][0] != ' ' or input2[i+k][1] != ' ' or input2[i+k][2] != ' ' or input2[i+k][3] != ' ':
                    partial *= tmp
                if i < 30:
                    print(int(('0' if input2[i+k][0] == ' ' else input2[i+k][0]) + 
                               ('0' if input2[i+k][1] == ' ' else input2[i+k][1]) + 
                               ('0' if input2[i+k][2] == ' ' else input2[i+k][2]) + 
                               ('0' if input2[i+k][3] == ' ' else input2[i+k][3])))
                k+=1
                if i+k == len(input2) or (input2[i+k][4] == '+' or input2[i+k][4] == '*'):
                    if i < 30:
                        print("*:",partial)
                        print("-"*20)
                    result += partial
                    break
        
print(result)


