import pyautogui
import time

# Thoda delay taake tum apna mouse sahi position par le ja sako
time.sleep(2)

# 1. Pehle diye gaye coordinate (1266, 1167) par click karega
pyautogui.click(1266, 1167)

# 2. Phir start point (1087, 265) se end point (1510, 847) tak drag karega (text select karne ke liye)
pyautogui.moveTo(1114,337 )
time.sleep(0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1278, 860, duration=2) # 1 second mein drag karega
pyautogui.mouseUp()

# 3. Text ko copy karne ke liye Ctrl + C press karega
pyautogui.hotkey('ctrl', 'c')