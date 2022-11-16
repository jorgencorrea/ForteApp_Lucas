from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton

class MDRaisedButton(MDRaisedButton):
    pass

class Raiz(MDScreen):
    pass

class ForteApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Raiz()

if __name__ == '__main__':
    ForteApp().run()