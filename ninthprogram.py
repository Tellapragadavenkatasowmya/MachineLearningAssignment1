#Inputing no of students from user
Number_of_Students=int(input("Enter the number of students :"))
#creating lists for lbs and kgs 
lbs_list=[]
kgs_list=[]
print("Enter weights of "+str(Number_of_Students)+"students")
#Using a for loop to add values of lbs and kgs entered by the user to the list accordingly 
for index in range(Number_of_Students):
    #using temp list to take input of student weights from user by displaying the no of students 
    templist=int(input(str(index+1)+") student weight:"))
    lbs_list.append(templist)
    #Converting the lbs entered by the user to kgs by multiplying the weight with 0.453 as 1bs= 0.453kg
    kgs_list.append(float("{:.2f}".format(templist*0.453)))
print("weights in lbs :",lbs_list)
print("weights in kgs :",kgs_list)
