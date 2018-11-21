# -*- coding: utf-8 -*-


def count(n):
	while n > 0:
		yield n # 生成值： n
		n -= 1
		print("n: %s" %n)

c = count(5)
print(c.next())

print("Again")
print(c.next())