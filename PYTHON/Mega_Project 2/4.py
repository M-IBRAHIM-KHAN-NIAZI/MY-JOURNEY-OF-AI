import time
import pyautogui
import pyperclip
from google import genai


def gemini_process(command):
  client = genai.Client(api_key="TERI_API_KEY_YAHAN_DALO")
  response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=command,
  )
  return response.text


# 2 second ka delay taake tu WhatsApp window par focus kar sake
time.sleep(2)

# 1. Last message ki jagah par click karna (Apni screen ke mutabiq coordinates set karna)
pyautogui.click(1294, 1166)
time.sleep(1)

# 2. Ctrl + A ki bajaye Mouse Drag ya Triple Click se sirf ek message select karna
# Yahan hum triple click ya drag ka use kar sakte hain, ya phir shortcut keys:
# Agar WhatsApp mein last message par double/triple click karein toh sirf wohi select hota hai
pyautogui.click(1294, 1166, clicks=3, interval=0.25)
time.sleep(1)

# 3. Copy karna
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

# 4. Clipboard se text uthana
text = pyperclip.paste()
print("Copied Last Message:", text)

if text:
  # 5. Gemini API se response lena
  ai_response = gemini_process(text)
  print("AI Response:", ai_response)

  # 6. WhatsApp ke type box par click karke response paste aur send karna
  pyautogui.click(1266, 1167)  # Type box coordinates
  time.sleep(1)

  pyperclip.copy(ai_response)
  pyautogui.hotkey("ctrl", "v")  # Paste
  time.sleep(0.5)
  pyautogui.press("enter")  # Send
    