def count_words(filename):
    """count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "sorry the file " + filename + " does not exist."
        print(msg)
        # if you wanted a silent fail, meaning no traceback was shown on screen but the program continued to run anyways
        # you can use the pass command
        
    # except FileNotFoundError:
    #     pass
    else:
        #Count approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+" has about "+str(num_words) + " words.")

# filename = 'alice.txt'
# count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt','/home/sid/python_work/files_exceptions/pcc/chapter_10/moby_dick.txt', 'pcc/chapter_10/little_women.txt']
for file in filenames:
    count_words(file)
