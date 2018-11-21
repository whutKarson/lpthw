'''
Some function about file object.
close: close the file connection
read: read all the content of file
readline: read one line of content of file each time
truncate: Clear the content of file
write('stuff'): write 'stuff' into file
seek(0): move the w/r location to the head of content

'''
from sys import argv
# get filename and script name from argv
script, filename = argv

formater = "{}\n{}\n{}"

# output msg to user to make decision whether clear content of ile or not
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# output msg to ask user to confirm clear or cancel clear action
input("?")
# output msg to prompt the user the file is opening.
print("Opening the file...")
# open the file with filename in write model.
target = open(filename, 'w')
# output msg to prompt the user the content will be clear.
print("Truncating the file. Goodbye!")
# clear the content of file
target.truncate()
# print the prompt msg that will ask 3 lines of content which will be wrote into file
print("Now I'm going to ask you for three lines.")

# prompt msg to ask user to input msg and return the msg as line1
line1 = input("line1: ")
# prompt msg to ask user to input msg and return the msg as line2
line2 = input("line2: ")
# prompt msg to ask user to input msg and return the msg as line3
line3 = input("line3: ")
# print the prompt msg that will write content to file
print("Now I'm going to write these to the file.")
# add the content of line1 to the file
target.write(formater.format(line1, line2, line3))


# print the prompt msg
print("And finally, we close it.")
# close the file connection
target.close()

