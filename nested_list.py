if __name__ == '__main__':
    arr_class = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        arr_student = []
        arr_student.append(name)
        arr_student.append(score)

        arr_class.append(arr_student)

    def myFunc(e):
        return e[1]

    arr_class.sort(key=myFunc)

    score = arr_class[0][1]

    arr_name_student = []
    for i in arr_class:
        if i[1] > score:
            score = i[1]
            break

    for i in arr_class:
        if i[1] == score:
            arr_name_student.append(i[0])

    arr_name_student.sort()
    for i in arr_name_student:
        print(i)
