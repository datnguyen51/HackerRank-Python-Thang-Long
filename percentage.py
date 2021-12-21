if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    arr_score_student_query = student_marks[query_name]

    average_score = sum(arr_score_student_query)/len(arr_score_student_query)

    print(round(average_score, 2))
