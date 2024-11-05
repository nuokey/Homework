l = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
L = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"

a = open("input.txt").read()
def sipher(a):
    b = ""
    for i in range(len(a)):
        if a[i] in l or a[i] in L:
            try:
                b += l[len(l)-l.index(a[i])-1]
            except Exception:
                b += L[len(L)-L.index(a[i])-1]
        else:
            b += a[i]

    return b

print()
print(sipher(a))
# print(sipher(sipher(a)))