import numpy

# Последовательность Фибоначчи
def fib(n):
	if n < 3:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# print(fib(int(input())))

# Раскладывание числа на простые множители
def prost(n):
	
	for i in range(2, n+1):
		# print(n, i)
		if n % i == 0:
			a = i
			return str(i) + " " + prost(n//i)
	else:
		return ""


# print(prost(int(input())))


# Упражнение 3
def three():
	

# Упражнение 4
def triangle():
	a = input().split()
	n = int(a[0])
	s = a[1]

	for i in range(n):
		if i <= n // 2-1:
			print(s*(i+1))
		else:
			print(s*(n-i))

# triangle()


# Упражнение 5
def spiral():
	a = input().split()
	n, m = int(a[0]), int(a[1])
	s = numpy.ones((n, m))
	
	l = []
	x = 0
	y = 0
	d = 0

	while len(l)//2 != n*m:
		s[x, y] = len(l)//2 + 1

		

		l.append((x, y))

		
		if d == 0:
			if y == m - 1:
				d += 1
			elif (x, y + 1) in l:
				d += 1
		if d == 1:
			if x == n - 1:
				d += 1
			elif (x + 1, y) in l:
				d += 1
		if d == 2:
			if y == 0:
				d += 1
			elif (x, y - 1) in l:
				d += 1
		if d == 3:
			if x == 0:
				d = 0
			elif (x - 1, y) in l:
				d = 0


		if d == 0:
			y += 1
			l.append((x, y))
		elif d == 1:
			x += 1
			l.append((x, y))
		elif d == 2:
			y -= 1
			l.append((x, y))
		elif d == 3:
			x -= 1
			l.append((x, y))

		# print((x, y), d, len(l)//2)
	print(s)
	for i in range(n):
		print(s[i] * i)


spiral()

# Упражнение 6

