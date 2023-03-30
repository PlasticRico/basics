import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.core.text
import webbrowser
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class StartScreen(Screen):
    pass


class SearchLocation(Screen):
    pass


class ERNearMe(Screen):
    pass


class PoliceNearMe(Screen):
    def button_on(self, **kwargs):
        self.ids.MapButton.source = 'MapMarker Button down.png'

    def button_off(self, **kwargs):
        self.ids.MapButton.source = 'MapMarker Button up.png'


class EmergencyNumbers(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("crimewhereza.kv")


class CrimeWhereZA(App):
    def build(self):
        return kv


if __name__ == '__main__':
    CrimeWhereZA().run()
