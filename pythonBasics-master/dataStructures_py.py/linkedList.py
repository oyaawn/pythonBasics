class node: # node class
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList: # linked list wrapper class
    def __init__(self):
        self.head = node()

    def append(self,data):
        newNode = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

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
        curIndex=0
        curNode=self.head
        while True:
            curNode=curNode.next
            if curIndex==index: return curNode.data
            curIndex+=1

    def eraseByIndex(self,index):
        if index>=self.length():
            print("Error: 'Erase' index out of range!")
            return None
        curIndex=0
        curNode=self.head
        while True:
            lastNode=curNode
            curNode=curNode.next
            if curIndex==index:
                lastNode.next=curNode.next
                return
            curIndex+=1

    def insertAfterData(self,data,newData):
        newNode=node(newData)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            if cur.data==data:
                newNode.next=cur.next
                cur.next=newNode
                return
    
    def eraseByData(self,data):
        cur=self.head
        while cur.next!= None:
            lastNode=cur
            cur=cur.next
            if cur.data==data:
                lastNode.next=cur.next
                return
    

            

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





