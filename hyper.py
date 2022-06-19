
licence = '''


'''

## Libraries needed

from distutils.log import error
import getpass
import os
import requests
from pystyle import Write, Colorate, Colors
import time
from instagramy import InstagramUser
import random
from TikTokApi import TikTokApi

banner = '''

Hyper
Copyright (C) unofficialdxnny (Danial Ahmed). All rights reserved.
Type 'Licence' to view Licence

'''
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
        ## View a websites Source
        elif split[0] == 'hyper' and split[1] == 'strip':
            source = requests.get(split[2])
            print(source.text)
            print('')

        ## Install url contents
        elif split[0] == 'hyper' and split[1] == 'install':
            url = split[2]
            r = requests.get(url, allow_redirects=True)

            open(split[3] + split[4], 'wb').write(r.content)
        

        
        ## check instauser details
        
        elif split[0] == 'hyper' and split[1] == 'instacheck':
            name = split[2]
            # instance of instagram user
            print(name)
            user = InstagramUser(name)
            print(user.is_verified)
            # total followers
            followers = user.number_of_followers
            print('Total followers:', followers)
            # total followings
            following = user.number_of_followings
            print('Total followings:',following)
            # total number of posts
            posts = user.number_of_posts
            print('Total posts:',posts)
            # bio description
            bio = user.biography
            print('Bio:\n', bio)
            # link in bio
            link_in_bio = user.website
            print('Link in Bio:', link_in_bio)
        
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
            print('Hyper Help')
            print(open('COMMANDS.txt').read())
            print('')
            print('Terminal Help')
            os.system('help')






        # elif split[0] == 'hyper' and split[1] == 'hash':
        #     my_string = input("What Is The Message You Would Like To Encode? : ")
        #     hash_object = hashlib.sha512(b'Hello World')
        #     hex_dig = hash_object.hexdigest()
        #     print(hex_dig)
        #     time.sleep(5)

        else:
            os.system(main_input)

    except KeyboardInterrupt and ImportError:
        print(error)
        os.system('cls')
        reset()