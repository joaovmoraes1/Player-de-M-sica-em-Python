import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from player import MusicPlayer
import os

class MusicPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.player = MusicPlayer()

        self.title("Music Player")
        self.geometry("400x300")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        # Customize theme colors for a modern look
        self.style.configure('TButton', background='#333333', foreground='#ffffff', font=('Helvetica', 10), padding=10, borderwidth=0)
        self.style.configure('TLabel', background='#333333', foreground='#ffffff', font=('Helvetica', 10))
        self.style.configure('TScale', background='#333333', foreground='#ffffff', troughcolor='#40444b', sliderrelief='flat', sliderthickness=8)
        self.style.configure('TFrame', background='#333333')
        self.style.map('TButton', foreground=[('active', '#333333'), ('pressed', '#333333')])  # Keep text color when active/pressed

        # Add color for highlight buttons
        self.style.configure('Highlight.TButton', background='#FF8C00', foreground='#ffffff')  # Orange highlight

        self.create_widgets()
        self.update_track_info()

    def create_widgets(self):
        frame_controls = ttk.Frame(self)
        frame_controls.pack(pady=10)

        self.load_button = ttk.Button(frame_controls, text="Load Music", command=self.load_music)
        self.load_button.grid(row=0, column=0, padx=5, pady=5)

        self.play_button = ttk.Button(frame_controls, text="Play", command=self.player.play_music, style='Highlight.TButton')
        self.play_button.grid(row=0, column=1, padx=5, pady=5)

        self.pause_button = ttk.Button(frame_controls, text="Pause", command=self.player.pause_music, style='Highlight.TButton')
        self.pause_button.grid(row=0, column=2, padx=5, pady=5)

        self.unpause_button = ttk.Button(frame_controls, text="Unpause", command=self.player.unpause_music, style='Highlight.TButton')
        self.unpause_button.grid(row=0, column=3, padx=5, pady=5)

        self.stop_button = ttk.Button(frame_controls, text="Stop", command=self.player.stop_music, style='Highlight.TButton')
        self.stop_button.grid(row=0, column=4, padx=5, pady=5)

        self.next_button = ttk.Button(frame_controls, text="Next", command=self.next_music, style='Highlight.TButton')
        self.next_button.grid(row=1, column=1, padx=5, pady=5)

        self.previous_button = ttk.Button(frame_controls, text="Previous", command=self.previous_music, style='Highlight.TButton')
        self.previous_button.grid(row=1, column=0, padx=5, pady=5)

        self.volume_label = ttk.Label(self, text="Volume")
        self.volume_label.pack(pady=10)

        self.volume_scale = ttk.Scale(self, from_=0, to=1, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=10)

        self.track_info_label = ttk.Label(self, text="", wraplength=300, font=("Helvetica", 10), foreground='#ffffff')
        self.track_info_label.pack(pady=10)

    def load_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.player.playlist.append(file_path)
            self.player.current_index = len(self.player.playlist) - 1
            self.player.play_music()
            self.update_track_info()

    def set_volume(self, volume):
        self.player.set_volume(float(volume))

    def next_music(self):
        self.player.next_music()
        self.update_track_info()

    def previous_music(self):
        self.player.previous_music()
        self.update_track_info()

    def update_track_info(self):
        track_name, duration = self.player.get_current_track_info()
        if track_name:
            info_text = f"Now Playing: {track_name}\nDuration: {duration:.2f} seconds"
        else:
            info_text = "No track loaded"
        self.track_info_label.config(text=info_text)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = MusicPlayerApp()
    app.run()