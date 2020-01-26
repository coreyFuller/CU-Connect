import json #needed to read in JSON File


class Student:
    ID = 0
    Hobbies = []
    Classes = []
    Name = []
    totalDistance = 0
    matchAverage = 0

    # default constructor 
    def __init__(self, idval, name, hobbies, classes): 
        self.ID = idval
        self.Name = name
        self.Hobbies = hobbies
        self.Classes = classes
        self.totalDistance = 0
        self.matchAverage = 0

studentList = []

#maps of classes to a distance line 
classDict = {
    "CPSC 1010" : 0,
    "CPSC 1060" : 20,
    "CPSC 1070" : 0,
    "CPSC 1010" : 5,
    "CPSC 1060" : 20,
    "CPSC 1020" : 50,
    "CPSC 1070" : 70,
    "CPSC 2070" : 100,
    "CPSC 2120" : 125,
    "CPSC 2150" : 135,
    "CPSC 2310" : 160,
    "CPSC 3220" : 210,
    "CPSC 3720" : 220,
    "CPSC 3600" : 235,
    "CPSC 3710" : 240,
    "CPSC 4200" : 300,
    "CPSC 4240" : 310,
    "CPSC 4620" : 335,
    "CPSC 4910" : 350,
 }

# maps hobbies to a distance
classHobbies = {
    "-nan" : 0,
    "Coding" : 5,
    "Virtual Reality" : 7,
    "Video games" : 8,
    "Robotics" : 12,
    "Movies" :  14,
    "Music/Music Production" : 16,
    "Photography" : 25,
    "Archery" : 100,
    "Basketball" : 150,
    "Baseball" : 200,
    "Track" : 250,
    "Cross-Country" : 260,
    "Volleyball" : 300,
    "Lacrosse" : 350,
    "Soccer" : 370,
    "Softball" : 220,
    "Swimming" : 1500,
    "Football" : 600,
    "Rowing" : 800,
    "Field Hockey" : 1000,
    "Bowling" : 1300,
    "Golf" : 1600,
    "Frisbee" :  410,
    "Ping Pong" : 2000,
    "Cheerleading" : 2200,
    "Fencing" : 2400,
    "Esports" : 5,
    "Skateboarding" : 2800,
    "Hockey" : 1100,
    "Chess" : 3000,
    "Drawing/Art" : 5000,
    "Cooking" : 4000,
    "Playing music" : 5500,
    "Martial arts" : 6000,
    "Board games" : 3300,
}


#holds the similarity ratio for the all students to
#the one being matched

#read in info from the JSON file and pass it to an array of objects
#build objects by putting info in the constructors

def calcDistances(StudentA, StudentB):
    totalDist = 0
    for x in range(5):
        totalDist += abs(classHobbies[StudentA.Hobbies[x]] - classHobbies[StudentB.Hobbies[x]])
    aStudClassVal = 0
    bStudClassVal = 0
#Calculating mean value of Student A's classes
    for x in StudentA.Classes:
        aStudClassVal += classDict[x]
    aStudClassVal /= len(StudentB.Classes)
    #Calculating mean value of Student B's classes
    for x in StudentB.Classes:
        bStudClassVal += classDict[x]
    bStudClassVal /= len(StudentB.Classes)
    #Finding difference between mean values of A's classes and B's classes
    totalDist += abs(aStudClassVal - bStudClassVal)
    return totalDist

def matchStudents(students):
    students.sort(key = lambda x: x.matchAverage)
    matched = students[:5]
    return match

#for all students in list
    # find the total distace for all 10 dimensions from user to each student
    # store average of distances total in student object






#sort based on average
# return 10 student objects


def main():
    student1 = (1, ["Coding", "Virtual Reality"], ["CPSC 1010", "CPSC 1020"], ["Bob", "Smith"], 1000, 1002)
    student2 = (2, ["Coding", "Virtual Reality"], ["CPSC 1060", "CPSC 2120"], ["Annie", "Hill"], 1003, 1004)
    x = calcDistances(student1, student2)
    print(x)
    print("testing yo")
    
    with open('db.json') as json_file:
        data = json.load(json_file)
        for s in data['students']:
            studentList.append(Student(s['ID'], s['name'], s['hobbies'], s['classes']))

    
# if __name__ == 'main':
main()
        