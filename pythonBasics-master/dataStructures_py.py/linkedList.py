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

    def get(self,index):
        if index>=self.length():
            print("ERROR: 'Get' index out of range!")
            return None
        currentIndex=0
        currentNode=self.head
        while True:
            currentNode=currentNode.next
            if currentIndex==index: return currentNode.data
            currentIndex+=1

    def erase(self,index):
        if index>=self.length():
            print("Error: 'Erase' index out of range!")
            return None
        currentIndex=0
        currentNode=self.head
        while True:
            lastNode=currentNode
            currentNode=currentNode.next
            if currentIndex==index:
                lastNode.next=currentNode.next
                return
            currentIndex+=1
            

myList=linkedList()

myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
myList.display()

 #print("element at 2nd index:",myList.get(2))
myList.erase(1)
myList.display()





