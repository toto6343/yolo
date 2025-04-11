import pyfiglet

sentence = pyfiglet.figlet_format("GOOD")
print(sentence)

# 함수화
def call_message(sentence):
    say = pyfiglet.figlet_format(sentence)
    print(say)
    
call_message("FREE")