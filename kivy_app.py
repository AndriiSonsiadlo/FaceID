# Copyright (C) 2021 Andrii Sonsiadlo

import threading

from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from classes.screen_FaceScanner.facescanner_screen import FaceScanner
from classes.Popup.my_popup_ask import *
from classes.screen_Learning.learningmode_screen import LearningMode
from classes.screen_Learning.editmodel_screen import LearningEdit
from classes.screen_Learning.createmodel_screen import LearningCreate
from classes.screen_AddPerson.addperson_screen import AddPerson
from classes.screen_EditPerson.editperson_screen import EditPerson
from classes.screen_WantedPerson.wantedperson_screen import *
from classes.screen_WantedPerson.selectable_recycleview import *
from classes.screen_Learning.selectable_recycleview_create import *
from classes.drop_button import DropButton
from classes.screen_FaceScanner.kivy_camera import KivyCamera
from classes.screenstack.screen_stack import ScreenStack

# loading ui files
Builder.load_file("Graphics/ui files/widget_styles.kv")
Builder.load_file("Graphics/ui files/app_ui.kv")
Builder.load_file("Graphics/ui files/facescanner_screen.kv")
Builder.load_file("Graphics/ui files/addperson_screen.kv")
Builder.load_file("Graphics/ui files/editperson_screen.kv")
Builder.load_file("Graphics/ui files/wantedperson_screen.kv")
Builder.load_file("Graphics/ui files/learningmode_screen.kv")
Builder.load_file("Graphics/ui files/createmodel_screen.kv")
Builder.load_file("Graphics/ui files/editmodel_screen.kv")
Builder.load_file("Graphics/ui files/my_popup.kv")
Builder.load_file("Graphics/ui files/plot_popup.kv")


# Main Screen with navigation bar on top
class Main(GridLayout, threading.Thread):
	manager = ObjectProperty(None)


# manager for changing screens
class WindowManager(ScreenManager):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.stack = ScreenStack()
		self.stack.add_screen("facescanner")


# main app class
class AIApp(App):  # Automatic Identification App
	icon = 'Graphics/Images/icon_pwr.ico'
	title = 'Automatic Identification'

	Window.size = (800, 600)
	Window.minimum_width, Window.minimum_height = Window.size
	Window.resizable = False

	def build(self):
		# showing main screen
		return Main()


if __name__ == '__main__':
	AIApp().run()
