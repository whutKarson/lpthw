# -*- coding: utf-8 -*-

"""
该类用来扫描用户输入的词汇，然后动态分析归档输出对应的类型
如动词-走
名词-苹果等
1.先创建一个游戏词汇表。 区分动词， 名词，方向等词汇
2.截断用户的输入
3.分析截断的输入词汇并联系词汇表进行归档，输出不能修改的tuple表
"""

class Lexicon(object):

	# 定义一个方法， 试着去转换str到int，如果成功，返回int类型，如果不成功，返回None
	def conver_number(self, s):
		try:
			return int(s)
		except ValueError:
			return None


	# 定义一个方法，区分每个单词所属的类型
	def judge_type(self, word):
		if self.conver_number(word) != None:
			return ("number", self.conver_number(word))
		else:
			return self.search_in_dictionary(word)

	# 定义一个方法，接受用户的输入并断句，然后依据词汇表归档
	def scan(self, s):

		words = s.split()
		result = []
		for word in words:
			r = self.judge_type(word)
			print(f"r ---> {r}")
			result.append(r)
		return result
	# 定义一个方法，接受一个word，依据词汇表进行查询
	def search_in_dictionary(self, s):
		for key, value in self.dictionary.items():
			if value.count(s) > 0:
				return (key, s)				
		return("error", s)

	# 创建词汇表
	dictionary = {
					"direction": ["north",
									"south",
									'east',
									'west',
									'down',
 									'up',
									'left',
									'right',
									'back'],
									'verb': ['go',
									'stop',
									'kill',
									'eat'],
					'noun': ['door',
							'bear',
							'princess',
							'cabinet'],
					'stop': ['the',
							'in',
							'of',
							'from',
							'at',
							'it']
	}









