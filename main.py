from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Root(App):
    def build(self):
        bl = BoxLayout()
        but1 = Button(text = 'b1')
        but2 = Button(text = 'b2')
        bl.add_widget(but1)
        bl.add_widget(but2)
        return bl

if __name__ == '__main__':
    Root().run()
