
import random


class Student:
    def __init__(self, name, age, subjects, grades):
        self.name = name
        self.age = age
        self.subjects = subjects
        self.grades = grades
        self.m=max(self.grades)
        self.avg= sum(self.grades)/len(self.grades)
    def studinfo(self):
        print(f'Name : {self.name}, Age: {self.age}, Subjects: {self.subjects}, Grades: {self.grades}, Max Grade: {self.m}, Average Grade: {self.avg} ')
    def retrain(self,studytime):
        for i in range(len(self.grades)):
            self.grades[i]=self.grades[i]+random.randint(-studytime, 5*studytime)
        self.m=max(self.grades)
        self.avg= sum(self.grades)/len(self.grades)

def randstudgen(n):
    stud=[]
    times=[]
    for i in range(n):
        s=Student(f'rufus_{i}',random.randint(2,17),['Math', 'English', 'Capy'], [random.randint(0,100),random.randint(0,100),random.randint(0,100)])
        stud.append(s)
        times.append(random.randint(0,10))
    return stud, times
class School:
    def __init__(self,students:list[Student]):
        self.students=students
        
    def big(self):
        avlist=[]
        for i in self.students:
            avlist.append(i.avg)
        print(f'Maximum Average Score: {max(avlist)}')
        return avlist
    def schoolinfo(self):
        for i in self.students:
            i.studinfo()
    def fail(self):
        failist=[]
        print(f'Failed:')
        for i in self.students:
            if i.avg<49:
                failist.append(i) 
                i.studinfo()
        if len(failist)==0:
            print("No Students Failed :)")
        return failist
    def retrain(self, studytimes):
        for i,j in zip(self.students,studytimes):
            i.retrain(j)
        print('------------------------------Retraining Complete-------------------------------')



stud1, times1=randstudgen(100)
GelEvosmou=School(stud1)
# GelEvosmou.schoolinfo()
GelEvosmou.big()  
failist=GelEvosmou.fail()

SummerSchool=School(failist)
SummerSchool.schoolinfo()
SummerSchool.retrain(times1)
SummerSchool.schoolinfo()
SummerSchool.big()



