from Student import Student
from tabulate import tabulate
import numpy as np
import shutil


#  Name, Admission number, Roll number, 
# Class, Science marks, Maths marks, Social studies marks and English marks
def printCenter(string):
        return ((string).center(shutil.get_terminal_size().columns))


class ReportCard():
    def __init__(self,allStudents,headings):
        self.allStudentObjects= allStudents
        self.allStudents  = []
        for i in allStudents:
            self.allStudents.append(i.returnList())
        self.headings = headings

    def getAggregateList(self):
        print(printCenter("STUDENTS WHO PASSED AGGREGATE\n"))
        aggregateStudents  = list(filter(lambda x : x.getAggregate()>=90,self.allStudentObjects))
        self.printRanked(aggregateStudents)


    def searchByName(self,name):
        length = len(self.allStudentObjects)
        srting = 'fsdf'

        for i in range(length):
            if ((self.allStudentObjects[i].name).lower() == name.lower()):
                return i
        return -1


    def searchByRollNumber(self,number):
        length = len(self.allStudentObjects)
        for i in range(length):
            if (self.allStudentObjects[i].rollNumber == number):
                return i
        return -1
    
    def searchByClass(self,cl):
        length = len(self.allStudentObjects)
        for i in range(length):
            if (self.allStudentObjects[i].cl == cl):
                return i
        return -1



    def searchStudent(self):
        while (1):
            parameter = input("""\n
            1.Search by name\n2.Search by roll number\n3. Search by class
            \n4.Quit\nEnter your option : 
        """)
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
                if (index == -1):
                    printCenter("\nSTUDENT NOT FOUND!\n")
                    return
                else:
                    self.updateDetails(index)
                        

    def parameter(self,student):
        return student.getAggregate()

    def printRanked(self,ranked):
        counter=1
        for i in ranked[:10]:
            print(printCenter(str(counter)+'.' +str(i)))
            counter+=1
        input("Press enter to continue : ")

    def rankStudents(self):
        print(printCenter("RANKS SCORED ABOVE AGGREGATE\n"))
        ranked = self.allStudentObjects
        ranked.sort(key=self.parameter,reverse=True)
        self.printRanked(ranked)
        
    def PRINTINVALIDNUM(self):
        print("INVALID\nPlease make sure that you have entered only numeric values")

    def display(self):
        print(tabulate(self.allStudents,self.headings))
        quit = input("Press enter to quit.")
        return
    def validateNumber(self,num):
        if (not num.isnumeric() or int(num)<=0):
            self.PRINTINVALIDNUM()
            return False
        return True
    def validateString(self,string):
        if (not string.isalpha()):
            print("INVALID NAME.\nPlease make sure that you have entered only characters for the name")
            return False
        return True
    def addStudent(self):
        name = input("Enter the name of the student : ")
        if (not self.validateString(name)):
            return False
        
        admissionNumber = input("Enter the admission number of the student : ")
        if (not self.validateNumber(admissionNumber)):
            return False
        admissionNumber = (admissionNumber)
        
        rollNumber = input("Enter the roll number of the student : ")
        if (not self.validateNumber(rollNumber)):
            
            return False
        rollNumber = (rollNumber)

        cl = input("Enter the standard of the student(IN NUMERIC FORM) : ")
        if (not self.validateNumber(cl)):
            return False
        scienceMarks = input("Enter the marks obtained in Science : ")
        
        if (not self.validateNumber(scienceMarks)):
            return False
        scienceMarks = (scienceMarks)

        mathsMarks = input("Enter the marks obtained in Maths : ")
        if (not self.validateNumber(mathsMarks)):
            return False

        mathsMarks = (mathsMarks)

        SSTMarks = input("Enter the marks obtained in SST : ") 
        if (not self.validateNumber(SSTMarks)):
            return False
        SSTMarks = (SSTMarks)

        englishMarks = input("Enter the marks obtained in English : ")                
        if (not self.validateNumber(englishMarks)):
            return False
        englishMarks = (englishMarks)

        #Everything entered is valid
        newStudent = Student(name,admissionNumber,rollNumber,cl,scienceMarks,mathsMarks,SSTMarks,englishMarks)
        self.allStudentObjects = np.append(self.allStudentObjects,[newStudent])
        self.allStudents.append(newStudent.returnList())
    
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
                    self.allStudentsObjects[index].cl = (int(newClass))
                    self.allStudents[index][3] = int(newClass)
                    print("Updated!")
            elif (thingToUpdate  == '5'):
                # science   
                newScienceMarks = input("Enter the new marks obtained in science : ")
                if (not self.validateNumber(newScienceMarks)):
                    continue
                else:
                    self.allStudentObjects[index].scienceMarks = (float(newScienceMarks))
                    self.allStudents[index][4] = float(newScienceMarks)
                    print("Updated!")
            
            elif (thingToUpdate == '6'):
                # maths
                newMathsMarks = input("Enter the new marks obtained in maths : ")
                if (not self.validateNumber(newMathsMarks)):
                    continue
                else:
                    self.allStudentObjects[index].mathsMarks = (float(newMathsMarks))
                    self.allStudents[index][5] = float(newMathsMarks)
                    print("Updated!")

            elif (thingToUpdate == '7'):
                # sst
                newSSTMarks = input("Enter the new marks obtained in SST : ")
                if (not self.validateNumber(newSSTMarks)):
                    continue
                else:
                    self.allStudentObjects[index].SSTMarks = (float(newSSTMarks))
                    self.allStudents[index][6] = float(newSSTMarks)
                print("Updated!")

            elif (thingToUpdate == '8'):
                # english
                newEnglishMarks = input("Enter the new marks obtained in english : ")
                if (not self.validateNumber(newEnglishMarks)):
                    continue
                else:
                    self.allStudentObjects[index].englishMarks =(float(newEnglishMarks))
                    self.allStudents[index][7] = float(newEnglishMarks)
                print("Updated!")
            elif (thingToUpdate == '9'):
                break
            else:
                print("INVALID OPTION!")
            


        print("All details updated!")

    


        

