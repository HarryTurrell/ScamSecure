import Screen.Config as config

config.apply_window_size()
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from Screen.Home import HomePage

class QuizScreen(Screen):
    pass

class HackaburryApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomePage(name="home"))
        sm.add_widget(QuizScreen(name="quiz"))
        # Add other screens
        return sm


if __name__ == "__main__":
    HackaburryApp().run()
