# -*- coding: utf-8 -*-

"""
class:
object:
instance:
def:
self:
inheritance:
composition:
attribute:
is-a:
has-a:
"""

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	  "Make a class nameed %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
	  "class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	  "class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
	  "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	  "From *** get the *** function, call it with params self, @@@",
	"***.*** = '***'":
	  "From ** get the *** attribute and set it to '***'"
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True
else:
	PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(), encoding='utf-8'))

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in 
				   random.sample(WORDS, snippet.count("%%%"))] # 依据PHRASE里每个key的 %%% 参数个数随机从WORDS list里抓取item 并赋予给class_names
	#print(f"random.sample(WORDS, snippet.count('%%%'): {random.sample(WORDS, snippet.count('%%%'))}")
	#print(f"class_names: {class_names}")

	other_names = random.sample(WORDS, snippet.count("***"))  # 依据PHRASE里每个key的 *** 参数个数随机从WORDS list里抓取item 并赋予给other_names
	#print(f"other_names: {other_names}")

	results = []  # 存储转换后的key和value tuple list
	param_names = [] # 存储参数名 list

	for i in range(0, snippet.count("@@@")):  # 判断参数 指示量数 @@@ 如果等于0，跳过，如果>=1， 每次从word列表里随机挑选添加一到三个参数
		param_count = random.randint(1, 3)
		param_names.append(','.join(random.sample(WORDS, param_count)))
		#print(f"param_names {param_names}")



	for sentence in snippet, phrase:    # 开始替代 @@@ *** %%%， 这里其实是双循环合并，python的一大简洁方法之一, 可以认为是for x in snippet and for y in phrase.
		result = sentence[:] 
		#print("Result: %s" % sentence)

		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results


# keep going untill they hit CTRL-D
try:
	while True:
		# get keys of PHRASES and assign to a list
		snippets = list(PHRASES.keys())
		#print(f"snippets: {snippets}")
		# random the order of the list
		random.shuffle(snippets)
		#print(f"snippets after shuffle: {snippets}")


		for snippet in snippets:
			print(f"snippet in snippets {snippet}")
			# get the value of dict PHRASES 
			phrase = PHRASES[snippet]
			print(f"phrase is {phrase} in {snippet}")
			# conver the WORDS get 
			question, answer = convert(snippet, phrase)
			# print out the question 
			print("question is: %s" % question)
			# remind the user to confirm the answer print out
			input("> ")
			# print out the answer
			print(f"ANSWER:  {answer}\n\n")
		print("One round is completed!!!")
except EOFError:
	print("\Bye")



