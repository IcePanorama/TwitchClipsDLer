# "A quickly hacked together tool meant to make downloading many Twitch clips at once easier."
# Copyright (C) 2023  IcePanorama
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import yt_dlp
from time import sleep
from os import system, name

#TODO: move to separate utilities script
def ClearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def DisplayLinks(links):
    ClearScreen()
    print("Links:")

    x = 0
    while x < len(links):
        item = x + 1
        print(str(item) + " - " + links[x])
        x += 1

    print("\n")

def EditLinks(links):
    entry = ""
    while True:
        DisplayLinks(links)
        entry = input("Enter the # of the entry you'd like to edit or type [X] to continue: ")

        # check that entry exists
        if entry.upper() == "X":
            break
        else:
            # if entry != a number, throw err
            try:
                if int(entry) - 1 >= 0 and int(entry) - 1 < len(links):
                    while True:
                        userInput = input("\n[E]dit or [D]elete or [C]ancel?\n> ")
                    
                        # edit entry
                        if userInput.upper() == "E":
                           links[int(entry) - 1] = input("Enter replacement link for #" + entry + ": ")
                           break
                        # delete entry
                        elif userInput.upper() == "D":
                            links.pop(int(entry) - 1)
                            break
                        # skip entry
                        elif userInput.upper() != "C":
                            print("Invalid Input")
                            sleep(1)
                            ClearScreen()
                            DisplayLinks(links)
                        else:
                            break
                else:
                    print("Invalid Input")
                    sleep(1)
            except:    
                print("Invalid Input")
                sleep(1)

    return links

def DownloadLinks(links):
    outputFormat = 'Clips\%(upload_date)s-%(timestamp)s-%(creator)s-%(title)s.%(ext)s'
    timeout = 600 # wait 10 mins w/o internet before giving up
    
    ydl_opts = {
        'outtmpl': outputFormat,
        'socket_timeout': timeout
    }

    x = 0
    while x < len(links):
        ClearScreen()
        print("Downloading clip #" + str(x + 1))
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([links[x]])
        except:
            print("Download error, skipping")
            sleep(1)
        x += 1

def Main():
    links = [];

    # Prompt user for to either enter a twitch link or X to quit
    lastResponse = "";
    while lastResponse.upper() != "X":
        lastResponse = input("Enter clip link or [X] to continue: ")
       
        # Prevents blank entries/entries that start with blanks
        try:
            if lastResponse[0] != "" and lastResponse[0] != " " and lastResponse.upper() != "X":
                links.append(lastResponse)
        except:
            pass

        if len(links) > 0:
            DisplayLinks(links)

    if len(links) > 0:
        # Display list of clip links
        DisplayLinks(links)

        # prompt user to say they're correct or to enter the link # to replace it
        userInput = input("[E]dit links or [Press Any Key to Continue]\n> ")
        if userInput.upper() == "E":
            links = EditLinks(links)  

        # DL clips as %(upload_date)s-%(timestamp)s-%(creator)s-%(title)s.%(ext)s to Clips folder
        DownloadLinks(links)

if __name__ == "__main__":
    ClearScreen()
    Main()
