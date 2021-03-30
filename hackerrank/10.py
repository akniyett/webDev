    n = int(raw_input())
    student_marks = {}
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    sum = sum(student_marks.get(query_name))
    print("{:.2f}".format(sum/len(student_marks.get(query_name))))