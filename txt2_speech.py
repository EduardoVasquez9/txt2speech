import pyttsx3
from gtts import gTTS
import win32com.client as wincl
import os

engine = pyttsx3.init()
# infile = 'texto.txt'
texto = engine.say(input(str("Ingrese texto:")))
# f = open(infile, 'r')
# texto = f.read()
# f.close()

# tts = gTTS(text=input(str("Ingrese texto:")), lang='es')

# gTTS : text -> guardar cadena o archivo de texto recibido de base de datos, guardar como txt o directamente el texto en el codigo
# tts.save : guardar el mp3 para que luego sea enviado a Telegram por medio de:
# bot.send_audio(chat_id=chat_id, audio=open('audio.mp3', 'rb'))

# tts.save("audio1.mp3")
engine.runAndWait()
# os.system("audio1.mp3")
