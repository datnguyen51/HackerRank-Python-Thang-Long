# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    int_division = a // b
    int_mod = a % b

    arr = []
    arr.append(int_division)
    arr.append(int_mod)

    arr = tuple(arr)

    print(int_division)
    print(int_mod)
    print(arr)
