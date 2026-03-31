import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from unittest.mock import MagicMock

# --- CLOUD-SAFE HARDWARE IMPORT ---
try:
    import board
    import neopixel
    IS_PI = True
except ImportError:
    # Mocking board and neopixel for Anvil Editor
    board = MagicMock()
    board.D18 = "D18"
    neopixel = MagicMock()
    neopixel.GRB = "GRB"
    IS_PI = False
    print("--- CLOUD MODE: NeoPixel hardware mocked ---")

# --- CONFIGURATION ---
PIXEL_PIN = board.D18
WATCH_FILE = Path("/home/frank/anvildir/M3_App_2/services/leds.txt")
pixels = None

COLOR_MAP = {
    "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
    "yellow": (255, 255, 0), "cyan": (0, 255, 255), "magenta": (255, 0, 255),
    "white": (255, 255, 255), "off": (0, 0, 0)
}

def process_led_file(file_path):
    global pixels
    try:
        if not file_path.exists():
            return

        with open(file_path, "r") as f:
            lines = f.readlines()
            if not lines:
                return
            
            # Line 1: Setup
            num_pixels_from_file = int(lines[0].strip())
            ORDER = neopixel.GRB
            
            # Only initialize pixels if they haven't been yet
            if pixels is None:
                # We use 210 as per your original code
                pixels = neopixel.NeoPixel(PIXEL_PIN, 210, brightness=0.2, auto_write=True, pixel_order=ORDER)
                pixels.fill((0,0,0))

            # Process remaining lines
            for line in lines[1:]:
                parts = [p.strip().lower() for p in line.split(",")]
                if len(parts) == 2:
                    index_str, color_name = parts
                    key_color = index_str[-1] # 'w' or 'b'
                    pixel_index = int(index_str[:-1])
                    
                    rgb_value = COLOR_MAP.get(color_name)
                    
                    if rgb_value and 0 <= pixel_index < 210:
                        if key_color == "b" and color_name != "off":
                            rgb_value = COLOR_MAP.get("magenta")
                        
                        pixels[pixel_index] = rgb_value
                        if not IS_PI:
                            print(f"[Sim] Pixel {pixel_index} -> {color_name}")

    except Exception as e:
        print(f"Error processing file: {e}")

class LedFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if Path(event.src_path).resolve() == WATCH_FILE.resolve():
            process_led_file(WATCH_FILE)

if __name__ == "__main__":
    WATCH_DIR = WATCH_FILE.parent
    if not WATCH_DIR.exists():
        print(f"Error: Directory {WATCH_DIR} does not exist.")
    else:
        # Check if file exists to do initial load
        if WATCH_FILE.exists():
            process_led_file(WATCH_FILE)

        event_handler = LedFileHandler()
        observer = Observer()
        observer.schedule(event_handler, str(WATCH_DIR), recursive=False)
        observer.start()

        print(f"Monitoring {WATCH_FILE.name} for commands...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            if pixels:
                pixels.fill((0, 0, 0))
        observer.join()