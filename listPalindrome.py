# Code to see if a given list is a palindrome or not
from math import ceil,floor
def printPattern(arr):
    pointer = 0

    length = len(arr)
    allPatterns = []

    while (pointer <= ceil(length/2)):
        temp = arr[:pointer+1]
        stringToPrint=''
        if (len(temp)<2):
            stringToPrint = ''.join(temp)
        else:
            stringToPrint = ''.join(temp) + ''.join(temp[::-1][1:])
        allPatterns.append(stringToPrint)
        
        pointer+=1
    secondLength = len(allPatterns[-1])
    spaces = secondLength//2
    for i in allPatterns:
        print(' '*spaces + i)
        spaces-=1


    spaces = 1
    for i in allPatterns[::-1][1:]:
        print(' '*spaces + i)
        spaces+=1




def isPalindrome(fullList,left,right):
    
    if (left>=len(fullList) or right<0):
        return False
    if (left>=right and fullList[left] == fullList[right]):
        return True
    if (left>=right):
        return False
    if (fullList[left] == fullList[right]):
        return isPalindrome(fullList,left+1,right-1)
    return False


userInput = input("Enter the string : ")

result = isPalindrome(userInput,0,len(userInput)-1)
if result:
    print("Palindrome!")
    for i in userInput:
        print(hex(ord(i)),end=' ')
    print('\n')
else:
    print("Not palindrome!")
    printPattern(input("Enter the elements for the pattern with spaces in between : ").split(' '))
    