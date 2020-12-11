# This function would return the number to 
# be compared for sorting
def compare(a):
    return a[1]

def findMin(string)->int:
    result = 100000
    for i in range(len(string)):
        for j in string[i:]:
            # As we don't need 0 as the answer
            if (string[i]==j):
                continue
            result  = min(result,abs(ord(string[i]) -ord(j) ))
 
 
    return result
                



fileContents = []

with open("names.csv",'r') as file:
    fileContents = file.readlines()
    # Removing the first item (This would be the
    #  titles in the csv file)
    fileContents.pop(0)
    
    # Removing the \n from the end of the file
    for j,i in enumerate(fileContents):
        fileContents[j] = i.replace("\n","").split(',')
    #Sorting

    fileContents.sort( key = compare)


# This list would contain the final elements
final = []
with open("names.csv","w") as file:
    # Adding back the title of the csv file
    file.write("Name,Number\n")
    for j,i in enumerate(fileContents):
        # if the index is odd, don't add it
        if (j+1 & 1):
            continue
        final.append(i)
        # adding a comma in between the name and the number
        file.write(','.join(i) + '\n')


tempString = ''
# adding the first element (the name)
for i in final:
    tempString += i[0]
print(tempString)
# Finding the minimum difference between two elements 
# in the string
print(findMin(tempString))