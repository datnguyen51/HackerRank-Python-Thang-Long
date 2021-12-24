# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    line = input().split()

    number = int(line[1])
    string = permutations(line[0], number)

    string_return = list(string)
    string_return.sort()

    for i in string_return:
        s = ''
        for j in i:
            s += j
        print(s)
