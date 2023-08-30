'''Converter texto em fala em Python'''
import time

import subprocess
from gtts import gTTS

def gerar_arquivo_audio(language='pt-br'):
    '''Gera arquivo de áudio em português'''
    my_obj = gTTS(text='oi', lang=language, slow=False)
    my_obj.save('static/test.mp3')

def reproduzir_audio(arquivo_audio='test.mp3'):
    '''Reproduz e apaga o arquivo em seguida'''
    audio_process = subprocess.Popen(['xdg-open', arquivo_audio])
    while audio_process.poll() is None:
        time.sleep(1)
    #os.remove(arquivo_audio)
