from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from checkPictureExist import check_pic_exist
import os

pic_list = os.listdir("imgs")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    pic_result_list = []
    for pic in pic_list:
        result = check_pic_exist(pic_name=pic, confidence=0.8)
        if result:
            pic_result_list.append((pic,result))
    if len(pic_result_list)>0:
        if "final" in ",".join([x[0] for x in pic_result_list]):
                break
        elif "timeslot" in ",".join([x[0] for x in pic_result_list]):
                cur_pic_info = [x[1] for x in pic_result_list if "timeslot" in x[0]][0]
                click(cur_pic_info[0], cur_pic_info[1])
                sleep(0.25)
                click(cur_pic_info[0], cur_pic_info[1]-55)
                sleep(0.25)
                click(cur_pic_info[0], cur_pic_info[1]-110)
                sleep(0.25)
                click(cur_pic_info[0], cur_pic_info[1]-160)
                sleep(0.25)
        else:
            cur_pic_info = [x[1] for x in pic_result_list if int(x[0].split("-")[0]) == max([int(y[0].split("-")[0]) for y in pic_result_list])][0]
            click(cur_pic_info[0], cur_pic_info[1])