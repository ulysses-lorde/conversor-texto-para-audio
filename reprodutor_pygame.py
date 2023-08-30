'''Reproduzir arquivo de áudio usando pygame'''
import os

import pygame


def carregar_audio(audio_file):
    '''Carrega o arquivo de áudio'''
    # Inicializa o pygame e mixer
    pygame.init()
    pygame.mixer.init()

    # Inicia a reprodução do áudio
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    # Aguarda até que a reprodução termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Fecha o pygame
    pygame.quit()
    os.remove(audio_file)
