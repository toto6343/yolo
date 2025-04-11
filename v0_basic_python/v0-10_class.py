import pyfiglet
from termcolor import colored

class NiceMessage:
    def __init__(self, message):
        self.message = message
        
    def nice_message(self):
        say = pyfiglet.figlet_format(self.message)
        print(say)
        
    def color_nice_message(self, color):
        say_bye = pyfiglet.figlet_format(self.message)
        color_say_bye = colored(say_bye, color)
        print(color_say_bye)
        
message = NiceMessage("HELLO")
# message.nice_message()
message.color_nice_message("green")
message.color_nice_message("yellow")
message.color_nice_message("red")