if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    arr.sort()

    max_score = arr[len(arr)-1]
    for i in reversed(arr):
        if i < max_score:
            print(i)
            break
