class Node: 
    def __init__(self, data): 
        self.item = data 
        self.nref = None 
        self.pref = None


class DoublyLinkedList: 
    def __init__(self): 
        self.start_node = None

    def insert_in_emptylist(self, data): 
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
        else: 
            print("list is not empty")
            
    def insert_at_start(self, data): 
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
            print("node inserted") 
            return 
        new_node = Node(data) 
        new_node.nref = self.start_node 
        self.start_node.pref = new_node 
        self.start_node = new_node
        
    def insert_at_end(self, data): 
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
            return
        n = self.start_node 
        while n.nref is not None: 
            n = n.nref 
        new_node = Node(data) 
        n.nref = new_node 
        new_node.pref = n
            
    def insert_after_item(self, x, data): 
        if self.start_node is None: 
            print("List is empty") 
            return 
        else: 
            n = self.start_node 
            while n is not None: 
                if n.item == x: 
                    break 
                n = n.nref 
            if n is None: 
                print("item not in the list") 
            else: 
                new_node = Node(data) 
                new_node.pref = n 
                new_node.nref = n.nref 
                if n.nref is not None: 
                    n.nref.prev = new_node 
                n.nref = new_node
                
    def insert_before_item(self, x, data): 
        if self.start_node is None: 
            print("List is empty") 
            return 
        else: 
            n = self.start_node 
            while n is not None: 
                if n.item == x: 
                    break 
                n = n.nref 
            if n is None: 
                print("item not in the list") 
            else: 
                new_node = Node(data) 
                new_node.nref = n 
                new_node.pref = n.pref 
                if n.pref is not None: 
                    n.pref.nref = new_node 
                n.pref = new_node
                
    def traverse_list(self): 
        if self.start_node is None: 
            print("List has no element") 
            return 
        else: 
            n = self.start_node 
            while n is not None: 
                print(n.item , " ") 
                n = n.nref
                
    def delete_at_start(self): 
        if self.start_node is None: 
            print("The list has no element to delete") 
            return 
        if self.start_node.nref is None: 
            self.start_node = None 
            return 
        self.start_node = self.start_node.nref 
        self.start_node.pref = None
        
    def delete_at_end(self): 
        if self.start_node is None: 
            print("The list has no element to delete") 
            return 
        if self.start_node.nref is None: 
            self.start_node = None 
            return 
        n = self.start_node 
        while n.nref is not None: 
            n = n.nref 
        n.pref.nref = None
        
    def delete_element_by_value(self, x): 
        #check empty list
        if self.start_node is None: 
            print("The list has no element to delete") 
            return 
        #check if list is a single element
        if self.start_node.nref is None: 
            if self.start_node.item == x: 
                self.start_node = None 
            else: 
                print("Item not found")
                return 
        # list has > 1 element, and desirable elem is the first in the list
        # folllowing the delete_at_start() method
        if self.start_node.item == x: 
            self.start_node = self.start_node.nref 
            self.start_node.pref = None 
            return 
        # list is nonsingle-element and desirable elem is not the first
        n = self.start_node 
        while n.nref is not None: 
            if n.item == x: 
                break 
            n = n.nref 
        if n.nref is not None: 
            n.pref.nref = n.nref 
            n.nref.pref = n.pref 
        else: 
            if n.item == x: 
                n.pref.nref = None 
            else: 
                print("Element not found")
                
    def reverse_linked_list(self): 
        if self.start_node is None: 
            print("The list has no element to delete") 
            return 
        p = self.start_node 
        q = p.nref 
        p.nref = None 
        p.pref = q 
        while q is not None: 
            q.pref = q.nref 
            q.nref = p 
            p = q 
            q = q.pref 
        self.start_node = p

    # Первое упражнение
    def item_in_list(self, item):
        i = self.start_node
        while True:
            if i == None:
                return False
            elif i.item == item:
                return True
            i = i.nref

    # Второе упражнение
    def traverse_reversed_list(self):
        self.reverse_linked_list()
        self.traverse_list()

    # Четвертое упражнение
    def delete_item(self, item):
        self.delete_element_by_value(item)

    # Пятое упражнение
    def a1_an(self):
        i = self.start_node
        self.reverse_linked_list()
        p = self.start_node
        # print(i.pref.item, p.nref.item)
        while i.item != p.item:
            print(i.item-p.item)
            i = i.pref
            p = p.nref
            if i.pref.item == p.item:
                print(i.item-p.item)
                return

            

class LinkedList:
    def __init__(self):
        self.start_node = None

    def add_item(self, x, data):
        p = self.start_node
        m = self.start_node.nref
        if x == 0:
            self.start_node = Node(data)
            self.start_node.nref = p
            return
        
        for i in range(x):
            pass
    
    def delete_item(self, data):
        if self.start_node.item == data:
            self.start_node = self.start_node.nref
            return

        p = self.start_node
        i = self.start_node.nref
        while True:
            if i == None:
                print("Элемент не найден")
                return
            elif i.item == data:
                p.nref = i.nref
                return
            
    def traverse_list(self):
        i = self.start_node
        while i != None:
            print(i.item)
            i = i.nref

# Шестое упражнение
class Stack:
    def __init__(self):
        self.data = []
        self.u = -1

    def push(self, el):
        self.data.append(el)
        self.u += 1

    def pop(self):
        self.u -= 1
        p = self.data.pop(-1)
        return p


    def top(self):
        return self.data[-1]


    def size(self):
        return len(self.data)


    def isEmpty(self):
        if len(self.data) == 0:
            return False
        return True

    def printstack(self):
        print(self.data)

n = Stack()
n.push(1)
n.push(2)
n.push(3)
print(n.data)
print(n.pop())
print(n.data, n.u)
print(n.top())
print(n.size())
print(n.isEmpty())
n.printstack()

# Задача списка
# l = DoublyLinkedList()
# l.insert_at_end(1)
# l.insert_at_end(10)
# l.insert_at_end(11)
# l.insert_at_end(4)
# l.insert_at_end(13)
# l.insert_at_end(7)


# print(l.item_in_list(int(input())))
# l.traverse_reversed_list()

# l.delete_item(1)

# l.traverse_list()

# print()

# l.a1_an()

# m = LinkedList()
# m.add_item(0, 10)
# m.traverse_list()
