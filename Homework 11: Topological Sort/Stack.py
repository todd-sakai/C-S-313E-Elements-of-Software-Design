class Stack:
    def __init__(self):
        self.list = []   

    def push(self, node):
        self.list.insert(0, node)

    def pop(self):
        return self.list.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.list) == 0

    def get_size(self):
        return len(self.list)
    
    def peek(self):
        return self.list[0]
