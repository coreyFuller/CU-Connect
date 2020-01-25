from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#from kivy.config import config


class Screen2(GridLayout):

    def pressed(self, instance):
        # Get the value of all of the tex inputs
        username = self.username.text
        password = self.password.text

        # print the values to the screen
        print("Name:", username, "Last Name:", password)

        # Reset text to blank in each text input
        self.username.text = ""
        self.password.text = ""

    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.cols = 1

        self.title=(Label(text='[font=Helvetica]'+'Screen 2'+'[/font]', markup = True, font_size = 50))
        self.add_widget(self.title)



class LoginScreen(GridLayout):

    def pressed(self, instance):
        # Get the value of all of the tex inputs
        username = self.username.text
        password = self.password.text

        # print the values to the screen
        print("Name:", username, "Last Name:", password)

        # Reset text to blank in each text input
        self.username.text = ""
        self.password.text = ""
        return Screen2()

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1

        self.title=(Label(text='[font=Helvetica]'+'CU CONNECT'+'[/font]', markup = True, font_size = 50))
        self.add_widget(self.title)

        self.add_widget(Label(text='[font=Helvetica]'+'Username'+'[/font]', markup = True))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='[font=Helvetica]'+"Password"+ '[/font]', markup = True))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login = Button(text = '[font=Helvetica]' + "Log in" + '[/font]', font_size = 20, markup = True)
        self.add_widget(self.login)
        self.login.bind(on_press=self.pressed)

        self.createAcc = Button(text = '[font=Helvetica]' + "Create Account" + '[/font]', font_size = 20, markup = True)
        self.add_widget(self.createAcc)
    

class MyApp(App):

    def build(self):
        Window.size = (500,600)
        return LoginScreen()
        return Screen2()


if __name__ == '__main__':
    MyApp().run()