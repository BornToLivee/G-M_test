import time
import random

def slow_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))
