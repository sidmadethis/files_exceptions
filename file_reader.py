with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


# this opens the pi digits file, reads it, and then prints out the text to the screen.

# you first need to open the file to access it. the open() function needs one argument, the name of the file. python looks for this file in the same directory that the python program is running in.

# the with keyword will close the file once access to it is no longer needed. you could use close() but this can lead to easy mistakes
