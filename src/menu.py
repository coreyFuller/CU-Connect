import kivy
from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown

class FillUserInfo(Screen):
    # major = ObjectProperty(None)
    # course = ObjectProperty(None)
    # hobbies = ObjectProperty(None)
    
    # def courseBtn(self):
    #     print("Class Press")
    
    # def hobbiesBtn(self):
    #      print("Hobbies Press")
    print("hey")
    

class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def loginBtn(self):
        print(self.username.text)
        self.reset()
        sm.current="main"

    def reset(self):
        self.username.text = ""
        self.password.text = ""

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        self.reset()
        sm.current = "login"

    def submit(self):
        self.reset()
        sm.current = "userinfo"
        return subbutt()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm:current = "login"

    def on_enter(self, *args):
        self.n.text = "Account Name: Jamie"
        self.email.text = "Email: Ketchup@gmail.com"
        self.created.text = "Created On: Now"

def subbutt():
    pop = Popup(title='SUBMITTED', 
                    content=Label(text="Your thing has been submitted"), size_hint=(None,None), size=(400,300))
    pop.open()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"), FillUserInfo(name="userinfo")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyApp().run()