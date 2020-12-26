# Code to see if a given list is a palindrome or not
from math import ceil,floor
def printPattern(arr):
    arr = ''.join(arr)
    # a b c d e
    allElements = []
    length = len(arr)
    for pointer in range(length):
        stringToPrint = arr[:pointer+1] + arr[:pointer][::-1]
        allElements.append(stringToPrint)
    if (length<4):
        spaces = ceil(length/2)
    else:
        spaces = ceil(length/2) + 2
    for i in allElements:
        print(' '*spaces  + i)
        spaces-=1

    spaces +=2

    for i in allElements[::-1][1:]:
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
    