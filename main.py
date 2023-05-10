import pyttsx3

engine=pyttsx3.init()

for voice in engine.getProperty("voices"):
    pass

voices=engine.getProperty("voices")

engine.setProperty("voice",voices[1].id)

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

text=input("Enter your text : ")

Speak(text)

