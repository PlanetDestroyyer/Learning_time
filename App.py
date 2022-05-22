
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class Game_width(GridLayout):
	def __init__(self,**kwargs):
		super(Game_width,self).__init__()
		self.cols = 2
		self.add_widget(Label(text="Name of tge student : "))
		self.s_name = TextInput(multiline= False)
		self.add_widget(self.s_name)
		
		self.add_widget(Label("Enter ur age : "))
		self.s_age = TextInput()
		self.add_widget(self.s_age)
		
		self.add_widget(Label("Enter ur marsk : "))
		self.s_marks=TextInput()
		self.add_widget(self.s_marks)
		
		self.press= Button(text= "Clich here to continue")
		self.press.bind(on_press = self.button)
		self.add_widget(self.press)
		
	def button(self,instance):
    print(f" Name of the Student is {self.s_name}") 
		print(f"Age of the student is {self.s_age}")
    print(f"This student has scored {self.s_marks}")
    print("Thanks for using our service ") 
		
class Main_app(App):
		def main(self):
			return Game_width()

		
if __name__=="__main__":

		Main_app().run()
		
		
