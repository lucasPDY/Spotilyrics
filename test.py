from SwSpotify import spotify
from swaglyrics.cli import lyrics
import tkinter as tk

previous = None
i = 0
root = None

while i < 100000:
    # gets the current song being played
    current = spotify.song()
    while current is not None and previous != current:

        print('previous song: ', previous)
        print('current song: ', current)
        previous = current
        currentSongTitle = spotify.song()
        # gets the current artist
        currentArtist = spotify.artist()

        # gets the current lyrics of the song
        currentLyrics = lyrics(currentSongTitle, currentArtist)

        root = tk.Tk()
        root.title("Spotify Lyrics")
        root.configure( width = 10, height = 5)

        txt = tk.Text(root)
        txt.configure(font=("Century Gothic", 12), wrap='word')

        scrollbar = tk.Scrollbar(root, orient="vertical")
        scrollbar.config(command=txt.yview)
        scrollbar.pack(side="right", fill="y")
        txt.insert(tk.END, currentSongTitle + "\n")
        txt.insert(tk.END, currentArtist + "\n")
        # currentLyrics = currentLyrics.split('\n')
        txt.insert(tk.END, currentLyrics)
        txt.pack()

        # makes the window to be the topmost window
        root.wm_attributes("-topmost", True)
        root.mainloop()
        root.quit()

    
    i += 0.0001

