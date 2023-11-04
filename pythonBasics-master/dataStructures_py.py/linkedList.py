class node: # node class
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList: # linked list wrapper class
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur=self.head
        total=0
        while cur.next!= None:
            total+=1
            cur=cur.next
        return total
    
    def display(self):
        elements= []
        curNode= self.head
        while curNode.next!= None:
            curNode=curNode.next
            elements.append(curNode.data)
        print(elements)
        