from src.core.main_core import generate_example, calc_example, check_user_response


class App:
	def answer(self):
		pass


class ConsoleApp(App):
	def __init__(self):
		self.points = 0

	def answer(self):
		example = generate_example()
		correct_answer = calc_example(example)
		print(f'Вопрос: {example}')
		user_answer = input('Ваш ответ: ')

		if check_user_response(correct_answer, user_answer):
			self.points += 1
			print('Верно! +1 балл')
		else:
			self.points -= 1
			print('Неверно! -1 балл')
			print(f'Правильный ответ: {correct_answer}')
		print(f'Ваши очки: {self.points}')





