import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0
        self.load_music()

    def load_music(self):
        # Adicione as músicas específicas à playlist
        files = ["03 - Ela Gosta de Sambar.mp3", 
                 "Led Zeppelin - Stairway To Heaven Legendado Tradução(MP3_160K).mp3"]
        
        for file in files:
            if os.path.exists(file):
                self.playlist.append(file)
            else:
                print(f"Arquivo não encontrado: {file}")

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        self.stop_music()
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_music()

    def previous_music(self):
        self.stop_music()
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_music()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def get_current_track_info(self):
        if self.playlist:
            file_path = self.playlist[self.current_index]
            return os.path.basename(file_path), self.get_duration(file_path)
        return None, None

    def get_duration(self, file_path):
        return pygame.mixer.Sound(file_path).get_length()
