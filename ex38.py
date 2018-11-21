# -*- coding: utf-8 -*-


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', ' Boy']

while len(stuff) != 10:
	next_one = more_stuff.pop()

	print("Adding: ", next_one)

	stuff.append(next_one)
	print("There are %s items now" % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])   # Whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # What? cool!
print("#".join(stuff[3:5])) # super stellar!

"""
排队的买单人， 书表，字母表， 区号，百家姓， 车库位置， 高铁位置表，飞机位置表，一堆扑克牌，一副麻将牌

"""