class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or self.max_stack[-1] < val:
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max_stack[-1])
        
        print(self.stack)
        
            
    def pop(self):
        try:
            self.stack.pop()
            self.max_stack.pop()
            print(self.stack)
            
        except IndexError as ie:
            print("ERROR: There are no items in the stack!")
            return ie
    
    def get_max(self):
        try:
            print(self.max_stack[-1])
        except ValueError as ve:
            print("ERROR: There are no items in the stack!")
            return ve
        
        
stack = Stack()
stack.push(4)
stack.push(3)
stack.push(9)
stack.push(2)
stack.push(8)

stack.get_max() #9

stack.pop()
stack.pop()
stack.pop()

stack.get_max() #4

stack.pop()
stack.pop()
stack.pop() #"There are no items in the stack"

