from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class RepairApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='ระบบแจ้งซ่อมอุปกรณ์'))
        layout.add_widget(Button(text='ส่งรายการแจ้งซ่อม'))
        return layout

if __name__ == '__main__':
    RepairApp().run()