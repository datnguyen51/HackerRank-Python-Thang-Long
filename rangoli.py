letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def print_rangoli(size):
    # your code goes here
    width = (size-1)*2
    half_height = (size-1)

    sub_letter_up = letter[1:size]
    sub_letter_down = letter[1:size]

    sub_letter_center = ''
    letter_center = ''

    ''' Top '''
    while sub_letter_up:
        letter_center = sub_letter_up.pop()
        string = sub_letter_center.rjust(width, '-') + letter_center + sub_letter_center[::-1].ljust(width, '-')
        sub_letter_center += letter_center + '-'
        print(string)

    ''' Center '''
    print(sub_letter_center + letter[0] + sub_letter_center[::-1])

    ''' Bottom '''
    for i in range(half_height):
        data = sub_letter_center[:-2*(i+1)].rjust(width, '-') + sub_letter_down[i] + (sub_letter_center[:-2*(i+1)])[::-1].ljust(width, '-')
        print(data)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
