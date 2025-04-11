import pyfiglet
from termcolor import colored

sentence = pyfiglet.figlet_format("SUCCESS")
# sentence_color = colored(sentence, "GOOD")
# print(sentence_color)

def message(sentence):
    hello = pyfiglet.figlet_format(sentence)
    say = colored(hello, "red")
    print(say)


message("BEST")
