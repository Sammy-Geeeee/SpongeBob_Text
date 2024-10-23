# SpongeBob Text Generator

""""
This program will turn input text in the sPOngeBoB like text as the memes are

The purpose of this program was my own entertainment...
And it was also the first standalone program of any sort I made outside of a tutorial
"""

import tkinter as tk
from frameMain import *
from functions import *


class Window:
    def __init__(self, root, title, geometry):
        # This will set all the base info for the main window
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

        # To allow the expandability of all the rows and columns needed
        root.columnconfigure([0], weight=1)
        root.rowconfigure([0], weight=1)

        FrameMain(root)  # To make the main frame

        self.root.mainloop()  # To actually run the program loop


def main():
    window = Window(tk.Tk(), 'SpongeBob Text', '800x500')  # Main window defined here


main()
