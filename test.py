from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

 #Window.clearcolor = (1, 1, 1, 1)

class ContainerLayout(BoxLayout):
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

class LayoutLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(LayoutLayout, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 1)  # set the colour to red
            self.rect = Rectangle(pos=self.center,
                                  size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

    iteration = 1

    def do_layout(self, *largs):
        # optimize layout by preventing looking at the same attribute in a loop
        self.iteration += 1
        print('self.iteration:', self.iteration)

        len_children = len(self.children)
        if len_children == 0:
            return
        self.height = len_children * 50 + 100

        selfx = self.x
        selfy = self.y
        selfw = self.width
        selfh = self.height
        padding_left = self.padding[0]
        padding_top = self.padding[1]
        padding_right = self.padding[2]
        padding_bottom = self.padding[3]
        spacing = self.spacing
        orientation = self.orientation
        padding_x = padding_left + padding_right
        padding_y = padding_top + padding_bottom

        # calculate maximum space used by size_hint
        stretch_weight_x = 0.
        stretch_weight_y = 0.
        minimum_size_x = padding_x + spacing * (len_children - 1)
        minimum_size_y = padding_y + spacing * (len_children - 1)
        for w in self.children:
            shw = w.size_hint_x
            shh = w.size_hint_y
            if shw is None:
                minimum_size_x += w.width
            else:
                stretch_weight_x += shw
            if shh is None:
                minimum_size_y += w.height
            else:
                stretch_weight_y += shh

        if orientation == 'horizontal':
            x = padding_left
            stretch_space = max(0.0, selfw - minimum_size_x)
            for c in reversed(self.children):
                shw = c.size_hint_x
                shh = c.size_hint_y
                w = c.width
                h = c.height
                cx = selfx + x
                cy = selfy + padding_bottom

                if shw:
                    w = stretch_space * shw / stretch_weight_x
                if shh:
                    h = max(0, shh * (selfh - padding_y))

                for key, value in c.pos_hint.items():
                    posy = value * (selfh - padding_y)
                    if key == 'y':
                        cy += posy
                    elif key == 'top':
                        cy += posy - h
                    elif key == 'center_y':
                        cy += posy - (h / 2.)

                c.x = cx
                c.y = cy
                c.width = w
                c.height = h
                x += w + spacing

        if orientation == 'vertical':
            y = padding_bottom
            stretch_space = max(0.0, selfh - minimum_size_y)
            for c in self.children:
                shw = c.size_hint_x
                shh = c.size_hint_y
                w = c.width
                h = c.height
                cx = selfx + padding_left
                cy = selfy + y

                if shh:
                    h = stretch_space * shh / stretch_weight_y
                if shw:
                    w = max(0, shw * (selfw - padding_x))

                for key, value in c.pos_hint.items():
                    posx = value * (selfw - padding_x)
                    if key == 'x':
                        cx += posx
                    elif key == 'right':
                        cx += posx - w
                    elif key == 'center_x':
                        cx += posx - (w / 2.)

                c.x = cx
                c.y = cy
                c.width = w
                c.height = h
                y += h + spacing


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

container_layout = ContainerLayout(id='out_SV', size=(Window.width, 800),\
                    height=800)
with container_layout.canvas:
    Color(1, 0, 0, 1)  # set the colour to red
    container_layout.rect = Rectangle(pos=container_layout.center,
                                  size=(container_layout.width/2.,
                                        container_layout.height/2.))

#container_layout.bind(minimum_size_y=container_layout.setter('height'))
layout = LayoutLayout(spacing=10, size_hint_y=None, id='in_SV', orientation='vertical')
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
TestClass()

'''
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.label import Label

layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
layout2 = GridLayout(cols=1, spacing=10 )
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))
for i in range(100):
    btn = Button(text=str(i), size_hint_y=None, height=40)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)
layout2.add_widget(Label(text='Hello', size_hint_y=None, height='20dp'))
layout2.add_widget(root)

runTouchApp(root)
'''
