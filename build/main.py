#!/home/songtech/anaconda3/bin/python

# Import the eel and random libraries

import eel
import random
from random import choice

# Tells eel that our html/css/js files are located in the 'web-gui' folder

eel.init('web-gui')


# This function randomly chooses an answer of yes or no

@eel.expose # Exposes this function (makes it callable) from Javascript
def mainFunction():
    output = (random.choice(['Yes', 'No']))
    if output == 'Yes':
        eel.yesFunction() # Calls yesFunction() in JavaScript
    else:
        eel.noFunction() # Calls noFunction() in JavaScript


# Starts the GUI frontend server    

eel.start('index.html', size=(1440, 900), port=0)

