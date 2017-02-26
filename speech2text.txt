#!/usr/bin/env python

import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	
	print("Say something!")
 	audio = r.listen(source)

try:
 f=open('myfile.txt','w')
 f.write(r.recognize_google(audio))
 f.close()
except LookupError:
 print("Could not understand audio")