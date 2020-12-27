import pandas as pn
import numpy as np
from reportCard import ReportCard
import shutil


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

studentReportCard = ReportCard(allStudentsCSV.values,allStudentsCSV.columns)

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

        if (userInput == '5'):
            if (studentReportCard.addStudent()):
                print("Student added!")
            

        
        elif (userInput == '6'):
            print("\nThank you!\n")
            break
    
    



