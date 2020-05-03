'''Measures the distance scrolled over the 
screen

'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from math import sqrt
  

class YouScrolled(Widget):
    dx = NumericProperty(0)
    dy = NumericProperty(0)
    distance = NumericProperty(0)
    total_distance = NumericProperty(0)

    def on_touch_move(self, touch):
        self.dx = touch.dx
        self.dy = touch.dy
        self.distance = sqrt(self.dx**2.0 + self.dy**2.0)
        self.total_distance += self.distance

class YouScrolledApp(App):
    def build(self): 
		self.icon = 'icon.jpg'
        return YouScrolled() 

if __name__ == '__main__':
    YouScrolledApp().run()
