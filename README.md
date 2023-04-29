# TwitchClipsDLer

A quickly hacked together tool meant to make downloading many Twitch clips at once easier.

I originally made this script in an hour or two back on July 16th, 2022. I'm a bit of a data hoarder and so this script helps me archive twitch clips that I've made. I've been meaning to clean it up for some time now and I'm hoping to learn how to use git in the process.

## Installing and running

Clone the directory and run the given python file with the following command:

```plaintext
python TwitchClipsDLer.py
```

### What's needed to make this script work

This script uses `yt_dlp` to download these twitch clips. Install it using pip and the script should work fine.

### Using the script

The script uses an incredibly simple CLI. Just follow the instructions on screen and you should be good.

* It'll first ask you to enter the URL to a twitch clip. Do so and then press enter.

* If you make a mistake, just paste in all the rest of your clips as normal; you'll get the chance to fix your mistake later.

* Once all your links have been entered, press 'x' to continue.

* If you hit 'e', you'll be able to edit or remove certain links. Otherwise, hit anything to continue and the script should go ahead and download everything.

## Troubleshooting & Contributors

This code was hacked together many months ago at this point. I only needed it to do one thing and it does it pretty well. There are more than likely things that I'm either doing wrong or that could be done more easily in other ways. Feel free to submit pull requests and/or feedback. That being said, because of how hacked together this thing is, I'm not really going to be providing support for this. If you run into bugs or issues, feel free to submit them as well, but just don't expect too much. I don't really know what I'm doing myself.

## To Do

* Might make the script read links from a file to make downloading clips in bulk easier.
* Might make the script read links in the form of command line arguments to make downloading one or two clips a bit simpler.

## License

Copyright (C) 2023  IcePanorama

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.