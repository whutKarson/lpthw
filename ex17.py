from sys import argv
from os.path import exists
# Got three variables while running the py. 1st is python name, 2nd is destination file, 3rd is target file
script, from_file, to_file = argv
# output msg what the python file is for
print(f"Copying from {from_file} to {to_file} ")

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
# read the content from destination file and write it to target file
# If no variable is assigned, after write(), read() fuction being called, 
# the connetion will be closed by os. no need to run command close() again.
open(to_file, 'w').write(open(from_file).read())
