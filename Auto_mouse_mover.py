import pyautogui
import time
from tkinter import *

screensize = pyautogui.size()

while 1==1:
    pyautogui.moveTo(200, 100, duration = 1)
    time.sleep(20)
    pyautogui.moveTo(300, 100, duration = 1)
