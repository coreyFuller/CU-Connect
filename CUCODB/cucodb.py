#!/usr/bin/env python3

import json
import argparse
import os
import hashlib

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

# d["students"][0]["name"]
# for student in d["students"]:
#     student["name"]

# for key in d:
#     print(key)
#     d[key]

json_data = {}
if os.stat("db.json").st_size != 0:
    with open("db.json", "r") as json_file:
        json_data = json.load(json_file)
else:
    json_data['students'] = []
#UID = len(json_data) + 1
json_data['students'].append({
    'name'       : args.name,
    'username'   : args.user,
    'password'   : hash_password(args.pw),
    'classes'    : args.classes,
    'hobbies'    : args.hobbies,
    'connections': []
})


with open('db.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
    # json.dump(json_data, json_file)
