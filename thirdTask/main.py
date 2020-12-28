import pandas as pn
import numpy as np
from reportCard import ReportCard
import shutil
from Student import Student





def returnStudentList(arr):
    result = []
    for i in arr:
        result.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    return result

def checkUserInput(string):
    if (not string.isnumeric()):
        return False
    tempNum = int(string)
    return  (tempNum>0 and tempNum <7)

def INVALID():
    print("INVALID")

def printCenter(string):
        print(string.center(shutil.get_terminal_size().columns))

def printOptions():
    printCenter("REPORT CARD")
    print("""
    You have the following options : \n
    1. Display the list of students.\n
    2. Display individual data of student.\n
    3. Get the list of Top 10 students in the batch.\n
    4. Get the list of students who scored more than the aggregate.\n
    5. Add new student.\n
    6. Quit.\n

    """)
    return
allStudentsCSV = pn.read_csv("./studentList.csv")



studentReportCard = ReportCard(returnStudentList(allStudentsCSV.values),allStudentsCSV.columns)

userInput = "sexy"

while (userInput != '6'):
    printOptions()
    userInput = input("Enter your option : ")
    if (not checkUserInput(userInput)):
        INVALID()
        continue
    else:
        if (userInput == '1'):
            studentReportCard.display()

        # elif (userInput == '2'):


        elif (userInput == '3'):
            (studentReportCard.rankStudents())

        elif (userInput == '4'):
            studentReportCard.getAggregateList()

        elif (userInput == '5'):
            if (studentReportCard.addStudent()):
                print("Student added!")
            
    
        
        elif (userInput == '6'):
            print("\nThank you!\n")
            break
    


