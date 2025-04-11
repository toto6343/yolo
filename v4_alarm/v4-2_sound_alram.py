import pygame

pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Administrator\Desktop/AI/WTDC/v4_alarm/mp3/correct_answer3.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

print("SUCCESS")