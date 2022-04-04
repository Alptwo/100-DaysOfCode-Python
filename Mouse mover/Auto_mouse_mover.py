import pyautogui
import time
from tkinter import *

while 1==1:
    position = pyautogui.position()
    pyautogui.moveTo(position[0] + 30, position[1] + 30, duration = 1)
    pyautogui.moveTo(position[0], position[1], duration = 1)
    time.sleep(20)
