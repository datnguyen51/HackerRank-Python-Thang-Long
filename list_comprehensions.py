if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    array_return = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sub_array = []
                sub_array.append(i)
                sub_array.append(j)
                sub_array.append(k)

                if sum(sub_array) != n:
                    array_return.append(sub_array)

    print(array_return)
