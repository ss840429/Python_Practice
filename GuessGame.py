import random
from abc import ABCMeta, abstractmethod

class GuessGame(metaclass=ABCMeta):

	@abstractmethod
	def message(self, msg):
		pass

	@abstractmethod
	def guess(self):
		pass

	def start(self):
		quiz = int(random.random()*100)
		self.message(self.welcome)

		while True :
			num = self.guess()
			if num > quiz:
				self.message( self.smaller )
			elif num < quiz:
				self.message( self.bigger )
			else:
				self.message( self.correct )
				break				

class ConsoleGame(GuessGame):

	def __init__(self):
		self.welcome = 'ゲースゲームへようこそ、当たりまで遊んで続け。'
		self.bigger  = '大きくになって。'
		self.smaller = '小きくになって。'
		self.correct = '当たり!!! おめでとうございます。'
		self.inmsg   = '数字を書き込む...> '

	def message(self, msg):
		print(msg)

	def guess(self):
		guessing = int(input(self.inmsg))
		return guessing


Game = ConsoleGame()
print( Game.__dict__)
Game.start()


