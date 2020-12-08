# Code to see if a given list is a palindrome or not
def printPattern(arr):
    pointer = 0

    length = len(arr)
    while (pointer <= length/2):
        print(''.join(arr[:pointer+1] + arr[:pointer][::-1]))
        pointer+=1
    while (pointer>=0):
        print(''.join(arr[:pointer+1] + arr[:pointer][::-1]))
        pointer-=1




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


userInput = input("Enter the elements : ").split()

result = isPalindrome(userInput,0,len(userInput)-1)
if result:
    print("Palindrome!")
    for i in userInput:
        print(hex(ord(i)),end=' ')
    print('\n')
else:
    print("Not palindrome!")
    printPattern(['a','b','c','d'])
