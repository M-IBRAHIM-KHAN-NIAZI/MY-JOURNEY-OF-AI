from google import genai
import pyautogui
import time
import pyperclip

# 2 second ka delay taake tum mouse ko apni jagah par set kar sako
time.sleep(4)
pyautogui.click(1266, 1167)
# 1. Jis message ko copy karna hai, us par right-click karega (tumhare coordinates ke mutabiq)
pyautogui.rightClick(1550, 690)

# 2. Thoda sa pause taake right-click menu khul jaye
time.sleep(0.5)

# 3. Menu mein 'Copy' ka option select karne ke liye keyboard key press karega 
# (Aam taur par WhatsApp par right-click menu mein 'Copy' ke liye arrow down aur enter ya shortcut use hota hai, 
# ya tum direct 'c' key press kar sakte ho agar option available ho)
pyautogui.press('down')

pyautogui.press('enter')
text=pyperclip.paste()
print(text)
def gemini_process(command):
    client = genai.Client(api_key="AQ.Ab8RN6K0iBW4244Q_yk1WQtAiS-RsQl4995Avyte5c2lg9cUGw")
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=command,
    )
    print("AI Response:", response.text)
    # speak(response.text)  # Agar text-to-speech function use kar rahe ho
    pyperclip.copy(response.text)
# Function ko call karna
if text:
    
    
    gemini_process(text)
    pyautogui.click(1558,819)
    time.sleep(1)
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")

    
