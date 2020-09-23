# Import the eel and random libraries

import eel
import random
from random import choice

# Starts the GUI frontend server    


eel.init('web-gui')

eel.start('index.html', size=(1440, 900))


# This function randomly chooses an answer of yes or no

@eel.expose # Exposes this function (makes it callable) from Javascript
def mainFunction():
    output = (random.choice(['Yes', 'No']))
    if output == 'Yes':
        eel.yesFunction() # Calls yesFunction() in JavaScript
    else:
        eel.noFunction() # Calls noFunction() in JavaScript

# For dev purposes only:

while True:
    eel.sleep(10)