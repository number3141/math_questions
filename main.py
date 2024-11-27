from core import generate_example, calc_example, check_user_response


class App:
	def answer(self):
		pass


class ConsoleApp(App):
	def __init__(self):
		self.points = 0

	def answer(self):
		example = generate_example()
		answer = calc_example(example)
		print(f'Вопрос: {example}')
		user_answer = input('Ваш ответ: ')

		if check_user_response(answer, user_answer):
			self.points += 1
			print('Верно! +1 балл')
		else:
			self.points -= 1
			print('Неверно! -1 балл')
			print(f'Правильный ответ: {answer}')
		print(f'Ваши очки: {self.points}')



if __name__ == '__main__':
	app = ConsoleApp()
	while True:
		app.answer()

