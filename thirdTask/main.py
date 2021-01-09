import pandas as pn
import csv
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
    return  (tempNum>0 and tempNum <8)

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
    6. Update details about a student.\n
 
    7. Quit.\n

    """)
    return
allStudentsCSV = pn.read_csv("./studentList.csv")



studentReportCard = ReportCard(returnStudentList(allStudentsCSV.values),allStudentsCSV.columns)

userInput = "sexy"

while (userInput != '7'):
    printOptions()
    userInput = input("Enter your option : ")
    if (not checkUserInput(userInput)):
        INVALID()
        continue
    else:
        if (userInput == '1'):
            studentReportCard.display()

        elif (userInput == '2'):
            index = studentReportCard.searchStudent()
            studentReportCard.displayIndividualData(index)
        elif (userInput == '3'):
            (studentReportCard.rankStudents())

        elif (userInput == '4'):
            studentReportCard.getAggregateList()

        elif (userInput == '5'):
            if (studentReportCard.addStudent()):
                print(printCenter("Student added!"))
            
        elif (userInput == '6'):
            index = studentReportCard.searchStudent()
            studentReportCard.updateDetails(index)

        elif (userInput == '7'):
            (printCenter("\nThank you!\n"))
            break
    

#saving the file after all the playing

with open("./studentList.csv","w") as file:
    reader = csv.writer(file)
    reader.writerow(studentReportCard.headings)
    for i in studentReportCard.allStudentObjects:
        reader.writerow(i.returnList())


# Name,Adm.No.,RollNo.,Class,Science,Maths,SST,English
# Aryamann,6969696969,69,12,99.0,99,99,99
# Harkirat,1245867683,56,12,85.0,79,5,45
# Shefali,4548455246,12,11,65.0,78,98,56
# G-Eazy,4546787678,3,12,89.65,54,69,95
# Eminem,1277898799,10,12,96.0,100,85,100
# Tupac,12369,11,9,33.0,33,33,99
# Aryan,466768,45,12,96,54,23,65
# Ritvik,696969669,65,11,32,65,36,24
# Arnav,6546865486,54,11,67,54,85,28
# Bebe Rexa,463768473,19,6,13,79,69,69
# Halsey,647768737,75,12,93,98,95,74