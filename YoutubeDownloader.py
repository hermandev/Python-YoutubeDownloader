import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def CreateWidgets():
    linkLabel = Label(root, text="Maskan Link Video")
    linkLabel.grid(row=1, column=0, pady=5, sticky="E")

    root.linkText = Entry(root, width=45)
    root.linkText.grid(row=1, column=1, pady=5, columnspan=2, sticky="W")

    destinationLabel = Label(root, text="Save Directory")
    destinationLabel.grid(row=2, column=0, pady=5, sticky="E")

    root.destinationText = Entry(root, width=35)
    root.destinationText.grid(row=2, column=1, pady=5, sticky="W")

    browseButton = Button(root, text="Browse", command=Browse, width=5)
    browseButton.grid(row=2, column=2, pady=5, sticky="W")
    downloadButton = Button(root, text="Download", command=Downloads, width=31)
    downloadButton.grid(row=3, column=1, pady=5)


def Browse():
    root.destinationDIR = filedialog.askdirectory(initialdir="~/Downloads")
    root.destinationText.insert('1', root.destinationDIR)

def Downloads():
    getVideo = YouTube(root.linkText.get())
    videoStream = getVideo.streams.first()
    videoStream.download(root.destinationDIR)
    messagebox.showinfo("Berhasil", "Video berhasil di download")


root = tk.Tk()
root.geometry("520x130")
root.title("YouTube Downloader Python3")
root.resizable(False, False)
CreateWidgets()
root.mainloop()

