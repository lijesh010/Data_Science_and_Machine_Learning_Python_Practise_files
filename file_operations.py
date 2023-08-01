'''
Exercise 9:
Create a Python module named file_operations that contains functions to read and write text files.
Write a program to use this module to read the contents of a file and write the contents to a new file.
'''
#creating the module.
def read_file(path):
    file1=open(path,"r")
    return file1.read()
def write_file(path,content):
    file1=open(path,"w")
    file1.write("hello world")
    file1.close()