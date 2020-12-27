from Student import Student
from tabulate import tabulate
import numpy as np
#  Name, Admission number, Roll number, 
# Class, Science marks, Maths marks, Social studies marks and English marks

class ReportCard():
    def __init__(self,allStudents,headings):
        self.allStudents  = allStudents
        self.headings = headings
    def display(self):
        print(tabulate(self.allStudents,self.headings))
        quit = input("Press enter to quit.")
        return
    def validateNumber(self,num):
        if (not num.isnumeric() or int(num)<=0):
            print("INVALID\nPlease make sure that you have entered only numeric values")
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

        englishMarks = input("Enter the marks obtained in English")                
        if (not self.validateNumber(englishMarks)):
            return False
        englishMarks = (englishMarks)

        #Everything entered is valid
        newStudent = Student(name,admissionNumber,rollNumber,cl,scienceMarks,mathsMarks,SSTMarks,englishMarks)
        self.allStudents = np.append(self.allStudents,[newStudent])
    
    def updateDetails(self,index):
        thingToUpdate = "1"
        if (not thingToUpdate.isnumeric()):
            print("Invalid!")
        while (thingToUpdate != "9"):
            thingToUpdate = input("Enter the attribute to update :\n1. Name\n2. Admission number\n3. Roll number\n4. Class\n5. Science Marks\n6. Maths Marks\n7. SST Marks\n8. English Marks\n9. Quit")
            if (thingToUpdate == '1'):
                newName = input("Enter the new name of the student : ")
                if (not self.validateString(newName)):
                    continue
                else:
                    self.allStudents[index].name = newName
                    print("Updated!")
            elif (thingToUpdate == '2'):
                newAdmissionNumber = input("Enter the new admission number of the student : ")
                if (not self.validateNumber(newAdmissionNumber)):
                    continue
                
                else:
                    self.allStudents[index].admissionNumber=  (newAdmissionNumber)
                    print("Updated!")
            elif (thingToUpdate == '3'):
                newRollNumber = input("Enter the new roll number of the student : ")
                if (not self.validateNumber(newRollNumber)):
                    continue
                else:
                    self.allStudents[index].rollNumber = (newRollNumber)
                    print("Updated!")
            elif (thingToUpdate == '4'):
                newClass = input("Enter the new standard of the student :(NUMERIC ONLY) ")
                if (not self.validateNumber(newClass)):
                    continue
                else:
                    self.allStudents[index].cl = int(newClass)
                    print("Updated!")
            elif (thingToUpdate  == '5'):
                # science   
                newScienceMarks = input("Enter the new marks obtained in science : ")
                if (not self.validateNumber(newScienceMarks)):
                    continue
                else:
                    self.allStudents[index].scienceMarks = (newScienceMarks)
                    print("Updated!")
            
            elif (thingToUpdate == '6'):
                # maths
                newMathsMarks = input("Enter the new marks obtained in maths : ")
                if (not self.validateNumber(newMathsMarks)):
                    continue
                else:
                    self.allStudents[index].mathsMarks = (newMathsMarks)
                    print("Updated!")

            elif (thingToUpdate == '7'):
                # sst
                newSSTMarks = input("Enter the new marks obtained in SST : ")
                if (not self.validateNumber(newSSTMarks)):
                    continue
                else:
                    self.allStudents[index].SSTMarks = (newSSTMarks)
                print("Updated!")

            elif (thingToUpdate == '8'):
                # english
                newEnglishMarks = input("Enter the new marks obtained in english : ")
                if (not self.validateNumber(newEnglishMarks)):
                    continue
                else:
                    self.allStudents[index].englishMarks =(newEnglishMarks)
                print("Updated!")
            elif (thingToUpdate == '9'):
                break
            else:
                print("INVALID OPTION!")
            


        print("All details updated!")

    


        

