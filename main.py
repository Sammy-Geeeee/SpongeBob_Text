# SpongeBob Text Generator

# program will turn input text in the sPOngeBoB like text as the memes are.

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
