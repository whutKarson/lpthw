# output the numbers of cheeses and crackers which set as arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers")
	print("Get a blanket.\n")


print("We can just give the function nunbers directly:")
cheese_and_crackers(20, 30)

print("Or, we can use variable from our script:")
amount_of_cheeses = 20
amount_of_crackers = 10

cheese_and_crackers(amount_of_cheeses, amount_of_crackers)

print("We can even do match inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combile the two, variables and match:")
cheese_and_crackers(amount_of_cheeses + 100, amount_of_crackers + 1000)