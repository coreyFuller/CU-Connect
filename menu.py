from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#from kivy.config import config


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1

        self.title=(Label(text='[font=Helvetica]'+'CU CONNECT'+'[/font]', markup = True, font_size = 50))
        self.add_widget(self.title)

        self.add_widget(Label(text='[font=Helvetica]'+'Username'+'[/font]', markup = True))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # self.add_widget(Label(text='[font=Helvetica]'+'Email'+'[/font]', markup = True))
        # self.email = TextInput(multiline=False)
        # self.add_widget(self.email)

        self.add_widget(Label(text='[font=Helvetica]'+"Password"+ '[/font]', markup = True))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login = Button(text = '[font=Helvetica]' + "Log in" + '[/font]', font_size = 20, markup = True)
        self.add_widget(self.login)

        self.createAcc = Button(text = '[font=Helvetica]' + "Create Account" + '[/font]', font_size = 20, markup = True)
        self.add_widget(self.createAcc)
    

class MyApp(App):

    def build(self):
        Window.size = (500,600)
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()