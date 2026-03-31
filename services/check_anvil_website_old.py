import RPi.GPIO as GPIO
import requests
import time
import os
import hashlib

# --- Configuration ---
TARGET_URL = "http://192.168.1.237:3030"  # Change to your target site
TARGET_FILE = "/home/frank/anvildir/led_client/errors.txt"                # Change to your target file path
CHECK_INTERVAL = 5                     # Seconds between checks

# GPIO Pin Setup (Board Numbering)
YELLOW_LED = 22
GREEN_LED = 27
RED_LED = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup([YELLOW_LED, GREEN_LED, RED_LED], GPIO.OUT, initial=GPIO.LOW)

def get_file_hash(filepath):
    """Generates an MD5 hash of the file to detect changes."""
    if not os.path.exists(filepath):
        return None
    return hashlib.md5(open(filepath, 'rb').read()).hexdigest()

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
                
                # Task 2: Check for File Change (Only if site is up)
                if not website_up:
                    print(f"Site {TARGET_URL} is UP. Monitoring file...")
                    website_up = True
                    initial_hash = get_file_hash(TARGET_FILE)
                
                current_hash = get_file_hash(TARGET_FILE)
                if initial_hash and current_hash != initial_hash:
                    GPIO.output(RED_LED, GPIO.HIGH)
                    print("File change detected! Red LED ON.")
            else:
                GPIO.output(YELLOW_LED, GPIO.HIGH)
                GPIO.output(GREEN_LED, GPIO.LOW)
                GPIO.output(RED_LED, GPIO.LOW) # Reset red if site goes back down
                website_up = False
                print("Site is DOWN. Yellow LED ON.")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    monitor()