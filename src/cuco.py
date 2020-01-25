class Student:
    ID = 1
    Hobbies = []
    Classes = []
    Name = []
    unhash
    pwhash
    totalDistance = []

    # default constructor 
    def __init__(self, id, hobbies, classes, name, hasval1, hasval2): 
        self.ID = id
        self.Hobbies = hobbies
        self.Classes = classes
        self.Name = name
        self.unhash = hasval1
        self.pwhash = hasval2
        self.totalDistance = 0
    
    
