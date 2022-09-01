it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Length of the set it_companies :" ,len(it_companies))
#Adding a value to the set
it_companies.add("Twitter")
#Declaring multiple companies set and updating the previous set
Multiple_it_companies={"Hp","dell","Innroad"}
it_companies.update(Multiple_it_companies)
print(it_companies)
#Removing a value HP from the set
it_companies.remove("Hp")
#Performing operations such as  A Union B, A intersection B, A issubset B, A disjoint B, A union B and B union A
Join_A_B=A.union(B)
print("join of A and B:", Join_A_B)
A_intersection_B=A.intersection(B)
print("Intersection of A and B:",A_intersection_B)
A_issubset_B=A.issubset(B)
print("A subset B:",A_issubset_B)
A_disjoint_B=A.isdisjoint(B)
print("A is disjoint of B:",A_disjoint_B)
Join_A_B=A.union(B)
print("join of A and B:", Join_A_B)
Join_B_A=B.union(A)
print("join of B and A:", Join_B_A)
#performing operations such as A symmetric difference B
A_symmetricdifference_B=A.symmetric_difference(B)
print("Symmetric difference between A and B :",A_symmetricdifference_B)
#Deleting the sets completely
Delete_SetA=A.clear
Delete_SetB=B.clear
#Converting ages to a set and comparing the length of new age set with previous age set
new_age_set=set(age)
print(len(age))
print(len(new_age_set))
length_of_previousset=len(age)
length_of_new_age_set=len(new_age_set)
if(length_of_new_age_set==length_of_previousset):
    print("The previous age set is same as new age set")
else:
    print("Both sets are not equal")
