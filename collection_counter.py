from collections import Counter

if __name__ == '__main__':
    x = int(input())
    size_list = input().split()

    size_list = Counter(size_list)

    money_earn = 0
    n = int(input())
    for _ in range(n):
        line = input().split()

        if line[0] in size_list.keys():
            if size_list[line[0]] - 1 >= 0:
                size_list[line[0]] -= 1
                money_earn += int(line[1])
            else:
                continue

    print(money_earn)
