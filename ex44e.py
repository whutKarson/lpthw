class Other(object):

	def override(self):
		print("Other override()")

	def implicit(self):
		print("Other implicit()")

	def altered(self):
		print("Other altered()")


class Child(object):

	def __init__(self):
		self.other = Other()

	def implict(self):
		self.other.implicit()

	def override():
		print("Child override()")

	def altered(self):
		print("Child, before Other altered()")
		self.other.altered()
		print("Child, after Other altered()")

son = Child()

son.implict()
son.override()
son.altered()

# code standard: https://www.python.org/dev/peps/pep-0008/