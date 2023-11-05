student={'name':'Ayan',
        'age': 23,
        'courses':['Math','CompSci']
         }

print(student['name'])
print(student.get('phone'))


student.update({'name':'Jane','age':26,'phone':'555-5555'})
print(student)

age=student.pop('age')
print(age)
print(student)

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key,value)
