# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())

    arr = []
    for _ in range(n):
        line = input().split()
        arr.append(line)

    for i in arr:
        try:
            print(int(int(i[0]) / int(i[1])))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code: " + str(e))
