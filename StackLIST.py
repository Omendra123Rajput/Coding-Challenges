'''
Stack using python list

'''


class Stack():
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    # isEmpty

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    # push

    def push(self, value):
        self.list.append(value)
    # pop

    def pop(self):
        if self.isEmpty():
            return 'There are no elements in the stack'
        else:
            return self.list.pop()
    # peek()

    def peek(self):
        if self.isEmpty():
            return 'There are no elements in the stack'
        else:
            return self.list[len(self.list)-1]
    # delete()

    def delete(self):
        self.list = None


cusSTack = Stack()
cusSTack.push(1)
cusSTack.push(2)
cusSTack.push(3)
# cusSTack.delete()

print(cusSTack.pop())

print('---')

print(cusSTack)
