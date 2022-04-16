from tkinter import *
from configparser import ConfigParser
import io

import ConfigCreate

config = ConfigParser()
cfgfile = "config.ini"
config.read('config.ini')
width = config.getint('main', width)
height = config.getint('main', height)
geometry = width+'x'+height

if __name__ == "__main__":
    Tk = Tk()
    Tk.geometry(geometry)
    Tk.title('MyFiles')
    Tk.configure(bg='light dark')


    Tk.mainloop()

