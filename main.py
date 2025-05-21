
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="ইমন, তোমার স্মার্ট অ্যাসিস্ট্যান্ট চালু হয়েছে!", font_size='20sp'))

class ImonSmartAssistantApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    ImonSmartAssistantApp().run()
