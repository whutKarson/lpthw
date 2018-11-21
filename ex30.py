people = 30
cars = 40
trunks = 15

if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if trunks > cars:
	print("That's too many trunks.")
elif trunks < cars:
	print("Maybe we could take the trunks.")
else:
	print("We still can't decide.")

if people > trunks:
	print("Alright, let's just take the truncks.")
else:
	print("Fine, let's stay home then.")