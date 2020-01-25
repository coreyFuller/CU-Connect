import json #needed to read in JSON File


class Student:
    ID = 1
    Hobbies = []
    Classes = []
    Name = []
    unhash
    pwhash
    totalDistance = []
    matchAverage = [] 

    # default constructor 
    def __init__(self, id, hobbies, classes, name, hasval1, hasval2): 
        self.ID = id
        self.Hobbies = hobbies
        self.Classes = classes
        self.Name = name
        self.unhash = hasval1
        self.pwhash = hasval2
        self.totalDistance = 0

#maps of classes to a distance line 
classDict = {
    "CPSC 1010" : 0,
    "CPSC 1060" : 20
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
    "Coding" :
    "Virtual Reality" :
    "Video games" :
    "Robotics" :
    "Movies" : 
    "Music/Music Production" :
    "Photography" :
    "Archery" :
    "Basketball" :
    "Baseball" :
    "Track" :
    "Cross-Country" :
    "Volleyball" :
    "Lacrosse" :
    "Soccer" :
    "Softball" :
    "Swimming" :
    "Football" :
    "Rowing" :
    "Field Hockey" :
    "Bowling" :
    "Golf" :
    "Frisbee" :
    "Ping Pong" :
    "Cheerleading" :
    "Fencing" :
    "Esports" :
    "Skateboarding" :
    "Hockey" :
}

#holds the similarity ratio for the all students to
#the one being matched

#read in info from the JSON file and pass it to an array of objects
#build objects by putting info in the constructors

#for all students in list
    # find the total distace for all 10 dimensions from user to each student
    # store average of distances total in student object

#sort based on average

# for 10 iterations
    # return/display student objects
