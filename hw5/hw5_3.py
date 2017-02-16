class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, value):
        return self.stack.append(value)
    def pop(self):
        try:
            return self.stack.pop(-1)
        except IndexError:
            print('There\'s no object in the stack.')     