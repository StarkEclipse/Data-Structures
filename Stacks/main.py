class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.items)
print(stack.top())
stack.push(30)
print(stack.items)
stack.push("a")
stack.push("b")
print(stack.items)
print(stack.pop())
print(stack.top())