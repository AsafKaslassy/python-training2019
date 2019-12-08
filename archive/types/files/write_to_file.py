from pathlib import Path
import os

file_location = Path(__file__).absolute()


def fileWriter(filename, text, times):
     f = open(f"{filename}.txt", "w+")
     for i in range(times):
          f.write(f"This is line {i + 1} - {text}\n")
     f.close()


try:

     file1 = fileWriter("file_test", "the text", 12)
     file2 = fileWriter("file_test2", "the text2", 12)
     file3 = fileWriter("file_test3", "the text3", 12)
     for filenames in file1:
          filenameget = open(file1)
     print(f"The file(s):{filenameget.name},{file2},{file3} written successfully.")

except:
     print("Unable to write the file.")


def filenames(filename):
     result_filename = filename
     print(result_filename)
     return result_filename


printfilename = os.path.basename(file1.name)
