print("Name\t\tAge\t\tCountry\t\tCity")
#Assigning Name,Age,Country anf city
Name=["Asabeneh"]
#finding out the length of name 
lengthofname=len(Name)
Age=[250]
Country=["Finland"]
City=["Helsinki"]
#using a for loop to print the values by its namelength
for index in range(lengthofname):
    print(Name[index]+"\t"+str(Age[index])+"\t\t"+Country[index]+"\t\t"+City[index])
