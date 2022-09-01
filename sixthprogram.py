#defining a function named printwords for finding uniquewords from given sentence
def printwords(Givensentence):
    #using for loop to check unique words that are present in given sentence
    for uniquewords in Givensentence:
        print(uniquewords)
#Assigned the givensentence to a variable named str
str="I am a teacher and I love to inspire and teach people"
# setting up the sentence and split each uniqueword with a space
sentence=set(str.split(" "))
printwords(sentence)
