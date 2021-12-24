# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    # print(a)
    # print(b)
    arr = list(product(a, b))
    s = ''
    for i in arr:
        s += str(i) + ' '
    print(s)
