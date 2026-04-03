I will leave it to whoever might use this project to go through and change the path names in the following files. It is currently set up to use:

/home/frank/anvildir - where anvil projects are located (this is the only anvil project for the device)
/home/frank/anvildir/M3_App_2 - this is the anvil project itself
/home/frank/anvildir/M3_App_2/services - this is the code I wrote to be used with bash files and .service files.

check_anvil_website.py - checks to see if the anvil website is up. Turns on yellow LED while site is starting. Turns on green LED when the website is ready.
check_led_file.py - this checks the file "leds.txt" to see if the web page has sent data to it via choosing a key, scale, and clicking LEDs On.
shutdown.py - this works with the button on the board. If the button is pressed for 2 seconds - the Raspberry Pi does a graceful shutdown.

These service files go in /etc/systemd/system directory.

start_anvil_check.service   (Uses the /usr/local/bin/start_anvil_check.sh) 
start_anvil_check.sh (This runs a python script to check when the anvil-app-server
                      is up and running. Yellow LED while loading. Green LED when
                      the server is ready for use.)
mystartup.service            (Uses the /usr/local/bin/start_led.sh bash file.)
start_led.sh         (This is a python script that checks the LEDS.txt file for changes.
                      When there are changes, the script will turn the LED strip on.)
shutdown-script.service (When a button is press on the PCB board for 
                         2 seconds - the system cleanly shuts down. It uses the python script /home/frank/anvildir/M3_App_2/services/shutdown.py.)

User Services
                      
These files are used in setting up a local service in /home/frank/.config/systemd/user directory.
NOTE: Anvil server cannot start as root. This starts the anvil-app-server.

mystartup2.service    (Uses the start_anvil.sh bash file.)
start_anvil.sh
