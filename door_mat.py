# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = map(int, input().split())

    c = '.|.'
    w = 'WELCOME'

    for i in range(int((n-1)/2)):
        print((c*i).rjust(int((m-3)/2), '-')+c+(c*i).ljust(int((m-3)/2), '-'))

    print(w.center(int(m), '-'))

    for i in range(int((n-1)/2)):
        print((c*(int((n-1)/2)-i-1)).rjust(int((m-3)/2), '-') +
              c + (c*(int((n-1)/2)-i-1)).ljust(int((m-3)/2), '-'))
