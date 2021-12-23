if __name__ == '__main__':
    s = input()

    data = [False, False, False, False, False]

    for i in s:
        if i.isalnum():
            data[0] = True
        if i.isalpha():
            data[1] = True
        if i.isdigit():
            data[2] = True
        if i.islower():
            data[3] = True
        if i.isupper():
            data[4] = True

    for i in data:
        print(i)
