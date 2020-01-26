#!/usr/bin/env python3

import json
import argparse
import os
import hashlib

# using the sha256 hash method, hashes passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

get_args = argparse.ArgumentParser()

get_args.add_argument(
    "--user",
    type=str,
    default="",
)

get_args.add_argument(
    "--pw",
    type=str,
    default="",
)

get_args.add_argument(
    "--name",
    type=str,
    default=""
)

get_args.add_argument(
    "--email",
    type=str,
    default=""
)

get_args.add_argument(
    "--classes",
    nargs="*",
    type=str,
    default=[],
)

get_args.add_argument(
    "--hobbies",
    nargs="*",
    type=str,
    default=[],
)

#parse the arguments
args = get_args.parse_args()

# makes all class & hobby lists 5 no matter what is passed in
if len(args.classes) != 5:
    args.classes.extend(["-nan" for i in range (5 - len(args.classes))])
if len(args.hobbies) != 5:
    args.hobbies.extend(["-nan" for i in range (5 - len(args.hobbies))])    


json_data = {}
# Checks if the file is empty or not
# if so, then it makes an empty dictionary instead of trying to open an empty file
if os.stat("db.json").st_size != 0:
    with open("db.json", "r") as json_file:
        json_data = json.load(json_file)
else:
    json_data['students'] = []
# TODO: fix how this is calculated - rn is only 2 all the time
UID = len(json_data) + 1
# formatting the json data
json_data['students'].append({
    'name'       : args.name,
    'username'   : args.user,
    'password'   : hash_password(args.pw),
    'UID'        : UID,
    'email'      : args.email,
    'classes'    : args.classes,
    'hobbies'    : args.hobbies,
    'connections': []
})

# pretty prints the json data to the db file
with open('db.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
