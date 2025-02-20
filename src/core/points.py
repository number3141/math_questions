from abc import ABC, abstractmethod

class PointsBoard(ABC):
	def __init__(self):
		self._pointsboard = {
			# name: 0
		}

	def add_player(self, player_name, points=0):
		self._pointsboard[player_name] = points

	def get_points(self, name=None):
		if not name:
			return self._pointsboard
		else:
			return self._pointsboard.get(name)

	def plus_points(self, name):
		self._pointsboard[name] += 1

	def minus_points(self, name):
		self._pointsboard[name] -= 1

	@abstractmethod
	def save_points(self):
		...

	@abstractmethod
	def load_points(self):
		...
