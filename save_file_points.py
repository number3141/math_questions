import datetime

from core import Points


class TextFilePoints(Points):
	def save_points(self):
		with open('points.txt', 'w', encoding='utf-8') as f:
			x = datetime.datetime.now()
			f.write(f'{x} ----- {self.get_points()}')
			print('Файл сохранён!')


