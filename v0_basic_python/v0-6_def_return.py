# from pyfiglet import Figlet

# f = Figlet(font="slant")
# print(f.renderText("TEST"))

import pyfiglet
from termcolor import colored

def call(sentence, color):
     a = pyfiglet.figlet_format(sentence)
     b = colored(a, color)
     # return b
     print(b)

# call("HELLO", "blue")

# return으로 값을 받으시오.
def call2(sentence, color):
    a = pyfiglet.figlet_format(sentence)
    b = colored(a, color)
    return b

print(call2("Hello", "blue"))

tmp = call2("Hello", "blue")
print(tmp)

