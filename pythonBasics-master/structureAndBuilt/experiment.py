# lists

courses=['History','Math','Physics','CompSci']
print(len(courses))

print(courses[-1])
print(courses[0:2])
print(courses[:2])
courses.append('Chemistry')
courses.insert(0,'Art')


courses2=['Education','Biology']
courses.extend(courses2)

print(courses)
courses.remove('Math')
courses.reverse()

num= [1,5,2,4,3]

num.sort(reverse=True)

sortedCourses=sorted(courses)
print(sortedCourses)
print(num)

print(sum(num))
print(courses.index('CompSci'))

print ('polSc' in courses)

for item in courses:
    if item=='CompSci':
        print('Found!')
        break


for index, item in enumerate(courses):
    print(index,item)    



class node:
    def __init__(self,data=None):
        self.data=data
        self.Node=None

class linkedList:
    def __init__(self):
        self.head=node()

    def append(self,data):
        newNode= node(data)
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
            currentNode.next=newNode
        
    
