def swap_case(s):
    string = ''
    for i in s:
        if i.isupper():
            string += i.lower()
        elif i.islower():
            string += i.upper()
        else:
            string += i
    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
