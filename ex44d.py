class Parent(object):

	def override(self):
		print("Parent override()")

	def implicit(self):
		print("Parent implicit()")

	def altered(self):
		print("Parent altered()")

class Child(Parent):

	def overrid(self):
		print("Child override()")

	def implicit(self):
		print("Child implicit()")

	def altered(self):
		print("Child, before Parent altered()")
		super(Child, self).altered()
		print("Child, after Parent altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


dad.override()
son.override()

dad.altered()
son.altered()
