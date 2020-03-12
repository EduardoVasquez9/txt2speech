# se deben instalar gTTS desde consola
# win32com.client es opcional

import os
from gtts import gTTS
# import win32com.client as wincl

def convertirAudio(chatid, info):
    tts = gTTS(text=info, lang='es')
    tts.save("aud"+ chatid +".mp3")

    # gTTS : text -> guardar cadena o archivo de texto recibido de base de datos, guardar como txt o variable
    # tts.save : guardar el mp3 para que luego sea enviado a Telegram por medio de:
    # bot.send_audio(chat_id=chat_id, audio=open('aud[chatid].mp3', 'rb'))
