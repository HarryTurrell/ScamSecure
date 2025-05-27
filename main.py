from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

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
