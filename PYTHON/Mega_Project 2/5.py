import time
import pyautogui
import pyperclip
from google import genai

# 1. Thoda delay taake tum WhatsApp window par switch kar sako
time.sleep(4)
pyautogui.click(1290,1169)
time.sleep(1)

# 2. Mouse drag karke text select karna (Start X, Y se End X, Y tak drag karega)
# Yeh coordinates apni screen aur WhatsApp chat ke hisab se adjust karne hain
pyautogui.moveTo(1445, 276)  # Jahan se text shuru hota hai
pyautogui.dragTo(1662, 771, duration=1.0, button="left")  # Jahan tak select karna hai

# 3. Ctrl + C se copy karna
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

# Clipboard se text variable mein lana
text = pyperclip.paste()
print("Copied Text:", text)


# 4. Gemini API se response generate karna
def gemini_process(command):
  client = genai.Client(
      api_key="AQ.Ab8RN6K0iBW4244Q_yk1WQtAiS-RsQl4995Avyte5c2lg9cUGw"
  )  # Yahan apni Google Gemini API key dalna
  response = client.models.generate_content(
      model="gemini-3.5-flash",
      contents=command,
  )
  return response.text


if text:
  ai_response = gemini_process(text)
  print("AI Response:", ai_response)

  # 6. AI ke jawab ko clipboard par daal kar paste aur enter (send) karna
  pyperclip.copy(ai_response)
  pyautogui.hotkey("ctrl", "v")
  time.sleep(0.5)
  pyautogui.press("enter")