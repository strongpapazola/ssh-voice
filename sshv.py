import speech_recognition as sr
from os import system

def checkInternet():
	try:
		urlopen('https://www.google.com', timeout=1)
		return True
	except:
		return False

try:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Speak ! ...')
		audio = r.listen(source)

		try:
			text = r.recognize_google(audio)
			if text == 'SSH my server':
				print('mana????')
				system('play -q src/ssh_w.mp3')

		except:
			system('play -q src/canthear.mp3')
except:
	system('play -q src/errors.mp3')

