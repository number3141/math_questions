import shelve
from src.core import PointsBoard

class ShelvePoints(PointsBoard):
	def save_points(self):
		with shelve.open('points') as database:
			for name in self._pointsboard:
				database[name] = self.get_points(name)
			print('Файл сохранён!')

	def load_points(self):
		with shelve.open('points') as database:
			result_database = {}
			for name in database:
				result_database[name] = database.get(name)

			sorted_result = dict(sorted(result_database.items(), key=lambda item: item[1], reverse=True)[:10])
			print('База лидеров загружена!')
			return sorted_result



class TextFilePoints(PointsBoard):
	def save_points(self):
		with open('points.txt', 'a', encoding='utf-8') as f:
			for name in self._pointsboard:
				f.write(f'{name} ----- {self.get_points(name)}\n')
			print('Файл сохранён!')

	def load_points(self):
		with open('points.txt', 'r+', encoding='utf-8') as database:
			text = database.read().split('\n')
			text.remove('')
			result_database = {}
			for player_str in text:
				name, points = player_str.split('-----')
				result_database[name] = points

			sorted_result = dict(sorted(result_database.items(), key=lambda item: item[1], reverse=True)[:10])
			print('База лидеров загружена!')
			return sorted_result


if __name__ == '__main__':
	t = ShelvePoints()
	t.add_player('andrey')
	t.plus_points('andrey')
	t.plus_points('andrey')
	t.save_points()
	t.load_points()