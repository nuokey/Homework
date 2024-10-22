def one():
    s = input()
    s = s.replace("student_", "", 1)
    s = s.split("student_")

    print(s)

    b = []
    for i in range(len(s)):
        b.append(s[i][3:])

    for i in range(len(s)):
        b.append()

one()

# def two():
