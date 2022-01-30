# This is to define the main frame for the program


import tkinter as tk
from functions import *
import pyperclip


class FrameMain(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Constants for the tkinter layout here
        pad_ext = 5
        pad_int = 2
        button_width = 10


        # Elements within the main frame
        self.text_words = tk.Text(self.master, width=1000, height=1000)
        self.frame_buttons = tk.Frame(self.master)
        # And their positioning
        self.text_words.grid(row=0, column=0, padx=[2*pad_ext, 0], pady=2*pad_ext)
        self.frame_buttons.grid(row=0, column=1, padx=pad_ext, pady=pad_ext, sticky='ne')
        

        # Widgets in the buttons frame
        self.button_conv = tk.Button(self.frame_buttons, text='Convert', width=button_width, command=self.conversion)
        self.button_copy = tk.Button(self.frame_buttons, text='Copy', width=button_width, command=self.copy)
        self.button_paste = tk.Button(self.frame_buttons, text='Paste', width=button_width, command=self.paste)
        # And their positions
        self.button_conv.grid(row=0, column=0, padx=pad_ext, pady=[pad_ext, 8*pad_ext])
        self.button_copy.grid(row=1, column=0, padx=pad_ext, pady=pad_ext)
        self.button_paste.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)


    # Program window functions
    def conversion(self):
        text_input = self.text_words.get('1.0', tk.END)
        text_output = spongeBobify(text_input).rstrip('\n')
        self.text_words.delete('1.0', tk.END)
        self.text_words.insert('1.0', text_output)


    def copy(self):
        pyperclip.copy(self.text_words.get('1.0', tk.END))


    def paste(self):
        clipboard_text = pyperclip.paste()
        self.text_words.delete('1.0', tk.END)
        self.text_words.insert('1.0', clipboard_text)  
