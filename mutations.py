def mutate_string(string, position, character):
    string = list(string)

    string[position] = character

    string_return = ''.join(string)

    return string_return


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
