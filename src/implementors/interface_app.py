import random
import time
import dearpygui.dearpygui as dpg
from src.core import check_user_response, generate_example, calc_example
from src.implementors.points_options import ShelvePoints, TextFilePoints


class GraphicApp:
	def __init__(self):
		self.points_module = TextFilePoints()
		self.example = generate_example()
		self.player_name = f'player_{random.randint(1, 100)}'

	def start(self):
		dpg.create_context()
		dpg.create_viewport(title='Fast Math', width=332, height=370, resizable=False)

		with dpg.font_registry():
			with dpg.font('LiteralRegular.otf', 20, tag='main_font'):
				dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

			with dpg.font('LiteralRegular.otf', 40, tag='example_font'):
				dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

		with dpg.window(tag='main_board'):
			with dpg.tab_bar():
				with dpg.tab(label='Главная', tag='main_tab'):
					with dpg.group(tag='name_group'):
						dpg.add_text('Ваше имя: ')
						dpg.add_input_text(tag='name_player', default_value=self.player_name)
						dpg.add_button(label='Начать', callback=self.login)

					with dpg.group(width=180, tag='app_group'):
						dpg.add_text(tag='name_player_text', default_value=self.player_name)
						dpg.add_text(tag='points_area', default_value=f'Очков: 0')
						dpg.add_text(tag='example', default_value=self.example)
						dpg.add_input_float(tag='answer', width=300, step=0)
						dpg.add_button(label='Проверить', callback=self.paint_answer, width=300, height=40)
						dpg.add_button(
							label='Сохранить',
							callback=self.points_module.save_points,
							width=300, height=40
						)

					dpg.hide_item('app_group')

				with dpg.tab(label='Лидеры'):
					with dpg.group():
						dpg.add_text('Список рекордов: ')

						self.points_module.load_points()
						for name, points in self.points_module.get_players().items():
							dpg.add_text(f'{name} --- {points}')

				with dpg.tab(label='Помощь'):
					with dpg.group():
						dpg.add_text('Ответы деления округлять до сотых')

		with dpg.theme() as global_theme:
			with dpg.theme_component():
				dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (205, 241, 240))
				dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))
				dpg.add_theme_color(dpg.mvThemeCol_Tab, (75, 212, 208))
				dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (42, 155, 152))
				dpg.add_theme_color(dpg.mvThemeCol_TabActive, (30, 118, 116))
				dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (215, 254, 253))
				dpg.add_theme_color(dpg.mvThemeCol_Button, (30, 118, 116))

				dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 4)
				# dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1)
				dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

		dpg.bind_font('main_font')
		dpg.bind_theme(global_theme)
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
			self.points_module.plus_points(self.player_name)
		else:
			dpg.add_text(default_value='Неправильно! -1 point!', tag='_', parent='main_board')
			self.points_module.minus_points(self.player_name)

		dpg.set_value(item='points_area', value=f'Очков: {self.points_module.get_points(self.player_name)}')
		time.sleep(1)
		dpg.delete_item(item='_')
		self.update_example()

	def update_example(self):
		self.example = generate_example()
		dpg.set_value(item='example', value=self.example)

	def login(self):
		self.player_name = dpg.get_value(item='name_player')
		self.points_module.add_player(self.player_name)

		dpg.set_value(item='name_player_text', value=self.player_name)
		dpg.delete_item('name_group')
		dpg.show_item('app_group')


def graphic_start():
	t = GraphicApp()
	t.start()