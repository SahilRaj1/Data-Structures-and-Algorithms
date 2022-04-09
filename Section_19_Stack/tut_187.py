""" Stack using list without size limit"""

class Stack:
    def __init__(self):
        self.list = []

    # display stack
    def display(self):
        print(self.list)

    # check if the stack is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self,value):
        self.list.append(value)

    # pop
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print(self.list[len(self.list)-1])

    # delete
    def delete(self):
        self.list = None


s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.display()

s.pop()
s.display()

s.peek()

s.delete()