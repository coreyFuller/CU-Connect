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
from kivy.uix.checkbox import CheckBox 
from kivy.uix.scrollview import ScrollView
import subprocess



class HobbyChooser(Screen):
    hobbies = ObjectProperty(None)

    hobbylist = []

    def on_checkbox_active(self, checkboxInstance, isActive): 
        if isActive: 
            self.hobbylist.append(checkboxInstance) 
        else: 
            self.hobbylist.remove(checkboxInstance)

    def profile(self):
        if len(self.hobbylist) > 5 or len(self.hobbylist) < 1:
            return subbutt()
        else:
            # self.reset()
            input.append(self.hobbylist)
            sm.current = "main"
            


    def reset(self):
        self.major.text = ""

class FillUserInfo(Screen):
    major = ObjectProperty(None)
    course = ObjectProperty(None)

    courselist = []
    
    def on_checkbox_active(self, checkboxInstance, isActive): 
        if isActive: 
            #self.lbl_active.text ="Checkbox is ON"
            #print("Checkbox Checked" + checkboxInstance)
            self.courselist.append(checkboxInstance) 
        else: 
           # self.lbl_active.text ="Checkbox is OFF"
            #print("Checkbox unchecked "+ checkboxInstance)
            self.courselist.remove(checkboxInstance)
        print(self.courselist)
        

    def hobbies(self):
        if len(self.courselist) > 5 or len(self.courselist) < 1:
            return subbutt()
        else:
            # self.reset()
            input.append(self.courselist)
            sm.current = "hobbies"

    def reset(self):
        self.major.text = ""

class ConnectScreen(Screen):
    print("Hey")

class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def loginBtn(self):
        if self.useraccept() is True:
            self.reset()
            sm.current="main"
        else: 
            pop = Popup(title='NO ACCESS', 
                    content=Label(text="Incorrect Username/Password"), 
                    size_hint=(None,None), size=(400,300))
            return pop.open()

    def useraccept(self):
        return True

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
        if self.namee.text is "" or self.email.text is "" or self.password.text is "":
            pop = Popup(title='Blank Slots', 
                    content=Label(text="You have left spaces blank"), 
                    size_hint=(None,None), size=(400,300))
            return pop.open()
        input.append(self.namee.text)
        input.append(self.email.text)
        input.append(self.password)
        self.reset()
        sm.current = "userinfo"

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
        print(input)
        subprocess.call(['python', 'cucodb.py', '--user', input[0], '--pw', 'hello', '--name', input[1], 
                '--email',input[1],
                '--classes', input[3], 
                '--hobbies', input[4]
                ])
        self.n.text = "Account Name: " + input[0]
        self.email.text = "Email: " + input[1]


def subbutt():
    pop = Popup(title='Too many chosen', 
                    content=Label(text="Pick between one and\n five options, please"), size_hint=(None,None), size=(400,300))
    pop.open()

class WindowManager(ScreenManager):
    pass

input = []

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [LoginWindow(name="login"), 
            CreateAccountWindow(name="create"), 
            MainWindow(name="main"), 
            FillUserInfo(name="userinfo"),
            HobbyChooser(name="hobbies"),
            ConnectScreen(name="connect")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyApp().run()