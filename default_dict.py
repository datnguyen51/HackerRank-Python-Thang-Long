# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n, m = input().split()
    # m = int(input().split())
    arr_n = []
    for i in range(int(n)):
        data = str(input())
        arr_n.append(data)

    arr_m = []
    for i in range(int(m)):
        data = str(input())
        arr_m.append(data)

    for i in range(len(arr_m)):
        string = ''
        if arr_m[i] not in arr_n:
            string += '-1 '
        else:
            for j in range(len(arr_n)):
                if arr_m[i] == arr_n[j]:
                    string += str(j+1) + ' '
        print(string)
