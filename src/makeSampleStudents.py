#!/usr/bin/env python3
import subprocess
import time
# --user 'als' --pw '123' --name 'Ashton S' --classes 'CPSC 3600' 'CPSC 4620' --hobbies 'weightlifting' 'Basketball'

subprocess.call(['rm', 'db.json'])
subprocess.call(['echo', 'rm db.json'])
subprocess.call(['touch', 'db.json'])
subprocess.call(['echo', 'touch db.json'])

subprocess.call(['python', 'cucodb.py', '--user', 'asobeck', '--pw', '123', '--name', 'Ashton Sobeck', 
                '--email','asobeck@clemson.edu',
                '--classes', 'CPSC 3600', 'CPSC 4620', 'CPSC 3720', 'CPSC 2810', 'CPSC 2310',
                '--hobbies', 'Esports', 'Ping Pong', 'Bowling', 'Track', 'Golf'
                ])

time.sleep(2)

subprocess.call(['python', 'cucodb.py', '--user', 'tsark', '--pw', '456', '--name', 'Tony Stark', 
                '--email','tstark@clemson.edu',
                '--classes', 'CPSC 1010',
                '--hobbies', 'Virtual Reality', 'Music/Music Production', 'Track', 'Videogames', 'Coding'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'tpurp', '--pw', '789', '--name', 'Thanos Purp', 
                '--email','tpurp@clemson.edu',
                '--classes', 'CPSC 3600', 'CPSC 4620', 'CPSC 3720',
                '--hobbies', 'Esports', 'Ping Pong', 'Bowling', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'bwidow', '--pw', '1234', '--name', 'Natasha Widow', 
                '--email','bwidow@clemson.edu',
                '--classes', 'CPSC 1020', 'CPSC 2070', 
                '--hobbies', 'Esports', 'Baseball', 'Soccer', 'Rowing'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'hwkeye', '--pw', '457', '--name', 'Hawk Eye', 
                '--email','hwkeye@clemson.edu',
                '--classes', 'CPSC 2120', 'CPSC 2150', 
                '--hobbies', 'Fencing', 'Photography', 'Field Hockey', 'Frisbee'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'pparker', '--pw', '7728', '--name', 'Peter Parker', 
                '--email','pparker@clemson.edu',
                '--classes', 'CPSC 3600', 'CPSC 4620', 'CPSC 3720', 'CPSC 2810', 'CPSC 2310',
                '--hobbies', 'Esports', 'Photography', 'Bowling', 'Track', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'pquill', '--pw', '2298', '--name', 'Peter Quill', 
                '--email','pquill@clemson.edu',
                '--classes', 'CPSC 1070', 'CPSC 2310',
                '--hobbies', 'Skateboarding', 'Board Games', 'Playing Music'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'mmdock', '--pw', '7783', '--name', 'Matt Murdock', 
                '--email','mmdock@clemson.edu',
                '--classes', 'CPSC 4240', 'CPSC 4910', 'CPSC 4820', 'CPSC 2920',
                '--hobbies', 'Skateboarding', 'Hockey', 'Martial Arts', 'Bowling', 'Cheerleading'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'dpool', '--pw', '9982', '--name', 'Wade Wilson', 
                '--email','dpool@clemson.edu',
                '--classes', 'CPSC 3220', 'CPSC 3720', 'CPSC 4620',
                '--hobbies', 'Virtual Reality', 'Videogames', 'Coding'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'sstrange', '--pw', '2568', '--name', 'Steven Strange', 
                '--email','sstrange@clemson.edu',
                '--classes', 'CPSC 1060', 'CPSC 2070',
                '--hobbies', 'Skateboarding', 'Esports', 'Track', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'dmammu', '--pw', '3647', '--name', 'Dor Mammu', 
                '--email','dmammu@clemson.edu',
                '--classes', 'CPSC 2070', 'CPSC 1070', 'CPSC 2310',
                '--hobbies', 'Esports', 'Cross-Country', 'Archery', 'Photography'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'drax', '--pw', '7466', '--name', 'Drax Drax', 
                '--email','drax@clemson.edu',
                '--classes', 'CPSC 1060',
                '--hobbies', 'Videogames', 'Movies', 'Archery', 'Robotics', 'Virtual Reality'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'fcastle', '--pw', '3689', '--name', 'Frank Castle', 
                '--email','fcastle@clemson.edu',
                '--classes', 'CPSC 3220', 'CPSC 4620', 'CPSC 3720',
                '--hobbies', 'Track', 'Ping Pong', 'Robotics', 'Videogames', 'Movies'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'gmora', '--pw', '3684', '--name', 'Gamora G', 
                '--email','gmora@clemson.edu',
                '--classes', 'CPSC 1070', 'CPSC 2070', 'CPSC 2310',
                '--hobbies', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'grider', '--pw', '123', '--name', 'Johnny Blaze', 
                '--email','grider@clemson.edu',
                '--classes', 'CPSC 3710', 'CPSC 4620', 'CPSC 3720', 'CPSC 4240', 'CPSC 2310',
                '--hobbies', 'Ping Pong', 'Lacrosse', 'Cross-Country', 'Rowing'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'gstacy', '--pw', '3618', '--name', 'Gwen Stacy', 
                '--email','gstacy@clemson.edu',
                '--classes', 'CPSC 2150', 'CPSC 2120', 'CPSC 2310',
                '--hobbies', 'Esports', 'Photography', 'Track', 'Videogames', 'Lacrosse'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'bbanner', '--pw', '38797', '--name', 'Bruce Banner', 
                '--email','asobeck@clemson.edu',
                '--classes', 'CPSC 1020', 'CPSC 2310',
                '--hobbies', 'Esports', 'Videogames', 'Photography', 'Track', 'Basketball'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'jgrey', '--pw', '36593', '--name', 'Jean Grey', 
                '--email','jgrey@clemson.edu',
                '--classes', 'CPSC 3220', 'CPSC 4620', 'CPSC 3720', 'CPSC 2310',
                '--hobbies', 'Esports', 'Ping Pong', 'Bowling'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'ekmonge', '--pw', '3859', '--name', 'Erik Killmonger', 
                '--email','ekmonge@clemson.edu',
                '--classes', 'CPSC 3600', 'CPSC 3220', 'CPSC 3720', 
                '--hobbies', 'Esports', 'Archery', 'Robotics', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'tchalla', '--pw', '37599', '--name', 'T Challa', 
                '--email','tchalla@clemson.edu',
                '--classes', 'CPSC 4820', 'CPSC 4620', 'CPSC 3220',
                '--hobbies', 'Esports', 'Ping Pong', 'Virtual Reality', 'Baseball', 'Volleyball'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'lodinso', '--pw', '375939', '--name', 'Loki Odinson', 
                '--email','lodinso@clemson.edu',
                '--classes', 'CPSC 1010', 'CPSC 2070',
                '--hobbies', 'Esports', 'Ping Pong', 'Archery', 'Movies', 'Coding'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'todinso', '--pw', '4759', '--name', 'Thor Odinson', 
                '--email','todinso@clemson.edu',
                '--classes', 'CPSC 1070', 'CPSC 2810', 'CPSC 2310',
                '--hobbies', 'Photography', 'Coding', 'Basketball', 'Track', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'lcage', '--pw', '12893', '--name', 'Luke Cage', 
                '--email','lcage@clemson.edu',
                '--classes', 'CPSC 3220', 'CPSC 4620', 'CPSC 3220', 'CPSC 2810',
                '--hobbies', 'Esports', 'Baseball', 'Virtual Reality', 'Robotics', 'Movies'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'elehnsh', '--pw', '0976', '--name', 'Eric Lehnsherr', 
                '--email','elehnsh@clemson.edu',
                '--classes', 'CPSC 1020', 'CPSC 2070', 'CPSC 2810',
                '--hobbies', 'Archery', 'Videogames', 'Virtual Reality'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'nfury', '--pw', '39120', '--name', 'Nick Fury', 
                '--email','nfury@clemson.edu',
                '--classes', 'CPSC 3220', 'CPSC 4620', 'CPSC 4820',
                '--hobbies', 'Robotics', 'Ping Pong', 'Videogames', 'Archery', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'fnelson', '--pw', '1980', '--name', 'Foggy Nelson', 
                '--email','fnelson@clemson.edu',
                '--classes', 'CPSC 2070', 'CPSC 1070', 'CPSC 2810', 
                '--hobbies', 'Esports', 'Ping Pong', 'Bowling', 'Track', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'ppotts', '--pw', '821047', '--name', 'Pepper Potts', 
                '--email','ppotts@clemson.edu',
                '--classes', 'CPSC 1020', 'CPSC 2070',
                '--hobbies', 'Esports', 'Basketball', 'Movies', 'Coding', 'Track'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'pcoulson', '--pw', '19347', '--name', 'Phil Coulson', 
                '--email','pcoulson@clemson.edu',
                '--classes', 'CPSC 3600', 'CPSC 4620', 'CPSC 3220',
                '--hobbies', 'Frisbee', 'Football', 'Music/Music Production', 'Track', 'Coding'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'rraccoo', '--pw', '210346', '--name', 'Rocket Raccoon', 
                '--email','rraccoo@clemson.edu',
                '--classes', 'CPSC 1010', 
                '--hobbies', 'Football', 'Swimming', 'Videogames', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'groot', '--pw', '19431781', '--name', 'Groot Groot', 
                '--email','groot@clemson.edu',
                '--classes', 'CPSC 3220', 'CPSC 4620', 'CPSC 4200',
                '--hobbies', 'Esports', 'Movies', 'Swimming', 'Football', 'Virtual Reality'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'ultron', '--pw', '128379', '--name', 'Ultron U', 
                '--email','ultron@clemson.edu',
                '--classes', 'CPSC 4200', 'CPSC 4620', 'CPSC 4910',
                '--hobbies', 'Chess', 'Ping Pong', 'Videogames', 'Movies', 'Virtual Reality'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'stanlee', '--pw', '473862', '--name', 'Stan Lee', 
                '--email','stanlee@clemson.edu',
                '--classes', 'CPSC 3600', 'CPSC 4620', 'CPSC 3220',
                '--hobbies', 'Chess', 'Ping Pong', 'Cooking', 'Archery', 'Drawing/Art'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'venomv', '--pw', '102948', '--name', 'Venom V', 
                '--email','venomv@clemson.edu',
                '--classes', 'CPSC 1010',
                '--hobbies', 'Martial Arts', 'Cooking', 'Playing Music'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'vondoom', '--pw', '09834', '--name', 'Victor VonDoom', 
                '--email','vondoom@clemson.edu',
                '--classes', 'CPSC 4200', 'CPSC 4620', 
                '--hobbies', 'Videogames', 'Ping Pong', 'Coding', 'Skateboarding', 'Golf'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'ssurfer', '--pw', '19285', '--name', 'Silver Surfer', 
                '--email','ssurfer@clemson.edu',
                '--classes', 'CPSC 3600', 'CPSC 4200', 'CPSC 4910',
                '--hobbies', 'Skateboarding', 'Ping Pong', 'Hockey', 'Chess', 'Board Games'
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'jrhodes', '--pw', '98233', '--name', 'James Rhodes', 
                '--email','jrhodes@clemson.edu',
                '--classes', 'CPSC 4200', 'CPSC 3220',
                '--hobbies', 'Cooking', 'Martial Arts', 'Board Games', 'Coding', 
                ])
time.sleep(2)
subprocess.call(['python', 'cucodb.py', '--user', 'slang', '--pw', '127893', '--name', 'Scott Lang', 
                '--email','slang@clemson.edu',
                '--classes', 'CPSC 4200', 'CPSC 3220', 'CPSC 2810', 
                '--hobbies', 'Ping Pong', 'Board Games', 'Virtual Reality', 'Coding'
                ])
exit()