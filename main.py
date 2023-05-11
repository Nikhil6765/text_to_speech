import pyttsx3                      # text-to-speech conversion library and it works offline

engine=pyttsx3.init()                         # object created 

for voice in engine.getProperty("voices"):    
    pass

voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def Speak(Audio):               # creating a function that helps us to convert a text to speech. 
    engine.say(Audio)           # the function is used to speak our program
    engine.runAndWait()         # used to wait for our program for the next execution,


text=input("Enter your text : ")

Speak(text)

