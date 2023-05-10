import keyboard
from time import sleep
from random import randint

while True:
    sleep(0.05)
    if keyboard.is_pressed("l") or keyboard.is_pressed("r"):
        keyboard.write("\bw")