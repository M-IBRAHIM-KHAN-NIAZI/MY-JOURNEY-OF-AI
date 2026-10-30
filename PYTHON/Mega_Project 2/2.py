import pyautogui
import time
import pyperclip

# 2 second ka delay taake tum tayar ho sako
time.sleep(3)

# 1. Jis jagah ya icon par click karna hai (tumhara coordinate: 1266, 1167)
pyautogui.click(1294, 1166)

# 2. Thoda sa pause taake window focus mein aa jaye
time.sleep(1)

# 3. Poora text select karne ke liye Ctrl + A press karega
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
# 4. Text ko copy karne ke liye Ctrl + C press karega
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
text=pyperclip.paste()
print(text)