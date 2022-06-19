

## Libraries needed

from distutils.log import error
import getpass
import os
from urllib.error import URLError
import requests
from pystyle import Write, Colorate, Colors
import time
from instagramy import InstagramUser
import instaloader
import random
from TikTokApi import TikTokApi
import urllib3
import vlc

banner = '''

Hyper
Copyright (C) unofficialdxnny (Danial Ahmed). All rights reserved.
Type 'Licence' to view Licence

'''
## add google search google.com/search?q=
os.system('cls')
print(Colorate.Horizontal(Colors.red_to_purple, f"{banner}", 1))
print('')
username = getpass.getuser()
def clear():
    os.system('cls')

def Licence():
    print('')
    print(open('LICENCE.txt').read())
    
def reset():
    print(Colorate.Horizontal(Colors.red_to_purple, f"{banner}", 1))
    print('')

while True:
    try:
        main_input = Write.Input(f"Hyper@{username}> ", Colors.red_to_purple, interval=0.0025).lower()
        split = main_input.split()
        ## Displays licence for this project
        if main_input == 'licence':
            Licence()
            print('')
        ## clears terminal
        elif main_input == 'cls':
            clear()

        ## clears terminal
        elif main_input == 'clear':
            clear()

        ## Resets terminal to default
        elif main_input == 'reset':
            clear()
            reset()

        ## Install url contents
        elif split[0] == 'hyper' and split[1] == 'install':
            url = split[2]
            r = requests.get(url, allow_redirects=True)

            open(split[3] + split[4], 'wb').write(r.content)
        

        
        ## check instauser details
        # (broken)
        ##elif split[0] == 'hyper' and split[1] == 'instacheck':
        ##    # Connecting the profile
        ##    user = InstagramUser(split[2])

        ##    
        ##    print(user.is_verified())
        ##    print(user.popularity())
        ##    print(user.get_biography())
        ##    posts = user.get_posts_details()
        ##    print('\n\nLikes', 'Comments')
        ##    for post in posts:
        ##        likes = post["likes"]
        ##        comments = post["comment"]
        ##        print(likes,comments)

            
        ## install a tiktok video
        elif split[0] == 'hyper' and split[1] == 'tikinstall':
            with TikTokApi() as api:
                video = api.video(id=split[2])

                # Bytes of the TikTok video
                video_data = video.bytes()
            
                tiktok_name = random.random()
                with open(f"tiktok-{tiktok_name}.mp4", "wb") as out_file:
                    out_file.write(video_data)

        
        elif main_input == 'help':
            print('')
            print(Colorate.Horizontal(Colors.red_to_purple, f"Hyper Help", 1))
            print(open('COMMANDS.txt').read())
            print('')
            print(Colorate.Horizontal(Colors.red_to_purple, f"Terminal Help", 1))
            os.system('help')



        ## play audio within terminal (.mp3 and .wav) 
        elif split[0] == 'hyper' and split[1] == 'play':
            media = vlc.MediaPlayer(split[2])
            media.play()

        ## View a websites Source
        elif split[0] == 'hyper' and split[1] == 'strip':
            source = requests.get(split[2])
            print(source.text)
            print('')
            
        
        # elif split[0] == 'hyper' and split[1] == 'hash':
        #     my_string = input("What Is The Message You Would Like To Encode? : ")
        #     hash_object = hashlib.sha512(b'Hello World')
        #     hex_dig = hash_object.hexdigest()
        #     print(hex_dig)
        #     time.sleep(5)
        elif main_input == '':
            print("Invalid Input type 'help' for help")




        else:
            os.system(main_input)

    except KeyboardInterrupt:
        os.system('cls')
        reset()
    
    except IndexError:
        print('')

    except requests.exceptions.ConnectionError:
        print('Unable to make a valid connection')

    except URLError:
        print('Unable to make a valid connection')