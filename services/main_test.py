#import connect_wifi
#import anvil.pico
import board
import anvil.server
import RPi.GPIO as GPIO
import neopixel
import time
from collections import namedtuple
from signal import pause

class GlobalVars:
    __slots__ = ('nbr_of_piano_keys', 'nbr_of_piano_octaves', 
                 'LED_Positions', 'chosen_key', 'chosen_scale',
                 'chosen_color', 'np', 'BRIGHTNESS',
                 'errorLED', 'connectLED', 'neopixelPin')
    
#GLOBALS = GlobalVars(48,0,[],-1,[],'blue',None,0.0,0,0,0)
GLOBALS = GlobalVars()
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "off": (0, 0, 0)
}
        

# ====== INITIALIZE ======
# ============================================
# Scale engine: binary masks for many scales
# ============================================

CHROMATIC = ["C", "C#", "D", "D#", "E", "F",
             "F#", "G", "G#", "A", "A#", "B"]
# This is an example Anvil Uplink script for the Pico W.
# See https://anvil.works/pico for more information

try:
    UPLINK_KEY = "server_VLT3LRR437O4733M4JGZU2IA-OKGXPZMYXKDDSOMG"

    # We use the LED to indicate server calls and responses.
    GPIO.setmode(GPIO.BCM)

    GLOBALS.errorLED = 4
    GPIO.setup(GLOBALS.errorLED, GPIO.OUT)
    GLOBALS.connectLED = 5
    GPIO.setup(GLOBALS.connectLED, GPIO.OUT)          
    GLOBALS.neopixelPin = 0

    # ====== CONFIGURATION ======
    GLOBALS.BRIGHTNESS = 0.2   # Brightness scale (0.0 to 1.0)

    GPIO.output(GLOBALS.connectLED, GPIO.HIGH) # Turn on

    anvil.server.connect(UPLINK_KEY, "ws://192.168.1.126:3030/uplink")

    anvil.server.wait_forever()
except Exception as e:
    print(f"An exception occurred: {e}")