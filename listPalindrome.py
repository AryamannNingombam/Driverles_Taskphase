# Code to see if a given list is a palindrome or not
def printPattern(arr):
    pointer = 0

    length = len(arr)
    allPatterns = []
    while (pointer <= length/2  + 1):
        stringToPrint = ''.join(arr[:pointer+1] + arr[:pointer][::-1])
        allPatterns.append(stringToPrint)
        
        pointer+=1
    secondLength = len(allPatterns[-1])
    spaces = secondLength//2
    for i in allPatterns:
        print(' '*spaces + i)
        spaces-=1


    spaces = 0
    for i in allPatterns[::-1]:
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


# userInput = input("Enter the elements : ").split()

# result = isPalindrome(userInput,0,len(userInput)-1)
# if result:
#     print("Palindrome!")
#     for i in userInput:
#         print(hex(ord(i)),end=' ')
#     print('\n')
# else:
#     print("Not palindrome!")
#     printPattern(['a','b','c','d'])

(printPattern(['f','m','d','a']))