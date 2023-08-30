'''Converter texto em fala em Python'''
#import os
import time

import subprocess
from gtts import gTTS


# Conta os números por unidade
MY_TEXT = 'Passe um texto como argumento'
# LANGUAGE = 'pt-br'

def gerar_arquivo_audio(my_text=MY_TEXT, language='pt-br'):
    '''Gera arquivo de áudio em português'''
    my_obj = gTTS(text=my_text, lang=language, slow=False)
    my_obj.save('test.mp3')

def reproduzir_audio(arquivo_audio='test.mp3'):
    '''Reproduz e apaga o arquivo em seguida'''
    audio_process = subprocess.Popen(['xdg-open', arquivo_audio])
    while audio_process.poll() is None:
        time.sleep(1)
    #os.remove(arquivo_audio)
