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
    def studinfoshort(self):
        print(f'Name : {self.name}, Age: {self.age}, Average Grade: {self.avg} ')
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
    
    def best(self,subject):
      
        chosen=[]
        while len(chosen)<2:
            i=random.randint(0,len(self.students)-1)
            p=self.students[i]
            if p.grades[subject]>80:
                chosen.append(p)
        return chosen
        
    def retrain(self, studytimes):
        for i,j in zip(self.students,studytimes):
            i.retrain(j)
        print('------------------------------Retraining Complete-------------------------------')


def schoolgen(n,m): 
    schoolist=[]
    for i in range(n):
        stud2,times2=randstudgen(m)
        k=School(stud2)
        schoolist.append(k)
    return schoolist, times2

class Competition:
    def __init__(self,schools:list[School]):
        self.schools=schools

    def runcompetition(self, subject, subcomp:list[Student]):
        points=[]
 
        for i in subcomp: 

            points.append(random.random()*i.grades[subject])
        subwinner=subcomp[points.index(max(points))]
        winnerpoints=max(points)
        return subwinner, winnerpoints
        
    def runall(self,comp):
        winners=[]
        points=[]
        for i in range(3):
            z,point=self.runcompetition(i,comp[i])
            winners.append(z)
            points.append(point)
        print(f"The big winners are: ")
        subjectlist=['Math','English','Capy']
        for  i,j,p in zip(range(3),winners,points):
            print(f'{i+1}) Winner in {subjectlist[i]}: ')
            j.studinfoshort()
            print(f'Score: {p}')
        return winners
        
        

def main1():
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

def main2():
    skg_schools,times_s=schoolgen(10,100)
    subcomp1=[]
    subcomp2=[]
    subcomp3=[]
    for i in skg_schools:
        subcomp1.append(i.best(0)[0])
        subcomp1.append(i.best(0)[1])

        subcomp2.append(i.best(1)[0])
        subcomp2.append(i.best(1)[1])

        subcomp3.append(i.best(2)[0])
        subcomp3.append(i.best(2)[1])


    comp=[subcomp1,subcomp2,subcomp3]
    capySEEMUS=Competition(skg_schools)
    capySEEMUS.runall(comp)


main2()
