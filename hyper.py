import os
from pystyle import Write, Colorate, Colors
import getpass
import requests
import urllib3
from urllib.error import URLError
import unofficialdxnny
banner = '''
Hyper
Copyright (C) unofficialdxnny (Danial Ahmed). All rights reserved.
Type 'Licence' to view Licence
'''
## add google search google.com/search?q=
unofficialdxnny.clear()
print(Colorate.Horizontal(Colors.red_to_purple, f"{banner}", 1))
print('')
username = getpass.getuser()

while True:
    try:
        main_input = Write.Input(f"Hyper@{username}> ", Colors.red_to_purple, interval=0.0025).lower()
        split = main_input.split()


        if split[0] == 'clear':
            unofficialdxnny.clear()











    ## Errors
    except KeyboardInterrupt:
        print('')

    except IndexError:
        print('')

    except requests.exceptions.ConnectionError:
        print('Unable to make a valid connection')

    except URLError:
        print('Unable to make a valid connection')
