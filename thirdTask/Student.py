# Every student must have the following as his/her details:
#  Name, Admission number, Roll number, 
# Class, Science marks, Maths marks, Social studies marks and English marks
import statistics as stat


# this class has been made to make it easy for storing the values
# and to make appropriate changes and calculations
class Student():
    def __init__(self,name,admissionNumber,rollNumber,cl,scienceMarks,mathsMarks,SSTMarks,englishMarks):
        self.name =  name
        self.admissionNumber = admissionNumber
        self.rollNumber = rollNumber
        self.cl = cl
        self.scienceMarks = scienceMarks
        self.mathsMarks = mathsMarks
        self.SSTMarks = SSTMarks
        self.englishMarks = englishMarks

    def __str__(self) -> str:
        return f"{self.name} | {self.getAggregate()}%"

    def getAggregate(self):
        return stat.mean([self.scienceMarks,self.mathsMarks,self.SSTMarks,self.englishMarks])

    def isInMeritList(self):
        if (self.scienceMarks<90 or self.mathsMarks<90 or self.SSTMarks < 90 or self.englishMarks <90):
            return False
        return True
    def returnList(self):
        return [self.name,self.admissionNumber,self.rollNumber,self.cl,self.scienceMarks,self.mathsMarks,self.SSTMarks,self.englishMarks]
    
    

    

