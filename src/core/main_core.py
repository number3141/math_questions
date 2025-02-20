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
			return num_1 * num_2
		case '/':
			return round((num_1 / num_2), 2)

def check_user_response(correct_answer, user_input):
	if round(correct_answer, 2) == round(user_input, 2):
		return True
	return False
