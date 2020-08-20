import json #needed to read in JSON File
import os 
cwd = os.getcwd()

print(cwd)
with open(cwd + '\hobbies.json') as hobbies: 
    hobbyValues = json.load(hobbies)

with open(cwd + '\classes.json') as classes:
     classValues = json.load(classes)
     
with open(cwd + '\db.json') as studentDB:
    students = json.load(studentDB)



class Student:
    ID = 0
    Hobbies = []
    Classes = []
    Name = " "
    Email = " "
    totalDistance = 0
    matchAverage = 0

    # default constructor 
    def __init__(self, idval, name, email, hobbies, classes): 
        self.ID = idval
        self.Name = name
        self.Hobbies = hobbies
        self.Classes = classes
        self.Email = email
        self.totalDistance = 0
        self.matchAverage = 0
    def display(self):
        print(self.ID, self.Email, self.Name, self.Hobbies, self.Classes)

studentList = []

#holds the similarity ratio for the all students tof
#the one being matched

#read in info from the JSON file and pass it to an array of objects
#build objects by putting info in the constructors

def calcDistances(StudentA, StudentB):
    hobbyDist = 0
    classDist = 0
    for x in range(5):
        hobbyDist += abs(hobbyValues[StudentA.Hobbies[x]] - hobbyValues[StudentB.Hobbies[x]])
    hobbieMean = hobbyDist / 5
    #Calculating mean value of Student B's classes
    for x in range(5):
        classDist += abs(classValues[StudentA.Classes[x]] - classValues[StudentB.Classes[x]])
    classMean = classDist / 5
    #Finding difference between mean values of A's classes and B's classes
    totalDist = classMean + hobbieMean
    return totalDist

def matchStudents(students):
    #sorts objects based on average
    students.sort(key = lambda x: x.totalDistance)
    #creates list of top 5 matches
    matched = students[:5]
    #returns list
    return matched


with open('db.json') as json_file:
    data = json.load(json_file)
    for s in data['students']:
        studentList.append(Student(s['UID'], s['name'], s['email'], s['hobbies'], s['classes']))
matchStudent = studentList.pop()
    
    #for all students in list
    # find the total distace for all 10 dimensions from user to each student
    # store average of distances total in student object
for x in studentList:
    x.totalDistance += calcDistances(matchStudent, x);
    
    #sort based on average
    # return 10 student objects   
print("Scott Lang: ")
matchStudent.display()
print("\n")
print("Here are " + matchStudent.Name + "'s matches: ")
matched = matchStudents(studentList)  
for x in matched:
    x.display()

        