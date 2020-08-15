from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from formulas import *
from converter import UnitConversion


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    """Energy Expenditure"""

    def summary(self):
        text = ('Use the TDEE calculator to learn your Total Daily Energy Expenditure,'
                '\n a measure of how many calories you burn per day.')
        return text


class ThirdWindow(Screen):
    """Bodyfat Percentage"""
    pass


class FourthWindow(Screen):
    """Muscular Potential"""
    pass


class FifthWindow(Screen):
    """More"""

    def gen(self):
        return 'HELLO'


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')


class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()
