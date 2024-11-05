import re
f = int(input('Если префиксная форма, введите - 1, если постфиксная - 2 \n'))
a = input('Введите арифметическое выражение: \n').replace(' ', '')
Z = {'*':'.', '/':',', '+':'!', '-':'_'}

def p_post(a):
    Z = {'*': '.',
         '/': ',',
         '+': '!',
         '-': '_'}
    a = a.replace(' ', '')
    for i in '+-*/':
        a = a.replace(f'{i}', f' {i} ')

    a = a.split(' ')

    for z in '/*':
        while z in a:
            a = a[:a.index(f'{z}') - 1] + [' ' + a[a.index(f'{z}') - 1] + ' ' + a[a.index(f'{z}') + 1] + ' ' + f'{Z[z]}'] + a[a.index(f'{z}') + 2:]

    for z in '.,':
        while z in a:
            k = a[::].index(z)
            a = a[:k] + [''.join(a[k:k + 3:])] + a[k+3::]
            print(a)

    for z in '+-':
        while z in a:
            a = a[:a.index(f'{z}') - 1] + [a[a.index(f'{z}') - 1]] + [a[a.index(f'{z}') + 1]] + [f'{Z[z]}']  + a[a.index(f'{z}') + 2:]
    a = ' '.join(a)
    return a


def post(a):
    groups = [m.group() for m in re.finditer(r"(\([^\(]*?\))", a)]

    if '(' not in a:
        #print(a, ' ---------', p_post(a))
        return p_post(a)


    for el in groups:
        a = a.replace(el, post(el[1:-1]))
    return post(a)



def p_pref(a):
    Z = {'*': '.',
         '/': ',',
         '+': '!',
         '-': '_'}
    a = a.replace(' ', '')
    for i in '+-*/':
        a = a.replace(f'{i}', f' {i} ')

    a = a.split(' ')
    for z in '/*':
        while z in a:
            a = a[:a.index(f'{z}') - 1] + [f'{Z[z]}'] + [a[a.index(f'{z}') - 1]] + [a[a.index(f'{z}') + 1]] + a[a.index(f'{z}') + 2:]
    for z in '.,':
        while z in a:
            k = len(a) - 1 - a[::-1].index(z)
            a = a[:k] + [''.join(a[k:k + 3:])] + a[k+3::]


    for z in '+-':
        while z in a:
            a = a[:a.index(f'{z}') - 1] + [f'{Z[z]}'] + [a[a.index(f'{z}') - 1]] + [a[a.index(f'{z}') + 1]] + a[a.index(f'{z}') + 2:]



    a = ' '.join(a)

    return a

def pref(a):
    groups = [m.group() for m in re.finditer(r"(\([^\(]*?\))", a)]

    if '(' not in a:
        print(a, ' ---------', p_pref(a))

        return p_pref(a)


    for el in groups:
        a = a.replace(el, pref(el[1:-1]))
    return pref(a)


if f == 2:
    an = post(a)
else:
    an = pref(a)

for i in Z.items():
    if i[1] in an:
        an = an.replace(i[1], i[0])
print(an)

