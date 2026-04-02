#!/bin/bash

cd anvildir
source bin/activate
echo **************************************
echo * Starting check to see if anvil
echo * web server is up and running
echo **************************************
cd /home/frank/anvildir/M3_App_2/services
sudo /home/frank/anvildir/bin/python /home/frank/anvildir/M3_App_2/services/check_anvil_website.py &




