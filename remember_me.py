import json


#load the username, if it has been previously stored. otherwise prompt for the username and store it


filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we'll remember you when you come back, " + username+ "!")
else:
    print("welcome back, "+username+"!")
