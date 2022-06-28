from pystyle import Write, Colorate, Colors
import getpass
import requests
import urllib3
from urllib.error import URLError
import unofficialdxnny
import os
import pyautogui as pag
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
def reset():
    print(Colorate.Horizontal(Colors.red_to_purple, f"{banner}", 1))
    print('')
while True:
    try:
        main_input = Write.Input(f"Hyper@{username}> ", Colors.red_to_purple, interval=0).lower()
        split = main_input.split()


        if split[0] == 'clear' or split[0] == 'cls' or split[0] == 'clean':
            unofficialdxnny.clear()
        
        
        elif split[0] == 'reset':
            unofficialdxnny.clear()
            reset()

        
        elif split[0] == 'exit':
            unofficialdxnny.exit()
        
        
        elif split[0] == 'hyper' and split[1] == 'help':
            unofficialdxnny.help()
            print('')
            
        elif split[0] == 'licence':
            unofficialdxnny.licence()

        ## View a websites Source
        elif split[0] == 'hyper' and split[1] == 'strip':
            source = requests.get(split[2])
            print(source.text)
            print('')
        






        else:
            os.system(main_input)




    ## Errors
    except KeyboardInterrupt:
        print('')

    except IndexError:
        print('')

    except requests.exceptions.ConnectionError:
        print('')
        Write.Print(f"Unable to make a valid connection!", Colors.red, interval=0)
        print('')
    except requests.exceptions.MissingSchema:
        Write.Print(f"Link should start with 'https' or 'http'!", Colors.red, interval=0)
        print('')
    except URLError:
        Write.Print(f"Unable to make a valid connection!", Colors.red, interval=0)
        print('')
    except FileNotFoundError:
        Write.Print(f"Commands not found...", Colors.red, interval=0)
        print('')