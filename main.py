import time
import random
from pynput.keyboard import Key, Controller
from os import system

system("title " + "Coffee")
system('mode con: cols=30 lines=10')
keyboard = Controller()

def press_key_with_delay():
    while (True):
        time.sleep(120 + random.uniform(2, 7))
        keyboard.press(Key.f16)
        keyboard.release(Key.f16)
        print("pressed f16")

def main():
    print("Starting main.py...")
    press_key_with_delay();

if __name__ == '__main__':
    main()