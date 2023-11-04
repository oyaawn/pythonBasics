class node: # node class
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList: # linked list wrapper class
    def __init__(self):
        self.head = node()