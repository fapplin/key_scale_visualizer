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
        
    
def set_pixel(index):
    global GLOBALS

    """Set a single pixel color with brightness scaling."""
    
    r, g, b = COLORS.get(GLOBALS.chosen_color)
    GLOBALS.np[index] = (int(r * GLOBALS.BRIGHTNESS), int(g * GLOBALS.BRIGHTNESS), int(b * GLOBALS.BRIGHTNESS))
    #time.sleep(0.05)
    GLOBALS.np.write()

def set_pixel_rgb(index, rgb_color):
    global GLOBALS

    """Set a single pixel color with brightness scaling."""
    
    r, g, b = rgb_color
    GLOBALS.np[index] = (int(r * GLOBALS.BRIGHTNESS), int(g * GLOBALS.BRIGHTNESS), int(b * GLOBALS.BRIGHTNESS))
    #time.sleep(0.05)
    GLOBALS.np.write()

def fill_color(color):
    global GLOBALS

    """Fill the entire strip with one color."""
    for i in range(GLOBALS.nbr_of_piano_keys):
        set_pixel(i)
    GLOBALS.np.write()
    
def fill_color_rgb(color):
    global GLOBALS

    """Fill the entire strip with one color."""
    for i in range(GLOBALS.nbr_of_piano_keys):
        set_pixel_rgb(i, color)
    GLOBALS.np.write()
    
def color_wipe(color, delay=0.05):
    """Light up LEDs one by one."""
    for i in range(GLOBALS.nbr_of_piano_keys):
        set_pixel(i, color)
        GLOBALS.np.write()
        time.sleep(delay)

def csv_to_int_list(csv_string):
    """
    Convert a comma-separated string of numbers into a list of integers.
    Handles spaces and validates numeric values.
    """
    if not isinstance(csv_string, str):
        raise TypeError("Input must be a string.")

    # Split by comma and strip spaces
    items = csv_string.split(",")
    
    result = []
    for item in items:
        item = item.strip()  # Remove leading/trailing spaces
        if item == "":
            continue  # Skip empty entries
        try:
            result.append(int(item))
        except ValueError:
            raise ValueError(f"Invalid number found: '{item}'")
    
    return result


def scale_mask(root_note: str, intervals: list[int]) -> list[int]:
    """Return a 12-bit chromatic mask for a given root and interval pattern."""
    
    print("in scale_mask")
    root_index = CHROMATIC.index(root_note)
    notes = [root_index]
    current = root_index

    for step in intervals:
        current = (current + step) % 12
        notes.append(current)

    mask = [0] * 12
    for i in notes:
        mask[i] = 1

    return mask

def scale_matrix_for_interval(scale_intervals) -> dict[str, list[int]]:
    """Return a dict: root -> 12-bit mask for all 12 roots of a given scale type."""
    print("in scale_matrix_for_interval")
    print(f"scale_intervals: {scale_intervals}")
    
    #intervals = SCALE_FORMULAS[scale_type]
    intervals = scale_intervals
    print("intervals:")
    print(intervals)
    
    return {
        root: scale_mask(root, intervals)
        for root in CHROMATIC
    }

def print_key_scale_matrix(key_type, scale_intervals):
    """Pretty-print a 12x12 matrix for a given scale type."""
    
    print("in print_key_scale_matrix")
    print(f"key_type: {key_type}, scale_intervals: {scale_intervals}")
    matrix = scale_matrix_for_interval(scale_intervals)

    mask = matrix[key_type]
    bits = ", ".join(str(b) for b in mask)
    print(f" -> {bits}")
    new_list = [int(i) for i in bits.split(',')]
    print(new_list)
    return new_list

def rotate_list(nums, k):
    k = k % len(nums) # Handle cases where k > len(nums)
    return nums[-k:] + nums[:-k]

@anvil.server.callable()
def pico_fn_number_of_leds(nbr_leds):
    global GLOBALS
    
    print(f"Called pico_fn_number_of_leds")
    print(nbr_leds)
    GLOBALS.np = neopixel.NeoPixel(GLOBALS.neopixelPin, int(nbr_leds))
    #fill_color((0, 0, 0))  # Black
    GLOBALS.np.write()
    

@anvil.server.callable()
def pico_fn_led_positions(led_pos):
    global GLOBALS
    print(f"Called pico_fn_led_positions")
    print(led_pos)
    GLOBALS.LED_Positions = csv_to_int_list(led_pos)
    
@anvil.server.callable()
def pico_fn_number_of_octaves(nbr_octs):
    global GLOBALS
    print(f"Called pico_fn_number_of_octaves")
    print(nbr_octs)
    GLOBALS.nbr_of_piano_octaves = int(nbr_octs)
    GLOBALS.nbr_of_piano_keys = GLOBALS.nbr_of_piano_octaves * 12

    
@anvil.server.callable()
def pico_fn_keys(key):
    global GLOBALS
    # Output will go to the Pico W serial port
    print(f"Called pico_fn_keys")
    print(key)
    GLOBALS.chosen_key = key
    
    return key * 2

@anvil.server.callable()
def pico_fn_scales(scale):
    global GLOBALS
    # Output will go to the Pico W serial port
    print(f"Called pico_fn_scales")
    print(scale)
    
    GLOBALS.chosen_scale = csv_to_int_list(scale)
    
    return scale

@anvil.server.callable()
def pico_fn_scale_color(scale_color):
    global GLOBALS
    # Output will go to the Pico W serial port
    print(f"Called pico_fn_scale_color")
    print(scale_color)
    
    GLOBALS.chosen_color = scale_color
    
    return scale_color

@anvil.server.callable()
def pico_fn_startleds(n):
    global GLOBALS
    piano_keys = []
    # Output will go to the Pico W serial port
    print(f"Called pico_fn_startleds")
    
    print("Chosen scale")
    key_str = CHROMATIC[GLOBALS.chosen_key]
    print(f"key_str: {key_str}")
    print(f"chosen_scale: {GLOBALS.chosen_scale[0]}")
    
    new_scale = print_key_scale_matrix(key_str, GLOBALS.chosen_scale)
    print(f"new_scale: {new_scale}")
    
    if GLOBALS.chosen_key == -1 or GLOBALS.chosen_scale == "None":
        return
     
    #***************************************************
    # Fill a list with the particular scale in the
    # seen on a piano from left to right.
    #***************************************************
    for i in range(0, GLOBALS.nbr_of_piano_octaves):
        for j in range(0, 12):
            piano_keys.insert(0, new_scale[j])
    
            
    print("Original list")
    print(list(piano_keys))
    
    print("chosen_key:")
    print(GLOBALS.chosen_key)
    #***************************************************
    # Now, we rotate the list based on the key chosen.
    #***************************************************
    #rotated_piano_keys_list = rotate_list(piano_keys, chosen_key)
    
    piano_keys.reverse()
    
    print("reversed piano_keys: ")
    print(list(piano_keys))
    len_piano_keys = len(piano_keys) - 1
    
    fill_color_rgb((0, 0, 0))  # Black
    
    print(f"LED_Positions: {GLOBALS.LED_Positions}")
    
    led_cnt = len(GLOBALS.LED_Positions) - 1
    print(f"led_cnt: {led_cnt}")
    
    for i in range(len_piano_keys, -1, -1):
        print(f"{i}, {piano_keys[i]}")
        if piano_keys[i] == 1:
            print(f"{i}, GLOBALS.LED_Positions[{led_cnt}]: {GLOBALS.LED_Positions[led_cnt]}")
            set_pixel(GLOBALS.LED_Positions[led_cnt]) #blue
        else:
            set_pixel_rgb(GLOBALS.LED_Positions[led_cnt], (0, 0, 0))  # Black
        led_cnt -= 1
    
    #set_pixel(94, (0, 0, 255)) #blue
    print(" end pico_fn_startleds")

    return 1


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