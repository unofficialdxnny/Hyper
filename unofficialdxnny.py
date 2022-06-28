## Functions for hyper

import os
import pyautogui as pag
from pystyle import Colorate, Colors, Write
import requests
import pyjokes
def clear():
    os.system('cls')
def exit():
    pag.hotkey('alt', 'F4')
def help():
    print(Colorate.Horizontal(Colors.red_to_purple, f"{open('help.txt').read()}", 1))
def licence():
    print(Colorate.Horizontal(Colors.red_to_purple, f"{open('LICENCE').read()}", 1))
def joke():
    joke = pyjokes.get_joke()
    Write.Print(f"{joke}", Colors.orange, interval=0.025)
    print('')