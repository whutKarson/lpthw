
# function that count the sum value of two arguments
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

# function that count the value of a - b
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b
# fucntion that count the value of a * b
def multiply(a, b):
	print(f"MULTIPLYING {a} - {b}")
	return a * b

# function that count the value of a / b
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

print("Let's do some match with just functions!")
# define variable age , its' value is returned by called add function
age = add(30, 5)
# define variable height , its' value is returned by called subtract function
height = subtract(78, 4)
# define variable weight , its' value is returned by called multiply function
weight = multiply(90, 2)
# define variable divede , its' value is returned by called multiply function
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzele.")

# Do a complex math count with add, subtract, multiply, divide.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

