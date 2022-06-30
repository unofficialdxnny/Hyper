## Functions for hyper

import os
import pyautogui as pag
from pystyle import Colorate, Colors, Write
import requests
import pyjokes
from instagramy import InstagramUser
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
def internet_protocol():
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=6c651011137a45e2bc146eb14a3fda7e")
    Write.Print(f"{response.content}", Colors.orange, interval=0)
    print('')
def insuser():
    # user input
    name = Write.Input(f"Persons Instagram Username : ", Colors.red_to_purple, interval=0)
    # instance of instagram user
    user = InstagramUser(name)
    # total followers
    followers = user.number_of_followers
    print('Total followers:', followers)
    # total followings
    following = user.number_of_followings
    print('Total followings:',following)
    # total number of posts
    posts = user.number_of_posts
    print('Total posts:',posts)