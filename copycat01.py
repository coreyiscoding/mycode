#!/usr/bin/env python3

import shutil
#imports common toold built into python
import os
#imports operating system 
os.chdir('/home/student/mycode/')
#allow the user to run the program from any location on the system and our script still always start
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
#will copy the file at the path source to the folder at the path destination 
shutil.copytree('5g_research/', '5g_research_backup/')
#will copy the file at the path source to the folder at the path destination 
