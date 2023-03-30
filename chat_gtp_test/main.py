from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
import datetime
from kivy.clock import Clock
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder


class ColiCounter(BoxLayout):
    total_coli = NumericProperty(0)
    current_time = StringProperty()
    elapsed_time = NumericProperty(0.0)  # change elapsed_time to float
    paused_time = 0.0
    coli_per_hour = NumericProperty(0)
    stopwatch_running = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_paused = None
        self.update_current_time()
        self.current_time_event = Clock.schedule_interval(self.update_current_time, .1)
        self.stopwatch_event = None  # initialize stopwatch_event here
        self.stopwatch_running = False

    def update_current_time(self, *args):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.current_time = formatted_time

    def toggle_stopwatch(self):
        if not self.stopwatch_running:
            self.start_stopwatch()
        elif self.is_paused:
            self.resume_stopwatch()
        else:
            self.pause_stopwatch()

    def start_stopwatch(self):
        self.elapsed_time = 0.0
        self.stopwatch_event = Clock.schedule_interval(self.update_stopwatch, 1)
        self.stopwatch_running = True
        self.ids.stopwatch_button.text = 'Pause'

    def update_stopwatch(self, dt):
        self.elapsed_time += dt
        self.coli_per_hour = (self.total_coli / self.elapsed_time) * 3600
        coliperhour = int(self.coli_per_hour)
        total_seconds = int(self.elapsed_time)
        hours = total_seconds // 3600
        minutes = (total_seconds // 60) % 60
        seconds = total_seconds % 60
        self.ids.elapsed_time_label.text = f"Elapsed time: {hours:02d}:{minutes:02d}:{seconds:02d}"
        self.ids.coli_per_hour.text = f"Coli per hour: {coliperhour:}"

    def pause_stopwatch(self):
        if self.stopwatch_event:
            self.stopwatch_event.cancel()
            self.stopwatch_event = None
            self.is_paused = True
            self.ids.stopwatch_button.text = 'Resume'

    def resume_stopwatch(self):
        self.stopwatch_event = Clock.schedule_interval(self.update_stopwatch, 1)
        self.is_paused = False
        self.ids.stopwatch_button.text = 'Pause'

    def stop_stopwatch(self):
        if self.stopwatch_event:
            self.stopwatch_event.cancel()
            self.stopwatch_event = None
            self.elapsed_time = 0.0
            self.stopwatch_running = False
            self.is_paused = False
            self.ids.stopwatch_button.text = 'Start'

    def add_coli(self, coli_count):
        self.total_coli += coli_count
        self.ids.coli_input.text = ''

    def get_coli_per_hour(self):
        if self.elapsed_time > 0:
            coli_per_hour = self.total_coli / (self.elapsed_time / 3600)
            return "{:.2f} coli/hour".format(coli_per_hour)
        else:
            return


class Menu(BoxLayout):
    pass


kv = Builder.load_file("ColiCounter.kv")


class ColiCounterApp(App):
    def build(self):
        Window.size = (1080, 2340)
        return kv


ColiCounterApp().run()
