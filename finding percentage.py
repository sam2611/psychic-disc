if __name__ == '__main__':

    n = int(input())
    i=0
    student_marks ={ "name":[],
                     "scores":[]
                    }
    for i in range(n):
        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores

    query_name = input()

    list1 = list(student_marks[query_name])
    avg = sum(list1) / len(list1)
    print(avg)
