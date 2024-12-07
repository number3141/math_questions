import random


def generate_example():
	num_1 = random.randint(-100, 100)
	num_2 = random.randint(-100, 100)
	znak = random.choice(('+', '-', '*', '/'))

	return f'{num_1} {znak} {num_2}'


def calc_example(example):
	num_1, znak, num_2 = example.split(' ')
	num_1, num_2 = int(num_1), int(num_2)

	match znak:
		case '+':
			return num_1 + num_2
		case '-':
			return num_1 - num_2
		case '*':
			return round((num_1 * num_2), 2)
		case '/':
			return round((num_1 / num_2), 2)


def check_user_response(example, user_input):
	if round(calc_example(example), 2) == round(user_input, 2):
		return True
	print(f'Сравнил {round(calc_example(example), 2)} and {round(user_input, 2)}')
	return False


class Points:
	def __init__(self):
		self._points = 0

	def save_points(self):
		...

	def get_points(self):
		return self._points

	def set_points(self, value):
		self._points = value
