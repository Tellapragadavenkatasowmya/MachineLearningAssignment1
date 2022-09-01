#Created tuple with sisters and brothers
sisters=('chandini','madhavi','dhanvee')
brothers=('sriram','pranav')
#Joining sisters and brothers to a variable named sibilings
siblings=sisters+brothers
print("Siblings in the tuple ",siblings)
#finding the length of siblings
print("No of siblings",len(siblings))
#Converting tuple to list 
listofsiblings=list(siblings)
#Modifying the siblings tuple to Family Members by adding father and mother names
listofsiblings.append('Aditya')
listofsiblings.append('Anuraga')
Family_members=tuple(listofsiblings)
print("Family members after appending and converting them to a tuple: ",Family_members)
