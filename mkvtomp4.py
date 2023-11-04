import os
import ffmpeg
import tkinter as tk
from tkinter import filedialog

def select_files():
    input_path = filedialog.askopenfilename()
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4")
    convert_to_mp4(input_path, output_path)

def convert_to_mp4(mkv_file, mp4_file):
    ffmpeg.input(mkv_file).output(mp4_file).run()
    print("Finished converting {}".format(mkv_file))

def select_files():
    input_path = filedialog.askopenfilename()
    output_path = filedialog.asksaveasfilename(defaultextension=".mkv")
    convert_to_mkv(input_path, output_path)

def convert_to_mkv(mp4_file, mkv_file):
    ffmpeg.input(mp4_file).output(mkv_file).run()
    print("Finished converting {}".format(mp4_file))


root = tk.Tk()
buttonmp4 = tk.Button(root, text="Mkv to Mp4", command=select_files)
buttonmkv = tk.Button(root, text="Mp4 to Mkv", command=select_files)
buttonmp4.pack()
buttonmkv.pack()
root.mainloop()
