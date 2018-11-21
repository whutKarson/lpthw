from sys import argv

script, input_file = argv
# output all the contents of file
def print_all(f):
	print(f.read())
# reset the location of file reader to be head of file.
def rewind(f):
	f.seek(0)
# output the line number readed and the content of line
def print_a_line(line_count, f):
	print(line_count, f.readline())
# open the target file and assigned it to a variable as file object
current_file = open(input_file)

print("First let's print the whole file: \n")
# output all the contents of file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# reset the location of reader to be the head of file
rewind(current_file)

print("Let's print three lines:")
# setup a counter for counting what's the line have readed. and output it
current_line = 1
print_a_line(current_line, current_file)
# counter number add one once called print_a_line method, in order to sync the line nunber have readed
current_line +=  + 1
print_a_line(current_line, current_file)

# counter number add one once called print_a_line method, in order to sync the line nunber have readed
current_line +=  + 1
print_a_line(current_line, current_file)
