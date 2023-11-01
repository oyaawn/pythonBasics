class Employee:
    def __init__(self,firstName, lastName, salary):
        self.firstName= firstName
        self.lastName= lastName
        self.email= firstName+'.'+ lastName+'@gmail.com'
        self.salary= salary

emp1= Employee('Hardik','Pandya','123456')
emp2= Employee('Rohit','Sharma','789456')


print (emp1.email)
print (emp2.email)

