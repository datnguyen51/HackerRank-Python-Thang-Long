if __name__ == '__main__':
    N = int(input())

    arr = []
    for _ in range(N):
        line = input().split()
        arr.append(line)

    arr_return = []
    for i in arr:
        if i[0] == 'insert':
            arr_return.insert(int(i[1]), int(i[2]))
        elif i[0] == 'print':
            print(arr_return)
        elif i[0] == 'remove':
            arr_return.remove(int(i[1]))
        elif i[0] == 'append':
            arr_return.append(int(i[1]))
        elif i[0] == 'sort':
            arr_return.sort()
        elif i[0] == 'pop':
            arr_return.pop()
        elif i[0] == 'reverse':
            arr_return.reverse()
