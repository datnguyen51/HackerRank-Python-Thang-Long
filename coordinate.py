# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase

if __name__ == '__main__':
    r = input()

    r = complex(r)

    print(abs(r))
    print(phase(r))
