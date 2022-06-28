## Functions for hyper

import os
import pyautogui as pag
from pystyle import Colorate, Colors
import requests

def clear():
    os.system('cls')
def exit():
    pag.hotkey('alt', 'F4')
def help():
    print(Colorate.Horizontal(Colors.red_to_purple, f"{open('help.txt').read()}", 1))
def licence():
    print(Colorate.Horizontal(Colors.red_to_purple, f"{open('LICENCE').read()}", 1))
