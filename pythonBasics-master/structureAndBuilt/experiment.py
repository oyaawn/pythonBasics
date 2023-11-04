# lists

courses=['History','Math','Physics','CompSci']
print(len(courses))

print(courses[-1])
print(courses[0:2])
print(courses[:2])
courses.append('Chemistry')
courses.insert(0,'Art')


courses2=['Education','Biology']
courses.extend(0,courses2)
 
courses.insert(0,courses2)

print(courses)