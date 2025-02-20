from src.core import generate_example, calc_example, check_user_response


class ConsoleApp:
	def __init__(self):
		self.points = 0

	def start(self):
		while True:
			example = generate_example()
			correct_answer = calc_example(example)
			print(f'Вопрос: {example}')
			try:
				user_answer = input('Ваш ответ: ')
			except TypeError:
				print('Вы ввели не число!')
			else:
				if check_user_response(correct_answer, user_answer):
					self.points += 1
					print('Верно! +1 балл')
				else:
					self.points -= 1
					print('Неверно! -1 балл')
					print(f'Правильный ответ: {correct_answer}')
				print(f'Ваши очки: {self.points}')


def console_start():
	t = ConsoleApp()
	t.start()
