'''Reproduzir arquivo de áudio usando pygame'''
import pygame


class AudioPlayer:
    '''Classe com funções relacionadas
    à reprodução de áudio usando o pygame'''
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def play_audio(self, audio_file):
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    def close(self):
        '''Finaliza o pygame'''
        pygame.quit()
