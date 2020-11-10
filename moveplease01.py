#!/usr/bin/env python3


import shutil

import os

os.chdir('/home/student/mycode/')
#force the Python program to 'start' in the home user directory, which for us will be /home/student/mycode/. This is made possible by calling os.chdir(). This will allow the user to run the program from any location on the system and our script still always start at /home/student/mycode/
shutil.move('raynor.obj', 'ceph_storage/')
#Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location. If destination points to a folder, the source file gets moved into destination and keeps its current filename.
xname = input('What is the new name for kerrigan.obj? ')
#Prompt the user for a new name for the kerrigan.obj file.
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
#Rename the current kerrigan.obj file.

