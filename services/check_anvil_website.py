import requests
import time
import os
import hashlib
from unittest.mock import MagicMock

# --- Cloud-Safe Hardware Import ---
try:
    import RPi.GPIO as GPIO
    IS_PI = True
except ImportError:
    # If not on a Pi, create a fake GPIO object so the code still runs
    GPIO = MagicMock()
    # Manually define the constants the code needs
    GPIO.BCM = "BCM"
    GPIO.OUT = "OUT"
    GPIO.LOW = 0
    GPIO.HIGH = 1
    IS_PI = False
    print("--- Running in Cloud/Simulated Mode ---")

# --- Configuration ---
TARGET_URL = "http://192.168.1.237:3030"
TARGET_FILE = "/home/frank/anvildir/M3_App_2/services/errors.txt"
CHECK_INTERVAL = 5

# GPIO Pin Setup
YELLOW_LED = 22
GREEN_LED = 27
RED_LED = 26

# These will now run on the Pi OR the Cloud without crashing
GPIO.setmode(GPIO.BCM)
GPIO.setup([YELLOW_LED, GREEN_LED, RED_LED], GPIO.OUT, initial=GPIO.LOW)

def get_file_hash(filepath):
    """Generates an MD5 hash of the file to detect changes."""
    if not os.path.exists(filepath):
        return None
    # Using 'with' is safer for file handling on the Pi
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def monitor():
    website_up = False
    initial_hash = None

    print("Starting monitor... Press Ctrl+C to stop.")
    
    try:
        while True:
            # Task 1: Check Website Availability
            try:
                response = requests.get(TARGET_URL, timeout=5)
                is_available = response.status_code == 200
            except requests.RequestException:
                is_available = False

            if is_available:
                GPIO.output(YELLOW_LED, GPIO.LOW)
                GPIO.output(GREEN_LED, GPIO.HIGH)
                
                if not website_up:
                    print(f"Site {TARGET_URL} is UP. Monitoring file...")
                    website_up = True
                    initial_hash = get_file_hash(TARGET_FILE)
                
                current_hash = get_file_hash(TARGET_FILE)
                if initial_hash and current_hash != initial_hash:
                    GPIO.output(RED_LED, GPIO.HIGH)
                    if not IS_PI:
                        print("[Simulated] File change detected! RED LED would be ON.")
                    else:
                        print("File change detected! Red LED ON.")
            else:
                GPIO.output(YELLOW_LED, GPIO.HIGH)
                GPIO.output(GREEN_LED, GPIO.LOW)
                GPIO.output(RED_LED, GPIO.LOW) 
                website_up = False
                print("Site is DOWN. Yellow LED ON.")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        # Only cleanup if we are actually on the Pi
        if IS_PI:
            GPIO.cleanup()

if __name__ == "__main__":
    monitor()