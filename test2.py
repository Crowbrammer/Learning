from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

class ContainerLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ContainerLayout, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 0, 0, 1)  # set the colour to red
            self.rect = Rectangle(pos=self.center,
                                  size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class LayoutLayout(GridLayout):
    def __init__(self, **kwargs):
        super(LayoutLayout, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 1)  # set the colour to red
            self.rect = Rectangle(pos=self.center,
                                  size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class SuperScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(SuperScrollView, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 0.5)  # set the colour to red
            self.rect = Rectangle(pos=self.center,
                                  size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

container_layout = ContainerLayout(cols=1, id='out_SV', size=(Window.width, 800),\
                    height=800)
with container_layout.canvas:
    Color(1, 0, 0, 1)  # set the colour to red
    container_layout.rect = Rectangle(pos=container_layout.center,
                                  size=(container_layout.width/2.,
                                        container_layout.height/2.))

#container_layout.bind(minimum_size_y=container_layout.setter('height'))
layout = LayoutLayout(cols=1, spacing=10, size_hint_y=None, id='in_SV')
# Make sure the height is such that there is something to scroll.
#layout.bind(minimum_size_y=layout.setter('height'))
layout.add_widget(Label(text='Hello'))
for i in range(100):
    btn = Button(text=str(i), size_hint_y=None, height=40)
    layout.add_widget(btn)
root = SuperScrollView(size_hint=(None, None), id='SV', size=((Window.width - 100), 600))
root.add_widget(layout)
container_layout.add_widget(root)
#root.size = container_layout.size

runTouchApp(container_layout)
