# st = []

# st.append(8)
# st.append(1)
# st.append(3)
# st.append(5)
# st.append(9)

# print(st)

# st.pop()
# print(st)
# print(st[-1])


## List Implementation of Stack

# class Stack:
#     def __init__(self):
#         self.st = []

#     def push (self,x):
#         self.st.append(x)

#     def pop (self):
#         if len(self.st) == 0:
#             return -1
#         x = self.st [-1]
#         self.st.pop()
#         return x
    
#     def top (self):
#         if len (self.st) == 0:
#             return -1
#         return self.st[-1]
    
#     def size (self):
#         return len(self.st)
    
# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print(stack.size())
# print(stack.pop())
# print(stack.top())          


## Linked List Implementation of Stack

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
#         self.length = 0

#     def push (self,x):
#         self.length += 1
#         if self.top is None:
#             self.top = Node(x)
#             return
#         else:
#             newNode = Node(x)
#             newNode.next = self.top
#             self.top = newNode

#     def pop(self):
#         if self.top == None:
#             return -1
#         self.length -= 1
#         x = self.top.data
#         self.top = self.top.next
#         return x
    
#     def getTop(self):
#         if self.top == None:
#             return -1
#         return self.top.data
    
#     def size (self):
#         return self.length
        
# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print(stack.size())
# print(stack.pop())
# print(stack.getTop())
        


## Linked List Implementation of Queue


class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push (self,x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop (self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x
    

    def getFront(self):
        if len (self.q) == 0:
            return -1
        return self.q[self.front]
    
    def size (self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front
    

queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)

print(queue.getFront())
queue.pop()

print(queue.getFront())
print(queue.size())



### RECURSION   valid parenthesis program

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1 or len(s) % 2 != 0:
            return False

        st = []

        for i in range(len(s)):

            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                st.append(s[i])

            elif s[i] == "}":
                if st and st[-1] == "{":
                    st.pop()
                else:
                    return False

            elif s[i] == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    return False

            elif s[i] == "]":
                if st and st[-1] == "[":
                    st.pop()
                else:
                    return False

        return len(st) == 0
