import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        #Window.clearcolor = (0.9, 0.9, 0.9, 1)
        self.cols = 2
        self.add_widget(Label(text='Student Name'))
        self.s_name = TextInput( hint_text='Enter student name')
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student Marks'))
        self.s_marks = TextInput( )
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student Gender'))
        self.s_gender = TextInput( )
        self.add_widget(self.s_gender)


        self.press = Button(text = 'click me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        try:
            marks = float(self.s_marks.text)
            print("Name of student is " + self.s_name.text)
            print("Marks of student is " + str(marks))
            print("Gender of student is " + self.s_gender.text)
            print("")
            # Clear input fields after displaying information
            self.s_name.text = ''
            self.s_marks.text = ''
            self.s_gender.text = ''
        except ValueError:
            print("Please enter valid marks.")


class parentApp(App):
    def build(self):
        return childApp()

if __name__== "__main__":
    parentApp().run()