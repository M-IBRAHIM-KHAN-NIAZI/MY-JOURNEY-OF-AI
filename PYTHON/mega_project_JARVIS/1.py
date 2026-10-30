
import speech recognition as sr
import webbrowser
import pyttsx3
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    speak("hi ibrahim sir how may i help you")

