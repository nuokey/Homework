a = input().split("student_")[1:]

# print(a)
l = []
for i in a:
    l.append([int(i[3:]), int(i[:3])])

ls = sorted(l)
m = max(ls)
print(m[1])