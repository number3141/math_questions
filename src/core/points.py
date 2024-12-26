from abc import ABC, abstractmethod


class Points(ABC):
	def __init__(self):
		self._points = 0

	def get_points(self):
		return self._points

	def plus_points(self):
		self._points += 1

	def minus_points(self):
		self._points -= 1

	@abstractmethod
	def save_points(self):
		...