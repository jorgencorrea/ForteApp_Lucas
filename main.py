from kivy.core.window import Window
Window.size = (400, 680)
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRaisedButton

class MDRaisedButton(MDRaisedButton):
    pass

class Raiz(ScreenManager):
    pass

class StartScreen(MDScreen):
    pass

class StartInfo(MDScreen):
    pass

class ForteApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Raiz()

    def dots(self,*args):
        print('dots-vertical pressed')
    
    def back(self,*args):
        self.root.current = 'start'

    def change_screen(self,screen_name,*args):
        self.root.current = screen_name

if __name__ == '__main__':
    ForteApp().run()