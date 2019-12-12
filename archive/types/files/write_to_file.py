from os import path as path

# file_location = path.absolute(__file__)
file_location = path.dirname(__file__)

''' This method is creating a file and writed something inside.
     Params:
          file_location = at location of 'file_location'
'''


def fileWriter(filename, text, times):
    onlylocation = file_location
    # This line can be written in another way: f = open(file_location + "/" + filename, "w+")
    f = open(onlylocation + ("/{0}.txt".format(filename)), "w+")
    for i in range(times):
        f.write(f"This is line {i + 1} - {text}\n")
    f.close()
    return print(f"The file(s):{__file__} written successfully.")


# TODO: Finish the writing files from dictionary key : value.
try:
    filenames_dict = [{'file1': ("file_test", "the text", 12)},
                      {'file2': ("file_test2", "the text2", 12)},
                      {'file3': ("file_test3", "the text3", 12)}]
    # file1 = fileWriter("file_test", "the text", 12)
    # file2 = fileWriter("file_test2", "the text2", 12)
    # file3 = fileWriter("file_test3", "the text3", 12)
    for filenames in filenames_dict:
        # File writes with dictionary
        filenameget = open(fileWriter(filenames_dict.pop(len(filenames_dict))))

except:
    print("Unable to write the file.")


def filenames(filename):
    result_filename = filename
    print(result_filename)
    return result_filename


printfilename = ("Location of files: " + file_location)
print(printfilename)
