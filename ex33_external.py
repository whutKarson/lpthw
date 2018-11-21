numbers = []

def add_numbers(endNumber, step):
	i = 0
	while i < endNumber:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + step

		print("Numbers now: ", numbers)
		print(f"At the botoom i is {i}")

add_numbers(10, 2)

print("The numbers: ")

for num in numbers:
	print(num)