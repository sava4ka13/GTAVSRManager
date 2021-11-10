# ╔═══════════════════════════════════►
# ║   Made by sava4ka.
# ║   11/10/2021
# ║   Time spent: 4 hours
# ║   It's my third time using Python, so don't be mad.
# ║   If you use it somewhere, credit the author.
# ║
# ║
# ║  Github: https://github.com/sava4ka777/RRoulette
# ║
# ║  Luv u :3
# ║  ║▌│█│║▌║█║│║▌║
# ║  ║▌│█│║▌║█║│║▌║
# ║  ║▌│█│║▌║█║│║▌║
# ╚═══════════════════════════════════►

#Modules
import os
import sys
import shutil
import glob
from colorama import init
init()
from colorama import Fore
import pathlib
import os.path
from os import path
import time

#Cleans cmd
os.system('cls')

#Gets username
username = str(os.getlogin())

#Folder where .mp3 files located
musicfolder = "C:/Users/" + username + "/Documents/Rockstar Games/GTA V/User Music"

#Folder where User Music folder located
gtafolder = str("C:/Users/" + username + "/Documents/Rockstar Games/GTA V")

#Presets path
presetspath = str(pathlib.Path(__file__).parent.resolve()) + "\Presets"

#Prints logo
print(Fore.CYAN + "░██████╗░████████╗░█████╗░██╗░░░██╗░██████╗██████╗░███╗░░░███╗")
print(Fore.CYAN + "██╔════╝░╚══██╔══╝██╔══██╗██║░░░██║██╔════╝██╔══██╗████╗░████║")
print(Fore.CYAN + "██║░░██╗░░░░██║░░░███████║╚██╗░██╔╝╚█████╗░██████╔╝██╔████╔██║")
print(Fore.CYAN + "██║░░╚██╗░░░██║░░░██╔══██║░╚████╔╝░░╚═══██╗██╔══██╗██║╚██╔╝██║")
print(Fore.CYAN + "╚██████╔╝░░░██║░░░██║░░██║░░╚██╔╝░░██████╔╝██║░░██║██║░╚═╝░██║")
print(Fore.YELLOW + "                                          made by sava4ka     ")

#Line skip
print (" ")

#Printing options
print (Fore.MAGENTA + "1. Load Preset \n2. Save Preset \n3. Current Preset")

#Line skip
print (" ")

saveorload = int(input (Fore. RESET + "Choose option: "))

#Line skip
print (" ")

if (saveorload == 1):

    print (Fore.YELLOW + "List of presets:")
#Gets list of presets and prints them
    for i in os.listdir(presetspath):
        print (Fore.GREEN + i)

#Preset selection
    selected_preset = int(input(Fore.RESET + "Enter the preset number: "))  - 1

#Deletes User Music folder from GTA V directory
    if (path.exists(musicfolder)):
        shutil.rmtree(musicfolder)

#For Copying preset
    src_path = str(pathlib.Path(__file__).parent.resolve()) + "\Presets" + "\\" + str(os.listdir(presetspath)[selected_preset])

    dst_path = gtafolder + "/User Music"


#Copying preset to GTA V directory
    shutil.copytree(src_path, dst_path)

    print(Fore.GREEN + "Succesfuly loaded " + os.listdir(presetspath)[selected_preset] + "!")

    time.sleep(3)
    exit()
if (saveorload == 2):

        spresetname = input (Fore.RESET + "Name your preset: ",)


        src_path = gtafolder + "/User Music"

        dst_path =  str(pathlib.Path(__file__).parent.resolve()) + "\Presets" + "\\" + spresetname

        if (path.exists(dst_path)):
            print (Fore.RED + "Preset with this name already exists!")
            time.sleep(3)
            exit()

    #Copying preset to GTA V directory
        shutil.copytree(src_path, dst_path)

        print(Fore.GREEN + "Succesfuly saved " + spresetname + "!")

        time.sleep(3)
        exit()
if (saveorload == 3):
    print (" ")
    for b in os.listdir(musicfolder):
        print (Fore.GREEN + b)
