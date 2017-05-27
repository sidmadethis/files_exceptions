import json


#load the username, if it has been previously stored. otherwise prompt for the username and store it

# def greet_user():
#     """greet user by name"""
#
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("what is your name?")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("we'll remember you when you come back, " + username+ "!")
#     else:
#         print("welcome back, "+username+"!")
#
# greet_user()

# refactoring is breaking up large chunks of code into series of functions that have specific jobs



def get_stored_username():
    """get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
        # the None keyword is good for testing functions. function should return a value or None
    else:
        return username


def get_new_username():
    """prompt for a new username"""
    username = input("what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back, "+username+"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, "+ username+"!")


greet_user()

# this is a little better
# refactored again, each function has a clear purpose
