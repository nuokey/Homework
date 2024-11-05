l = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
L = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"

a = open("input.txt").read()
def sipher(a, n):
    b = ""
    for i in range(len(a)):
        if a[i] in l or a[i] in L:
            try:
                b += l[l.index(a[i]) + n]
            except Exception:
                b += L[L.index(a[i]) + n]
        else:
            b += a[i]

    return b

print()
print(sipher(a))
# print(sipher(sipher(a)))