'''Reproduzir arquivo de áudio usando pygame'''
import os

import pygame


def carregar_audio(audio_file):
    '''Carrega o arquivo de áudio'''
    # Inicializa o pygame e mixer (para reprodução de áudio)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    # Iniciar a reprodução do áudio
    pygame.mixer.music.play()
    # Aguardar até que a reprodução termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Fechar o pygame
    pygame.quit()
    os.remove(audio_file)
