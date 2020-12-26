#Code to remove all duplicates from a tuple and
# to return the sum of the elements using recursion

def removeDuplicates(arr):
    tempList = []
    for i in arr:
        if i not in tempList:
            tempList.append(i)
    return tuple(tempList)

def addAll(arr,pointer = 0,sum_=0):
    if (pointer == len(arr)):
        return sum_
    sum_ += arr[pointer]
    return addAll(arr,pointer+1,sum_)




tempList = list(map(int,input("Enter the elements : ").split(' ')))
mainTuple = removeDuplicates(tuple(tempList)) 
print("The elements after removing -> ",mainTuple,sep=' ')


print(f'SUM : {str(addAll(mainTuple))}')