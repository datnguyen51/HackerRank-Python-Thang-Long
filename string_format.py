def print_formatted(number):
    # your code goes here
    for i in range(number):
        octa = oct(i+1)[2:]
        hexa = hex(i+1)[2:]
        bina = '{0:b}'.format(i+1)

        space = len('{0:b}'.format(number))
        # print(space)
        print(' '*(space-len(str(i+1))) + str(i+1) + ' '*(space-len(octa)+1) + octa + ' '*(space -
              len(hexa)+1) + hexa.upper() + ' '*(space-len(bina)+1) + bina + ' '*(space-len(bina)+1))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
