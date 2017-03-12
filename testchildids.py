from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from random import choice

Builder.load_string('''


<MyCustomLayout1>:
    Button:
        id: mybutton
        text: "Goto 2"
        on_release: app.sm.current = "screen2"


<MyCustomLayout2>:
    Button:
        id: mybutton
        text: "Goto 1"
        on_release: app.sm.current = "screen1"
    Button:
        id: mybutton2
        text: 'GotoNone'


<Screen1>:
    MyCustomLayout1:
        id: mylayout

<Screen2>:
    MyCustomLayout2:
        id: mylayout

''')


class Screen1(Screen):

    def on_enter(self,*args):
        self.ids.mylayout.ids.mybutton.text = str(choice(range(100)))


class Screen2(Screen):

    def on_enter(self,*args):
        print(self.ids)
        print(self.ids.mylayout.ids)


class MyCustomLayout1(BoxLayout):
    pass

class MyCustomLayout2(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Screen1(name='screen1'))
        self.sm.add_widget(Screen2(name='screen2'))
        return self.sm


MyApp().run()
