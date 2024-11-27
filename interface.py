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
		dpg.create_viewport(title='math game', width=200, height=200)

		with dpg.window(tag='main_board'):
			dpg.add_text(tag='example', default_value=generate_example())
			dpg.add_input_float(tag='answer')
			dpg.add_button(label='Check', callback=self.paint_answer)
			dpg.add_button(label='Save', callback=self.points_module.save_points)

		dpg.setup_dearpygui()
		dpg.show_viewport()
		dpg.set_primary_window("main_board", True)
		dpg.start_dearpygui()
		dpg.destroy_context()

	def paint_answer(self):
		user_answer = round(float(dpg.get_value(item='answer')), 2)
		if check_user_response(dpg.get_value(item='example'), user_answer):
			dpg.add_text(default_value='Correct! +1 point!', tag='_', parent='main_board')
			self.points_module.set_points(self.points_module.get_points() + 1)
			time.sleep(2)
			dpg.delete_item(item='_')
		else:
			dpg.add_text(default_value='Bad! -1 point!', tag='_', parent='main_board')
			self.points_module.set_points(self.points_module.get_points() - 1)
			time.sleep(2)
			dpg.delete_item(item='_')

		self.update_example()

	def update_example(self):
		dpg.set_value(item='example', value=generate_example())


if __name__ == '__main__':
	t = GraphicApp()










