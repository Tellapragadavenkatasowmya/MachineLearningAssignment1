#importing statistics module for finding median
import statistics
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorting the age list
ages.sort()
print("Initial list of ages:",ages)
#finding max age in the list
maxage=max(ages)
print("Maxage in the list",maxage)
#finding min age in the list
minage=min(ages)
print("Minage in the list",minage)
#appending the max age and min age to the age list
ages.append(maxage)
ages.append(minage)
print("List of ages after appending min and max age :",ages)
#Finding median value from the age list
print("Median:",statistics.median(ages))
#finding average from the age list by defining a function 
def Average(list):
    return sum(list)/len(list)
average=Average(ages)
print("average:",average)
#finding range value from the age list
range=maxage-minage
print("Range in the list is :",range)
