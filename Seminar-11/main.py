class Node():
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

a = Node(10)
a.left = Node(7)
a.left.left = Node(8)
a.left.right = Node(4)
a.right = Node(15)
a.right.left = Node(90)
a.right.right = Node(0)

b = Node(10)
b.left = Node(15)
b.left.left = Node(0)
b.left.right = Node(90)
b.right = Node(7)
b.right.left = Node(4)
b.right.right = Node(8)

c = Node(10)
c.left = Node(7)
c.left.left = Node(8)
c.left.right = Node(4)
c.right = Node(15)
c.right.left = Node(90)
c.right.right = Node(0)

# Четвертое задание
def mirror(a):
    if a.left == None and a.right == None:
        return a
    else:
        b = Node(a.key, mirror(a.right), mirror(a.left))
        return b

def isIdentical(x, y):
    if x is None and y is None:
        return True
    
    return (x is not None and y is not None) and (x.key == y.key) and isIdentical(x.left, y.left) and isIdentical(x.right, y.right)

# Первое упражнение
def areSimmetrical(a, b):
    return isIdentical(a, mirror(b))

print(areSimmetrical(a, b))


france = [int(i) for i in input().split(" ")]
swimmers = [int(i) for i in input().split(" ")]
pianists = [int(i) for i in input().split(" ")]

l = swimmers

for i in swimmers:
    if i not in l:
        append