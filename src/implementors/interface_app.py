import time
import datetime
import shelve
import dearpygui.dearpygui as dpg
from src.implementors.console_app import App
from src.core.main_core import check_user_response, generate_example, calc_example
from src.core.points import Points


class ShelvePoints(Points):
	def save_points(self):
		with shelve.open('points') as database:
			key = str(datetime.datetime.now())
			database[key] = self.get_points()
			print('Файл сохранён!')

		# Проверка
		# with shelve.open('points') as database:
		# 	for key in database:
		# 		print(key)


class TextFilePoints(Points):
	def save_points(self):
		with open('points.txt', 'w', encoding='utf-8') as f:
			x = datetime.datetime.now()
			f.write(f'{x} ----- {self.get_points()}')
			print('Файл сохранён!')


class GraphicApp(App):
	def __init__(self):
		self.points_module = ShelvePoints()
		self.example = generate_example()
		self.paint_main_window()

	def paint_main_window(self):
		dpg.create_context()
		dpg.create_viewport(title='Fast Math', width=332, height=300, resizable=False)

		with dpg.font_registry():
			# if __name__ == '__main__':
			# 	print('Главный')
			# 	path = './LiteralRegular.otf'
			# else:
			# 	path = 'src/LiteralRegular.otf'

			with dpg.font('src/LiteralRegular.otf', 20, tag='main_font'):
				dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

			with dpg.font('src/LiteralRegular.otf', 40, tag='example_font'):
				dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

		with dpg.window(tag='main_board'):
			with dpg.tab_bar():
				with dpg.tab(label='Главная'):
					with dpg.group(width=180):
						dpg.add_text(tag='example', default_value=self.example)
					dpg.add_input_float(tag='answer', width=300, step=0)
					dpg.add_button(label='Проверить', callback=self.paint_answer, width=300, height=40)
					dpg.add_button(
						label='Сохранить', callback=self.points_module.save_points, width=300, height=40)

				with dpg.tab(label='Помощь'):
					with dpg.group(width=180):
						dpg.add_text(default_value='Ответы деления округлять до сотых')

		dpg.bind_font('main_font')
		dpg.bind_item_font(item='example', font='example_font')
		dpg.setup_dearpygui()
		dpg.show_viewport()
		dpg.set_primary_window("main_board", True)
		dpg.start_dearpygui()
		dpg.destroy_context()

	def paint_answer(self):
		user_answer = float(dpg.get_value(item='answer'))
		correct_answer = calc_example(self.example)

		if check_user_response(correct_answer, user_answer):
			dpg.add_text(default_value='Правильно! +1 point!', tag='_', parent='main_board')
			self.points_module.plus_points()
		else:
			dpg.add_text(default_value='Неправильно! -1 point!', tag='_', parent='main_board')
			self.points_module.minus_points()

		time.sleep(2)
		dpg.delete_item(item='_')
		self.update_example()

	def update_example(self):
		self.example = generate_example()
		dpg.set_value(item='example', value=self.example)


if __name__ == '__main__':
	t = GraphicApp()







