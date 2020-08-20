#!/usr/bin/python3.8
# coding:u8

###### RESSOURCES ###########################################################
# https://docs.python.org/3/library/tkinter.html
# https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
# https://www.tutorialspoint.com/python/tk_checkbutton.htm


import tkinter as tk
from os import path,chdir, listdir
from math import *


from file_management import create_user_folder, read_an_object
from data import list_owned_units
from commands import *
from displaying import Application


"""
This program help you to create a Blood Angels army list for Warhammer 4k.

- select the figurines you have ;
- select the figurines you want to play ;
- count the power value ;
- get a file with all unit profiles you need.

This program is a work to progress.

"""

def main_loop():
    create_user_folder()

    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Codex Warhammer Blood Angels")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    app.master.minsize(round(width/2), round(height/2))
    
    app.display_main_frame()

    app.display_frame_existing()

    app.display_frame_owned()

    app.display_frame_choosen()

    app.display_last_frame()

    app.mainloop()

if __name__ == '__main__':
    main_loop()





# cd /home/jaenne/Python/codex_warhammer
# ./codex.py