from SwSpotify import spotify
from swaglyrics.cli import lyrics
import tkinter as tk

# gets the current song being played
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


# mylist = tk.Listbox(root, width=50, height=20, yscrollcommand=scrollbar.set)
# mylist.pack(side="left",fill="both", expand=True)
# mylist.insert(tk.END, currentSongTitle)
# mylist.insert(tk.END, currentArtist)
# currentLyrics = currentLyrics.split('\n')
# for line in currentLyrics:
#    mylist.insert(tk.END, line)
 

# from tkinter import *

# def on_move(event):
#     component=event.widget
#     locx, locy = component.winfo_x(), component.winfo_y()
#     w , h =master.winfo_width(),master.winfo_height()
#     mx ,my =component.winfo_width(),component.winfo_height()
#     xpos=(locx+event.x)-(15)
#     ypos=(locy+event.y)-int(my/2)
#     if xpos>=0 and ypos>=0 and w-abs(xpos)>=0 and h-abs(ypos)>=0 and xpos<=w-5 and ypos<=h-5:
#        component.place(x=xpos,y=ypos)
#     return

# master = Tk()
# # master.geometry("%dx%d+0+0" % (500,500))
# msg = Label(master, text = "Click & Move")
# msg.config(bg='lightgreen', font=('Century Gothic', 24))
# # msg.bind('<B1-Motion>',on_move)
# msg.master.overrideredirect(True)
# msg.master.geometry("+250+250")
# # msg.master.lift()
# # msg.master.wm_attributes("-topmost", True)
# # msg.master.wm_attributes("-disabled", True)
# # msg.master.wm_attributes("-transparentcolor", "white")
# msg.place(x=10,y=20)
# msg.pack()
# master.bind('<B1-Motion>',on_move)
# # label = tkinter.Label(text='Lyrics here', font=('Century Gothic','20'), fg='black', bg='white')
# # label.master.overrideredirect(True)
# # label.master.geometry("+250+250")
# # label.master.lift()
# # label.master.wm_attributes("-topmost", True)
# # label.master.wm_attributes("-disabled", True)
# # # label.master.wm_attributes("-transparentcolor", "white")
# # label.pack()
# mainloop()

# label = tkinter.Label(text=currentArtist + " - " + currentSongTitle + "\n" + currentLyrics, font=('Century Gothic','20'), fg='black', bg='white')
# # label.master.overrideredirect(True)   # windows task manager will ignore the window
# # label.configure(text=spotify.song())

# label.master.geometry("+40+650")
# # label.master.lift()
# label.master.wm_attributes("-topmost", True)
# # label.master.wm_attributes("-disabled", True)       # can't interact with the window

# # # label.master.wm_attributes("-transparentcolor", "white")
# label.pack()
# label.mainloop()

# scrollbar = tkinter.Scrollbar()
# scrollbar.pack(side = "RIGHT", fill = "Y")
# scrollbar.mainloop()
