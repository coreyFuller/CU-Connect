#!/usr/bin/env python3

import json #needed to read in JSON File


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

#maps of classes to a distance line 
classDict = {
    "-nan" : 0,
    "CPSC 1010" : 5,
    "CPSC 1060" : 20,
    "CPSC 1020" : 50,
    "CPSC 1070" : 70,
    "CPSC 2070" : 200,
    "CPSC 2120" : 230,
    "CPSC 2920" : 210,
    "CPSC 2150" : 250,
    "CPSC 2310" : 270,
    "CPSC 2810" : 290,
    "CPSC 3220" : 300,
    "CPSC 3720" : 330,
    "CPSC 3600" : 380,
    "CPSC 3710" : 350,
    "CPSC 4200" : 420,
    "CPSC 4240" : 424,
    "CPSC 4620" : 462,
    "CPSC 4820" : 482,
    "CPSC 4910" : 491,
 }

# maps hobbies to a distance
classHobbies = {
    "-nan" : 0,
    "Coding" : 5,
    "Virtual Reality" : 100,
    "Videogames" : 120,
    "Robotics" : 15,
    "Movies" :  500,
    "Music/Music Production" : 290000,
    "Photography" : 700,
    "Archery" : 100,
    "Basketball" : 1500,
    "Baseball" : 2000,
    "Track" : 3000,
    "Cross-Country" : 3300,
    "Volleyball" : 4000,
    "Lacrosse" : 5000,
    "Soccer" : 6000,
    "Softball" : 2500,
    "Swimming" : 8000,
    "Football" : 10000,
    "Rowing" : 12000,
    "Field Hockey" : 15000,
    "Bowling" : 20000,
    "Golf" :150000 ,
    "Frisbee" :  26000,
    "Ping Pong" : 30000,
    "Cheerleading" : 40000,
    "Fencing" : 50000,
    "Esports" : 140,
    "Skateboarding" : 60000,
    "Hockey" : 16000,
    "Chess" : 220000,
    "Drawing/Art" :  750,
    "Cooking" : 75000,
    "Playing Music" : 300000 ,
    "Martial Arts" : 80000,
    "Board Games" : 200000,
}


#holds the similarity ratio for the all students tof
#the one being matched

#read in info from the JSON file and pass it to an array of objects
#build objects by putting info in the constructors

def calcDistances(StudentA, StudentB):
    hobbyDist = 0
    classDist = 0
    for x in range(5):
        hobbyDist += abs(classHobbies[StudentA.Hobbies[x]] - classHobbies[StudentB.Hobbies[x]])
    hobbieMean = hobbyDist / 5
    #Calculating mean value of Student B's classes
    for x in range(5):
        classDist += abs(classDict[StudentA.Classes[x]] - classDict[StudentB.Classes[x]])
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

def main():
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
    print("Here are " + matchStudent.Name + "'s matches: ")
    print("\n")
    matchStudent.display()
    print("\n")
    matched = matchStudents(studentList)  
    for x in matched:
        x.display()

    
if __name__ == '__main__':
    main()
        