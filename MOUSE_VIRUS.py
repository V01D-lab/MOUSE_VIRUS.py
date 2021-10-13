import pyautogui


pyautogui.FAILSAFE = False

width, hight = pyautogui.size()

mid_width = width / 2

mid_hight = hight / 2


while True:
    pyautogui.moveTo(mid_width, mid_hight, duration=0)