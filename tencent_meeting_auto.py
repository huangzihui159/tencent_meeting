import time
import win32api
import win32con
import os
import keyboard
import win32gui
def doClick(cx,cy,hwnd):
    long_position =win32api.MAKELONG(cx,cy)
    win32api.PostMessage(hwnd,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,long_position)
    time.sleep(0.1)
    win32api.PostMessage(hwnd,win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,long_position)

def get_all_windows():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    return hWnd_list

def get_title(hwnd):
    title = win32gui.GetWindowText(hwnd)
    return title

def get_hwnd_from_name(name):
     hWnd_list = get_all_windows()
     for hwd in hWnd_list:
        title = get_title(hwd)
        if title == name:
            return hwd

def get_son_windows(parent):
    hWnd_child_list = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hWnd_child_list)
    for hwnd in hWnd_child_list:
        get_title(hwnd)
    if hWnd_child_list:
        return hWnd_child_list

def get_meeting_hld():
    hld_list=get_all_windows()
    for i in hld_list:
        clsname = win32gui.GetClassName(i)
        if clsname == 'TXGuiFoundation':
            b=get_son_windows(i)
            if b:
                print(b)
                return b[2]

def test_hld():
    a=get_meeting_hld()
    qiandao_page=get_title(a)
    if qiandao_page == 'Chrome Legacy Window':
        return a

hld=test_hld()

while True:
    flag = False
    def key_press(key):
        global flag
        if key.name == '-':
            flag = True
    keyboard.on_press(key_press)
    doClick(260,311,hld)
    print("-键终止")
    time.sleep(1)
    if flag == True:
        print("终止")
        flag = False
        os._exit(0)