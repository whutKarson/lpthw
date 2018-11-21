
# -*- coding: utf-8 -*-



def A():
	"""
	跟踪调试yield语句执行流程
	设定两个方法，方法A里头用yield call 方法B
	"""
	print("Starting Function A...")
	n = 0	
	print("Function A,n: %s " % n)
	n = yield B()
	print("Function A,n again: %s" % n)

def B():
	i = 11
	print("Starting Function B...")

	print("Function B, i: %s" % i)
	return i


c = A()
d = c.next()
print("d: %s" %d)
print("I am test line.")





