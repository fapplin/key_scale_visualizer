from gpiozero import Button
from subprocess import check_call
from signal import pause
import os

# Define the button on GPIO 21
# hold_time=2 means you must press for 2 seconds to trigger
button = Button(21, hold_time=2)

def system_shutdown():
    print("Shutting down...")
    check_call(['sudo', 'poweroff'])

# Attach the function to the 'held' event
button.when_held = system_shutdown

print("Shutdown monitor active (GPIO 21). Hold for 2s to power off.")
pause()
