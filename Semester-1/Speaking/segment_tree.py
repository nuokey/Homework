import math

l = [8, 1, 9, 5, 4, 7, 3]

class SegmentTreeSum():
    def __init__(self, l):
        lox = math.ceil(math.log2(len(l)))
        while len(l) != 2**lox:
            l.append(0)
        
        t = [0] * (len(l) - 1) + l

        for i in range(len(l)-2, -1, -1):
            t[i] = t[2*i+1] + t[2*i+2]

        self.tree = t
        self.ilength = len(l)
        # print(self.tree)
        
    def query(self, left, right):
        return self.innerquery(left, right, 0, 0, self.ilength)
    
    def innerquery(self, left, right, i, goleft, goright): # goleft, goright - границы ответственности ноды
        if left == goleft and right == goright:
            return self.tree[i]
        
        mid = (goleft + goright) // 2
        a = 0
        b = 0
        if left < mid:
            a = self.innerquery(left, min(mid, right), 2*i+1, goleft, mid)
        if right > mid:
            b = self.innerquery(max(mid, left), right, 2*i+2, mid, goright)
        return a + b

tree = SegmentTreeSum(l)
print(tree.query(3, 7))