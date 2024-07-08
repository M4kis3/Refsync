# Refsync
A simple video player, inspired by Chris Zurbrigg's keyframe pro.

Main usage is to sync Autodesk Maya timeline to a video reference, instead of using laggy image planes.

## Installation

Download the maya_http_server.py file into your maya default scripts directory. It should generally be located in Documents\maya\scripts
Download the playeer_z.html file.
You can place the player_z.html file anywhere you like, preferably a convenient place to run.
## Usage
Now in Maya, open the script editor and make a new python tab. Paste this code:
```
import maya_http_server.py 

maya_http_server.start_server()
```
Now go to File>Save Script to Shelf in the script editor.

Now on clicking the shelf button, in the script editor history, it should show that a server has started on port 8000.[^1]
[^1]: If your port 8000 is not available, just go into the maya_http_server.py script and edit the port number in notepad and do the same for the html file.

Windows might give you a worning that a connection is trying to be established, just allow it, as it is only on your local network.

Now open the html file in a browser, preferably Chrome or Firefox.

You should have options to upload a video file from your computer, and when you click the Sync button on the bottom left and it says sync on, the maya timeline number shou,d be the same as the video frame number.

You can use this sync button to toggle sync on and off. Now if you know the video uploaded's frame rate, enter it into the frame rate input, and you will get more accurate frame by frame sync.

The offset input, adds the offset frames to the maya synced frame, and the multiplier input multiplies the maya frame input by this multiplier value. Use the size drop down menu to change the size of the player. 

You can also use the clone button on the top to create a new window with the same function, and maybe add another video reference to use.

## Deficiencies
I am not a professional coder, so I'm not fully aware of any deficiencies in my code, and I'm also not liable to any harm come to your device, should you install this script. 

This is just a 'free' version of keyframe pro I made cause I dont want to pay for it.

Unfortunately I haven't added working functionality that closes the server, so once you close maya, the server will be closed.

If you have any ideas or can make this better, please go ahead and create a better version on a fork. i would really appreciate it.
