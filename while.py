import speech_recognition as sr
from os import system

while True:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Speak ! ...')
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			print(text)
			if text == 'hey assistant':
				print('mana????')
				system('play -q src/ssh_w.mp3')
		except:
			system('play -q src/canthear.mp3')

