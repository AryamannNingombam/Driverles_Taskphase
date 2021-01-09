from Student import Student
# this library function is being used to display the table
from tabulate import tabulate

import numpy as np

# this libary function is being imported for alignment purposes
import shutil


#  Name, Admission number, Roll number, 
# Class, Science marks, Maths marks, Social studies marks and English marks

# function that prints the text at the center of
# the screen
def printCenter(string):
        return ((string).center(shutil.get_terminal_size().columns))


class ReportCard():



    def __init__(self,allStudents,headings):
        # two arrays are being maintained,
        # one containing the student object and
        # the other only the values, the student object 
        # would later help in getting the aggregate and
        # displaying
        self.allStudentObjects= allStudents
        self.allStudents  = []
        for i in allStudents:
            self.allStudents.append(i.returnList())
        # for displaying 
        self.headings = headings


    # function that displays the students who
    # cleared the aggregate cutoff
    def getAggregateList(self):
        print(printCenter("STUDENTS WHO PASSED AGGREGATE\n"))
        aggregateStudents  = list(filter(lambda x : x.getAggregate()>=90,self.allStudentObjects))
        self.printRanked(aggregateStudents)

    # simple function that linearly searches for a 
    # student by name
    def searchByName(self,name):
        length = len(self.allStudentObjects)
       

        for i in range(length):
            if ((self.allStudentObjects[i].name).lower() == name.lower()):
                return i
        return -1




    # searching by roll number
    def searchByRollNumber(self,number):
        number = int(number)
        length = len(self.allStudentObjects)
        for i in range(length):
            if (self.allStudentObjects[i].rollNumber == number):
                return i
        return -1


    # searching by the class, not the best option 
    # id say
    def searchByClass(self,cl):
        cl = int(cl)
        length = len(self.allStudentObjects)
        for i in range(length):
            if (self.allStudentObjects[i].cl == cl):
                return i
        return -1






    # main function that handles the main 
    # logic behind searching the student, 
    # to either display or update the 
    def searchStudent(self):
        while (1):
            parameter = input("""
            1.Search by name\n
            2.Search by roll number\n
            3. Search by class\n
            4.Quit\n
            Enter your option : """)
            if (not self.validateNumber(parameter)):
                continue
            else:
                temp = int(parameter)
                index = -1
                if (temp<1 or temp>4):
                    self.PRINTINVALIDNUM()
                    continue
                elif (temp==1):
                    searchName = input("Enter the name : ")
                    if (not self.validateString(searchName)):
                        return
                    index = self.searchByName(searchName)

                elif (temp==2):
                    searchRollNumber = input("Enter the roll number of the student : ")
                    if (not self.validateNumber(searchRollNumber)):
                        return
                    index = self.searchByRollNumber(searchRollNumber)


                elif (temp==3):
                    searchClass =input("Enter the class of the student(NUMERIC ONLY) : ")
                    if (not self.validateNumber(searchClass)):
                        return
                    index=  self.searchByClass(searchClass)
                elif (temp==4):
                    break

                    # this statement
                    # would be true when the input
                    # entered by the user does not exist
                if (index == -1):
                    print(printCenter("\nSTUDENT NOT FOUND!\n"))
                    input("Press enter to continue")
                    return
                else:
                   return index


    # displays data of student in tabular format
    def displayIndividualData(self,index):
        stud = self.allStudentObjects[index]
        studentToDisplay = self.allStudents[index]
        printCenter("STUDENT DATA")
        temp = np.append(self.headings,['Aggregate'])

        print(tabulate([studentToDisplay+[stud.getAggregate()]],temp))
        input("Press enter to continue")


    # this function is used to sort the
    #  students based on their aggregate
    def parameter(self,student):
        return student.getAggregate()

    # function that prints the top 10 students in the class.
    def printRanked(self,ranked):
        counter=1
        for i in ranked[:10]:
            print(printCenter(str(counter)+'.' +str(i)))
            counter+=1
        input("Press enter to continue : ")

    # this function calls the printRanked function after
    # sorting the students based on their merit
    def rankStudents(self):
        print(printCenter("RANKS SCORED ABOVE AGGREGATE\n"))
        ranked = self.allStudentObjects
        ranked.sort(key=self.parameter,reverse=True)
        self.printRanked(ranked)
        
    # just a function to print invalid inputs as im lazy 
    # to write same lines again.
    def PRINTINVALIDNUM(self):
        print("INVALID\nPlease make sure that you have entered values")

    # displays all the students
    def display(self):
        print(tabulate(self.allStudents,self.headings))
        quit = input("Press enter to quit.")
        return





# function that validates user data
# when it is expected to be a number
    def validateNumber(self,num):
        if (not num.isnumeric() or int(num)<=0):
            self.PRINTINVALIDNUM()
            return False
        return True

# function that validates user data
# when it is expected to be a string
    def validateString(self,string):
        if (not string.isalpha()):
            print("INVALID NAME.\nPlease make sure that you have entered only characters for the name")
            return False
        return True
# function that adds a new student to the array and the DB
    def addStudent(self):
        name = input("Enter the name of the student : ")
        if (not self.validateString(name)):
            return False
        
        admissionNumber = input("Enter the admission number of the student : ")
        if (not self.validateNumber(admissionNumber)):
            return False

        
        rollNumber = input("Enter the roll number of the student : ")
        if (not self.validateNumber(rollNumber)):
            
            return False


        cl = input("Enter the standard of the student(IN NUMERIC FORM) : ")
        if (not self.validateNumber(cl)):
            return False
     
        if int(cl)>12:
            return False
        scienceMarks = input("Enter the marks obtained in Science : ")
        
        if (not self.validateNumber(scienceMarks)):
            return False
    
        if float(scienceMarks)<0 or float(scienceMarks)>100:
            return False

        mathsMarks = input("Enter the marks obtained in Maths : ")
        if (not self.validateNumber(mathsMarks)):
            
            return False
        if float(mathsMarks)<0 or float(mathsMarks)>100:
            return False


        SSTMarks = input("Enter the marks obtained in SST : ") 
        if (not self.validateNumber(SSTMarks)):
            return False
        if float(SSTMarks)<0 or float(SSTMarks)>100:
            return False

        englishMarks = input("Enter the marks obtained in English : ")                

        if (not self.validateNumber(englishMarks)):
            return False
        if float(englishMarks)<0 or float(englishMarks)>100:
            return False

        #Everything entered is valid
        newStudent = Student(name,admissionNumber,rollNumber,cl,scienceMarks,mathsMarks,SSTMarks,englishMarks)
        self.allStudentObjects = np.append(self.allStudentObjects,[newStudent])
        self.allStudents.append(newStudent.returnList())
    
    # function that updates the data of an existing student
    def updateDetails(self,index):
        thingToUpdate = "1"

        while (thingToUpdate != "9"):
            thingToUpdate = input("""Enter the attribute to update :\n
            1. Name\n
            2. Admission number\n
            3. Roll number\n
            4. Class\n
            5. Science Marks\n
            6. Maths Marks\n
            7. SST Marks\n
            8. English Marks\n
            9. Quit\nEnter your option : """)
            if (thingToUpdate == '1'):
                newName = input("Enter the new name of the student : ")
                if (not self.validateString(newName)):
                    continue
                else:
                    self.allStudentObjects[index].name = newName
                    self.allStudents[index][0] = newName
                    print("Updated!")
            elif (thingToUpdate == '2'):
                newAdmissionNumber = input("Enter the new admission number of the student : ")
                if (not self.validateNumber(newAdmissionNumber)):
                    continue
                
                else:
                    self.allStudentObjects[index].admissionNumber=  int(newAdmissionNumber)
                    self.allStudents[index][1] = int(newAdmissionNumber)
                    print("Updated!")
            elif (thingToUpdate == '3'):
                newRollNumber = input("Enter the new roll number of the student : ")
                if (not self.validateNumber(newRollNumber)):
                    continue
                else:
                    self.allStudentObjects[index].rollNumber = int(newRollNumber)
                    self.allStudents[index][2] = int(newRollNumber)
                    print("Updated!")
            elif (thingToUpdate == '4'):
                newClass = input("Enter the new standard of the student :(NUMERIC ONLY) ")
                if (not self.validateNumber(newClass)):
                    continue
                else:
                    if (int(newClass)>12):
                        self.PRINTINVALIDNUM()
                        continue
                    self.allStudentObjects[index].cl = (int(newClass))
                    self.allStudents[index][3] = int(newClass)
                    print("Updated!")
            elif (thingToUpdate  == '5'):
                # science   
                newScienceMarks = input("Enter the new marks obtained in science : ")
                if (not self.validateNumber(newScienceMarks)):
                    continue
                else:
                    newScienceMarks = float(newScienceMarks)
                    if newScienceMarks<0 or newScienceMarks>100:
                        self.PRINTINVALIDNUM()
                        continue
                    self.allStudentObjects[index].scienceMarks = (float(newScienceMarks))
                    self.allStudents[index][4] = float(newScienceMarks)
                    print("Updated!")
            
            elif (thingToUpdate == '6'):
                # maths
                newMathsMarks = input("Enter the new marks obtained in maths : ")
                if (not self.validateNumber(newMathsMarks)):
                    continue
                else:
                    newMathsMarks = float(newMathsMarks)
                    if newMathsMarks<0 or newMathsMarks>100:
                        self.PRINTINVALIDNUM()
                        continue
                    self.allStudentObjects[index].mathsMarks = (float(newMathsMarks))
                    self.allStudents[index][5] = float(newMathsMarks)
                    print("Updated!")

            elif (thingToUpdate == '7'):
                # sst
                newSSTMarks = input("Enter the new marks obtained in SST : ")
                if (not self.validateNumber(newSSTMarks)):
                    continue
                else:
                    newSSTMarks = float(newSSTMarks)
                    if newSSTMarks<0 or newSSTMarks>100:
                        self.PRINTINVALIDNUM()
                        continue
                    self.allStudentObjects[index].SSTMarks = (float(newSSTMarks))
                    self.allStudents[index][6] = float(newSSTMarks)
                print("Updated!")

            elif (thingToUpdate == '8'):
                # english
                newEnglishMarks = input("Enter the new marks obtained in english : ")
                if (not self.validateNumber(newEnglishMarks)):
                    continue
                else:
                    newEnglishMarks=float(newEnglishMarks)
                    if newEnglishMarks<0 or newEnglishMarks>100:
                        self.PRINTINVALIDNUM()
                        continue

                    self.allStudentObjects[index].englishMarks =(float(newEnglishMarks))
                    self.allStudents[index][7] = float(newEnglishMarks)
                print("Updated!")
            elif (thingToUpdate == '9'):
                break
            else:
                print("INVALID OPTION!")
            


        print("All details updated!")

    


        

