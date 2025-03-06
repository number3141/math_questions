from abc import ABC, abstractmethod

class Points(ABC):
	def __init__(self):
		self.points_board = {
			# alex: 21,
			# bob: 15,
		}

	def get_players(self):
		return self.points_board

	def add_player(self, name):
		self.points_board[name] = 0

	def get_points(self, name):
		return self.points_board.get(name, self.points_board)

	def plus_points(self, name):
		self.points_board[name] += 1

	def minus_points(self, name):
		self.points_board[name] -= 1

	@abstractmethod
	def save_points(self):
		...

	@abstractmethod
	def load_points(self):
		...
