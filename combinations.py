# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    line = input().split()

    number = int(line[1])
    string = []
    for i in range(number):
        string += list(combinations(sorted(line[0]), i+1))

    string_return = string

    for i in string_return:
        s = ''
        for j in i:
            s += j
        print(s)
