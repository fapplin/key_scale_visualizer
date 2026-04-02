#!/bin/bash

cd /home/frank/anvildir
source bin/activate
echo **************************************
echo * Starting check LED file process
echo **************************************
cd /home/frank/anvildir/M3_App_2/services
sudo /home/frank/anvildir/bin/python /home/frank/anvildir/M3_App_2/services/check_led_file.py 



