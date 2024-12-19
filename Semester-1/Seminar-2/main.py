# Все задания оформлены в виде функций


def one():
    a = input().split()

    n = a[0]

    l = a[1:]
    l = sorted(l)

    for i in range(len(l)):
        # print(l[i], i + 1)
        if int(l[i]) != i + 1:
            print(i+1)
            break
    else:
        print(n)

# one()

def two():
    a = input().split()

    g = int(a[0])

    s = a[1]

    l = ""

    x = ""
    q = 0
    for i in range(len(s)):
    	if q != g-1:
    		x = s[i] + x
    		q += 1
    	else:
    		x = s[i] + x
    		l += x
    		x = ""
    		q = 0

    print(l)

# two()

def three():
	a = ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y", "1", "8"]
	b1 = ["E", "J", "S", "Z"]
	b2 = ["a", "b", "c", "d"]
	b3 = ["3", "L", "2", "5"]
	d = ["B", "C", "D", "F", "G", "K", "N", "P", "Q", "R"]

	s = input()
	s2 = s

	p = False
	z = False

	if s[::-1] == s:
		p = True

	for i in range(4):
		s2 = s2.replace(b1[i], b2[i])
		s2 = s2.replace(b3[i], b1[i])
		s2 = s2.replace(b2[i], b3[i])

	for i in range(len(d)):
		s2 = s2.replace(d[i], "")

	if s2[::-1] == s:
		z = True

	# print(s2)
	# print(p, z)
	if p and z:
		print(f"{s} is a mirrored palindrome")
	elif p and not z:
		print(f"{s} is a regular palindrome")
	elif not p and z:
		print(f"{s} is a mirrored string")
	elif not p and not z:
		print(f"{s} is not a palindrome")



# three()

def four():
	a = input().split()
	for i in range(0, len(a)-1, 2): a[i], a[i+1] = a[i+1], a[i]
	print(a)

# four()

def five():
	a = input().split()
	print([a[-1]] + a[0:-1])

# five()


def six():
	a = input().split()
	for i in range(len(a)):
		if a.count(a[i]) == 1:
			print(a[i])

# six()

def seven():
	a = input().split()

	m = 0
	for i in range(len(a)):
		m = max(m, a.count(a[i]))

	for i in range(len(a)):
		if m == a.count(a[i]):
			print(a[i])
			break

# seven()

def eight():
	n = input()
	a = input().split()

	b = int((int(max(a)) + int(min(a))) // 2)

	c = min(a, key=lambda i: abs(b - int(i)))
	print(c)


# eight()


def nine():
	s = open("input.txt").read()
	s = s.replace("!", ".")
	s = s.replace("?", ".")

	while ".." in s:
		s = s.replace("..", ".")

	if s[-1] == ".":
		s = s[:-1]

	s = s.split(".")
	print(len(s), s)

# nine()

def ten():
	g = ["а", "о", "у", "и", "э", "ю", "я", "ё", "ы", "е"]

	a = open("input.txt").read()
	b = ""

	for i in range(len(a)):
		b += a[i]
		if a[i] in g:
			b += f"с{a[i]}"

	print(b)

# ten()