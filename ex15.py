# import argv model from sys model.
from sys import argv
# Got filename from input of user
filename = input("Please input your filename: ")
# Got the file object by calling open function with fileName variable
txt = open(filename)

# output the msg with formatter
print(f"Here's your file {filename}:")
# call the read() function of file object 'txt_again' and return the content of file. Then call print function to output those content
print(txt.read())

# close the open
txt.close()
