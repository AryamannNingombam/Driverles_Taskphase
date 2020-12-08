def compare(a):
    return a[1]

def findMin(string)->int:
    result = 100000
    for i in range(len(string)):
        for j in string[i:]:
            if (string[i]==j):
                continue
            result  = min(result,abs(ord(string[i]) -ord(j) ))
 
 
    return result
                



fileContents = []

with open("names.txt",'r') as file:
    fileContents = file.readlines()
    for j,i in enumerate(fileContents):
        fileContents[j] = i.replace("\n","").split(',')
    #Sorting
    print(fileContents)
    fileContents.sort( key = compare)
    print(fileContents)

final = []
with open("names.txt","w") as file:
    for j,i in enumerate(fileContents):
        if (j+1 & 1):
            continue
        final.append(i)
        file.write(','.join(i) + '\n')


tempString = ''
for i in final:
    tempString += i[0]
print(tempString)
print(findMin(tempString))