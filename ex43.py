# -*- coding: utf-8 -*-

"""
1.把要解决的问题写下来，或者画出来
2.将第一条中的关键概念提取出来并加以研究
3.创建一个类层次结构和对象图
4.用代码实现各个类，并写一个测试来运行它们
5.重复上述步骤并细化代码
"""

"""
做一个游戏 《来自Percal 25号行星的歌顿人》，这是一款空间冒险游戏。

描述：
外星人入侵了宇宙飞船，我们的英雄需要通过各种房间组成的迷宫， 打败遇到的外星人，这样才能通过救生船回到下面的行星上去。

死亡： 玩家死去的场景，应该比较搞笑
中央走廊： 游戏的起点
激光武器库： 
飞船主控舱：
救生舱：

"""

"""
-Map
-Engine
-Scene
	-Death
	-Central Corridor
	-Laser Weapon Armory
	-The Bridge
	-Escape Pod

*Map
	-next_scene
	-opening_scene
*Engine
	-play
*Scene
	-enter
	*Death
	*Central Corridor
	*Laser Weapon Armory
	*The Bridge
	*Escape Pod
"""

class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		pass

	def play():
		pass

class Death(Scene):

	def enter(self):
		pass

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

a_map = Map('centeral_corridor')
a_game = Engine(a_map)
a_game.play()