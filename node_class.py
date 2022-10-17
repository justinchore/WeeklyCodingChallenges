class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_nodes(self):
        while self != None:
            print(self.val, "->", end="")
            self = self.next
        print("\n")