import time
import board
import neopixel
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
PIXEL_PIN = board.D18      # GPIO pin connected to the pixels


WATCH_FILE = Path("/home/frank/anvildir/led_client/leds.txt")
pixels = None


# Color Map: String to (R, G, B)
COLOR_MAP = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "off": (0, 0, 0)
}

def process_led_file(file_path):
    global pixels
    try:
        with open(file_path, "r") as f:
            line_cnt = 0
            for line in f:
                print("line:")
                print(line)
                line_cnt += 1
                #******************************************
                # Read first line of file which is the
                # number of pixels of the LED strip. Also
                # turn off all of the pixels in the strip.
                #******************************************
                if line_cnt == 1:
                    print("line_cnt == 1")
                    ORDER = neopixel.GRB       # Or RGB, depending on your strip
                    NUM_PIXELS = int(line)   # Number of pixels in your strip  
                    # Setup the NeoPixel strip
                    print("Setup the NeoPixel strip")
                    pixels = neopixel.NeoPixel(PIXEL_PIN, 210,             brightness=0.2, auto_write=True,     pixel_order=ORDER) 
                    color_name = "off"
                    print("color_name = off")
                    rgb_value = COLOR_MAP.get(color_name)
                    print("looping through pixels")
                    pixels.fill((0,0,0))
                    print("done")
                else:
                    #********************************************
                    # Get the pairs from the file ex. 10w,blue.
                    # The 10 would be the pixel to light up. The
                    # 'w' tells you it's a white key ('b' for 
                    # black key). 'blue' is the color to light
                    # the LED to. Unless it a black key then
                    # make it magenta.
                    #********************************************
                    parts = [p.strip().lower() for p in line.split(",")]
                    print("parts:")
                    print(parts)
                
                    if len(parts) == 2:
                        key_color = ""
                        index_str, color_name = parts
                        print("index_str:")
                        print(index_str)
                        print("color_name:")
                        print(color_name)
                        #************************************
                        # key_color should be 'w' or 'b'.
                        #************************************
                        key_color = index_str[-1]
                        print("key_color:")                   
                        print(key_color)
                        
                        # 1. Convert index to integer
                        len_index_str = len(index_str) - 1
                        #************************************
                        # pixel_index is the pixel position
                        # on the led string.
                        #***********************************
                        pixel_index = int(index_str[0:len_index_str])
                        print("pixel_index:")
                        print(pixel_index)
                        
                        # 2. Convert color string to RGB tuple
                        rgb_value = COLOR_MAP.get(color_name)

                        if rgb_value and 0 <= pixel_index < NUM_PIXELS:
                            print(color_name)
                            if key_color == "b" and color_name != "off":       
                                rgb_value = COLOR_MAP.get("magenta")
                                    
                            pixels[pixel_index] = rgb_value
                            print(f"Set pixel {pixel_index} to {color_name} {rgb_value}")
                        else:
                            print(f"Skipping: Invalid index {pixel_index} or color '{color_name}'")
    except Exception as e:
        print(f"Error: {e}")

class LedFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Using .resolve() handles absolute/relative path comparisons safely
        print("LedFileHandler()")
        if Path(event.src_path).resolve() == WATCH_FILE.resolve():
            process_led_file(WATCH_FILE)

if __name__ == "__main__":
    # Ensure the directory exists
    WATCH_DIR = WATCH_FILE.parent
    if not WATCH_DIR.exists():
        print(f"Error: Directory {WATCH_DIR} does not exist.")
    else:
        event_handler = LedFileHandler()
        observer = Observer()
        observer.schedule(event_handler, str(WATCH_DIR), recursive=False)

        print(f"Monitoring {WATCH_FILE.name} for NeoPixel commands...")
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            pixels.fill((0, 0, 0)) # Turn off LEDs on exit
            #print(f"Excption: {e}")
        observer.join()