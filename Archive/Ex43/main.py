# ex43.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty

class Ex43(BoxLayout):
    my_data = ListProperty([])
    selected_value = StringProperty('Select a button')
    def change(self,change):
        self.selected_value = 'Selected: {}'.format(change.text)

class Ex43App(App):
    def build(self):
        return Ex43()

if __name__ == '__main__':
    Ex43App().run()