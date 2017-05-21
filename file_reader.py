# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)


# this opens the pi digits file, reads it, and then prints out the text to the screen.

# you first need to open the file to access it. the open() function needs one argument, the name of the file. python looks for this file in the same directory that the python program is running in.

# the with keyword will close the file once access to it is no longer needed. you could use close() but this can lead to easy mistakes

# if this file wasn't in the same directory as the python program, you could give a relative file path.

# with open('text_files/filename.txt') as file_object

# Or use the full file path if needed



# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
