import os
import eel
from engine.features import play_start_sound  # Import the renamed function
from engine.command import *


def start():
    eel.init("www")
    play_start_sound()

    # Open the app in the default browser
    os.system('start msedge --app="http://localhost:8000/index.html"')

    # Start the Eel application
    eel.start('index.html', mode=None, host='localhost', block=True)

if __name__ == '__main__':
    start()  # This allows you to run main.py directly if needed