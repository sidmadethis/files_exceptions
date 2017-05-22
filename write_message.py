filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("i love programming.\n")


# w is write mode, r is read mode, a is append mode
with open(filename, 'a') as file_object:
    file_object.write("I also love to use big data.\n")
    file_object.write("i love creating apps that can be run in a browser.\n")
