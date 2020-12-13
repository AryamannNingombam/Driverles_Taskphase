#Code to multiply two matrices
# This code assumes that the matrices are valid and 
# the multiplication is valid
def generateMatrix(row,col):
    result = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(0)
        result.append(temp)
    return result


def displayMatrix(arr):
    for i in arr:
        for j in i:
            print(j,end=' ')
        print('\n')
    return



def multiply2(arr1,arr2):
      #Get number of rows for the final answer
    rowsInAnswer = len(arr1)
    
    #Get number of columns for the final answer
    
    colsInAnswer = len(arr2[0])
    finalResult = generateMatrix(rowsInAnswer,colsInAnswer)
    for i in range(rowsInAnswer):
        for j in range(colsInAnswer):
            for k in range(len(arr1[0])):
                finalResult[i][j] += arr1[i][k]  * arr2[k][j]



    return finalResult


def multiply(arr1,arr2):
    #Get number of rows for the final answer
    rowsInAnswer = len(arr1)
    
    #Get number of columns for the final answer
    
    colsInAnswer = len(arr2[0])
    # for later calculations
    colsInArr1 = len(arr1[0])
    rowsInArr2 = len(arr2)
    # making matrix that would contain the final answer
    finalResult = generateMatrix(rowsInAnswer,colsInAnswer)

    # MAIN LOGIC
    arr1RowPointer = 0
    arr2ColPointer = 0
    finalAnswerRow=0
    finalAnswerCol=0
    #This while loop would fill individual elements 
    #in the final answer when it iterates once
    while (arr1RowPointer < rowsInAnswer and arr2ColPointer < colsInAnswer):
        arr1ColPointer= 0
        arr2RowPointer = 0
        tempResult = 0
        #This while loop would add the corresponding 
        #values to get the final result;
        while (arr1ColPointer < colsInArr1 and arr2RowPointer < rowsInArr2):
            tempResult += arr1[arr1RowPointer][arr1ColPointer]*arr2[arr2RowPointer][arr2ColPointer]

            arr1ColPointer+=1
            arr2RowPointer+=1
        
        #To store the values in the final result    
        finalResult[finalAnswerRow][finalAnswerCol] = tempResult

        #incrementing the pointers to
        #go to the next iteration;
        arr2ColPointer+=1
        finalAnswerCol+=1

        #To shift the rows once we reach
        #the end of the column
        if (arr2ColPointer == colsInAnswer):
            arr1RowPointer+=1
            arr2ColPointer = 0

        #This is to go to the
        #next row once we reach the end of th
        #row
        if (finalAnswerCol == colsInAnswer):
            finalAnswerRow+=1
            finalAnswerCol=0

    return finalResult  

#This function would run under the assumption
#that arr is a valid input
def transpose(arr):
    rows = len(arr)
    cols = len(arr[0])
    colsInFinalAnswer = rows
    rowsInFinalAnswer = cols
    finalResult = generateMatrix(rowsInFinalAnswer,colsInFinalAnswer)
    arrRowPointer,arrColPointer,resultRowPointer,resultColPointer=0,0,0,0
    
    #When this condition is true, we have made the transpose and can return the result;
    while arrRowPointer < rows and resultColPointer < colsInFinalAnswer:
        finalResult[resultRowPointer][resultColPointer] = arr[arrRowPointer][arrColPointer]

        arrColPointer+=1
        resultRowPointer+=1
        if (arrColPointer==cols and resultRowPointer == rowsInFinalAnswer):
            arrRowPointer+=1
            resultColPointer+=1
            arrColPointer=0
            resultRowPointer=0       

    return finalResult


dim1 = list(map(int,input("Enter the dimensions of the first matrix : ").split(' ')))
dim2 = list(map(int,input("Enter the dimensions of the second matrix : ").split(' ')))

if (dim1[1] != dim2[0]):
    print("MULTIPLICATION NOT POSSIBLE!")
else:
    matrix1 = generateMatrix(dim1[0],dim1[1])

    for i in range(dim1[0]):
        for j in range(dim1[1]):
            matrix1[i][j] = int(input("Enter the element for first : "))
    
    matrix2 = generateMatrix(dim2[0],dim2[1])

    for i in range(dim2[0]):
        for j in range(dim2[1]):
            matrix2[i][j] = int(input("Enter the element for second :  "))
    print(matrix1)
    print(matrix2)
    print("Matrix 1 : ")
    displayMatrix(matrix1)
    print("Matrix 2 : ")
    displayMatrix(matrix2)

    print("RESULT")
    result = multiply(matrix1,matrix2)
    displayMatrix(result)

    print("Verifying transpose(AB) = transpose(B)transpose(A)")    
    print("transpose(A*B)")
    displayMatrix(transpose(result))
    print("transpose(B) * transpose(A)")
    displayMatrix(multiply(transpose(matrix2),transpose(matrix1)))
    print("BOTH EQUAL!")


