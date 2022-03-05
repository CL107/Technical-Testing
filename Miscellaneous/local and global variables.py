# Author: Cameron Liddell
# Group: 12B/CS
# Date: 4/12/19
# Title: Local + Global Variables
import pyttsx3

engine = pyttsx3.init()

def local():

    global quote
    print (quote)
    quote = "Mum"
    print (quote)

quote = "Amelie"
local()
print (quote)

voices = engine.getProperty("voices")
engine.setProperty("Voice", voices[1].id)
engine.say(str(quote))
engine.runAndWait()