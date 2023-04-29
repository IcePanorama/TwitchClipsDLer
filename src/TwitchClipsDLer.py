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
from Utilities import clear_screen


def display_links(links) -> None:
    clear_screen()
    print("Links:")

#TODO: might be able to replace this with an enum
    x = 0
    while x < len(links):
        item = x + 1
        print(str(item) + " - " + links[x])
        x += 1

    print("\n")


def link_editor(links) -> None:
    entry = ""
    while True:
        display_links(links)
        entry = input("Enter the # of the entry you'd like to edit or type [X] to continue: ")

#TODO: handle input not being of type int
        if entry.upper() == "X":
            break
        #should int(entry) be its own var?
        elif int(entry) - 1 < 0 or int(entry) - 1 >= len(links):
            print("Invalid Input")
            sleep(1)
            continue

        try:
            while True:
                user_input = input("\n[E]dit or [D]elete or [C]ancel?\n> ")
            
                match user_input.upper():
                    case "E":
                        links[int(entry) - 1] = input("Enter replacement link for #" + entry + ": ")
                        break
                    case "D":
                        links.pop(int(entry) - 1)
                        break
                    case "C":
                        break
                    case _:
                        print("Invalid Input")
                        sleep(1)
                        clear_screen()
                        display_links(links)           

        except:    
            print("Invalid Input")
            sleep(1)

    return links


#TODO: move this comment into javadocs esque comment
# DL clips as %(upload_date)s-%(timestamp)s-%(creator)s-%(title)s.%(ext)s to Clips folder
def download_links(links) -> None:
    # Should clips output to their own dir or to the root dir?
    output_format = '../%(upload_date)s-%(timestamp)s-%(creator)s-%(title)s.%(ext)s'
    timeout = 600 # in seconds
    
    ydl_opts = {
        'outtmpl': output_format,
        'socket_timeout': timeout
    }

    x = 0
    while x < len(links):
        clear_screen()
        print("Downloading clip #" + str(x + 1))
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([links[x]])
        except:
#FIXME: currently the program skips clips when errors occur. should this be handled in a better way?
            print("Download error, skipping")
            sleep(1)
        x += 1


def get_links() -> list:
    links = []
    last_response = ""

    while last_response.upper() != "X":
        last_response = input("Enter clip link or [X] to continue: ")
       
        # Prevents blank entries/entries that start with blanks
        try:
            if last_response[0] != "" and last_response[0] != " " and last_response.upper() != "X":
                links.append(last_response)
        except:
            pass

        if len(links) > 0:
            display_links(links)
    
    return links


def edit_links(links) -> None:
    display_links(links)

    user_input = input("[E]dit links or [Press Any Key to Continue]\n> ")
    if user_input.upper() == "E":
        links = link_editor(links)  


if __name__ == "__main__":
    clear_screen()

    links = get_links()

    if len(links) > 0:
        edit_links(links)

        download_links(links)