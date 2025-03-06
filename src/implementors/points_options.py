import shelve
from src.core import Points

class ShelvePoints(Points):
	def save_points(self):
		with shelve.open('points') as database:
			self.points_board = dict(sorted(self.points_board.items(), key=lambda item: item[1], reverse=True)[:3])
			for name in self.points_board:
				database[name] = self.get_points(name)
			print('Файл сохранён!')

	def load_points(self):
		with shelve.open('points') as database:
			for name in database:
				self.points_board[name] = database.get(name)
			print('База лидеров загружена!')


class TextFilePoints(Points):
	def save_points(self):
		with open('points.txt', 'w', encoding='utf-8') as f:
			self.points_board = dict(sorted(self.points_board.items(), key=lambda item: item[1], reverse=True)[:3])
			for name in self.points_board:
				f.write(f'{name} ----- {self.get_points(name)}\n')

	def load_points(self):
		with open('points.txt', 'r+', encoding='utf-8') as database:
			text = database.read().split('\n')
			text.remove('')
			for player_str in text:
				name, points = player_str.split('-----')
				self.points_board[name] = int(points)

if __name__ == '__main__':
	t = ShelvePoints()
	t.add_player('andrey')
	t.plus_points('andrey')
	t.plus_points('andrey')
	t.save_points()
	t.load_points()