from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os
# ('stickman.png', region = (150,175,350,600), grayscale=True, confidence = 0.8)
def check_pic_exist(pic_name,confidence,grayscale=True):
    pic_path = os.path.join(os.getcwd(),"imgs",pic_name)
    result = pyautogui.locateCenterOnScreen(pic_path,confidence=0.8, grayscale = True)
    return result


