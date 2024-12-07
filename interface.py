import time
from main import App
from core import check_user_response, generate_example
from save_file_points import TextFilePoints
import dearpygui.dearpygui as dpg


class GraphicApp(App):
	def __init__(self):
		self.points_module = TextFilePoints()
		self.paint_main_window()

	def paint_main_window(self):
		dpg.create_context()
		dpg.create_viewport(title='Fast Math', width=332, height=300, resizable=False)
		dpg.set_viewport_small_icon('./icon.png')

		with dpg.font_registry():
			with dpg.font('./LiteralRegular.otf', 20, tag='main_font'):
				dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

			with dpg.font('./LiteralRegular.otf', 40, tag='example_font'):
				dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

		with dpg.window(tag='main_board'):
			with dpg.tab_bar():
				with dpg.tab(label='Главная'):
					with dpg.group(width=180):
						dpg.add_text(tag='example', default_value=generate_example())
					dpg.add_input_float(tag='answer', width=300, step=0)
					dpg.add_button(label='Проверить', callback=self.paint_answer, width=300, height=40)
					dpg.add_button(label='Сохранить', callback=self.points_module.save_points, width=300, height=40)

				with dpg.tab(label='Помощь'):
					with dpg.group(width=180):
						dpg.add_text(default_value='Ответы деления округлять до сотых')


		dpg.bind_font('main_font')
		dpg.bind_item_font(item='example', font='example_font')
		dpg.set_viewport_large_icon('./icon.ico')
		dpg.setup_dearpygui()
		dpg.show_viewport()
		dpg.set_primary_window("main_board", True)
		dpg.start_dearpygui()
		dpg.destroy_context()

	def paint_answer(self):
		user_answer = round(float(dpg.get_value(item='answer')), 2)
		if check_user_response(dpg.get_value(item='example'), user_answer):
			dpg.add_text(default_value='Правильно! +1 point!', tag='_', parent='main_board')
			self.points_module.set_points(self.points_module.get_points() + 1)
			time.sleep(2)
			dpg.delete_item(item='_')
		else:
			dpg.add_text(default_value='Неправильно! -1 point!', tag='_', parent='main_board')
			self.points_module.set_points(self.points_module.get_points() - 1)
			time.sleep(2)
			dpg.delete_item(item='_')

		self.update_example()

	def update_example(self):
		dpg.set_value(item='example', value=generate_example())


if __name__ == '__main__':
	t = GraphicApp()










