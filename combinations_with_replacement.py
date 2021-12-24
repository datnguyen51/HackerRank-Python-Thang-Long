# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    line = input().split()

    number = int(line[1])
    string = combinations_with_replacement(sorted(line[0]), number)

    string_return = list(string)
    # print(string_return)
    # string_return.sort()

    for i in string_return:
        s = ''
        for j in i:
            s += j
        print(s)
