import re


def ev(a):
    a = a.split()
    a = ' '.join([a[0], a[2], a[1]])

    return eval(a)


def f(a):
    try:
        k = 0
        for i in '+-*/':
            k += a.count(i)
        if k == 0:
            return a

        groups = [m.group() for m in re.finditer(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+) [-+]?(?:\d+(?:\.\d*)?|\.\d+) [-+/*]", a)]
        for el in groups:
            a = a.replace(el, str(ev(el)))
        return f(a)
    except Exception:
        return 'Выражение составлено некорректно'


a = input('Введите арифметическое выражение. Числа значения вводятся через пробел  \n')
r = f(a)
print(f(a))
