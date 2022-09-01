#Creating an empty dictionary named dog
dog={}
# Assigning Keys and values to the dog dictionary
dog= {'name':'oreo','colour':'brown','breed':'shihtzu','legs': 4,'age':2}
#Creating a student empty dictionary and assigning keys and values to the dictionary
student={'first_name':'sriram','last_name':'tellapragada'
,'gender':'male','age':18,'martial status':'single'
,'skills':['Good Communication','Analytical','Accountancy'],'country':'india','city':'hyderabad'
,'address':'A.S.Rao Nagar'}
#finding the length of student dictionary and type of student skills
length=len(student)
print("Length of the student list: ",length)
print("Student Skills As List:",student['skills'])
print("Type of student skills :",type(student['skills']))
print("Dog dictionary:",dog)
print("Student dictionary",student)
#appending skills to student skills
student['skills'].append('Maths')
student['skills'].append('Physics')
print("Student skills after appending two more skills :",student['skills'])
#Printing keys and values as list 
keylist=list(student.keys())
valueslist=list(student.values())
print("keys:",keylist)
print("Values:",valueslist)
