These service files go in /etc/systemd/system directory.

start_anvil_checks.service   (Uses the /usr/local/bin/start_anvil_check.sh) 
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
