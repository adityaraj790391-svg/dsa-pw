### linked list

### Singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(3)
c = Node(1)

a.next = b
b.next = c

head = a

# print(head.data)
# print(head.next.data)
# print(head.next.next.data) 


### traverse in linke list

def printLinkedList(head):
    curr = head

    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next

# printLinkedList(head)

### insert at the beginning

newNode = Node(9)
newNode.next = head
head = newNode

# printLinkedList(head)

### insert at the end

newNode = Node(1)

curr = head
while curr.next != None:
    curr = curr.next

curr.next = newNode
# printLinkedList(head)

### insertion at the kth index

k = 2
newNode = Node(6)

curr = head
for i in range(k-1):
    curr = curr.next

newNode.next = curr.next
curr.next = newNode

# printLinkedList(head)


### delete the first node

head = head.next
# printLinkedList(head)

### delete the last node

curr = head

while curr.next.next != None:
    curr = curr.next

curr.next = None
# printLinkedList(head)

### delete node at kth index

k = 2

curr = head
for i in range(k-1):
    curr = curr.next

curr = curr.next.next

# printLinkedList(head)


### Doubly linked list

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

a = DoublyNode(5)
b = DoublyNode(3)
c = DoublyNode(1)

a.next = b
b.prev = a
b.next = c
c.prev = a

head = a

# print(head.data)
# print(head.next.data)
# print(head.next.next.data) 


### Circular linked list

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

a = CircularNode(5)
b = CircularNode(3)
c = CircularNode(1)

a.next = b
b.next = c
c.next = a

head = a

print(head.data)
print(head.next.data)
print(head.next.next.data)

curr = head

while True:
    print(curr.data, end = " ") 
    curr = curr.next
    if curr == head:
        break











