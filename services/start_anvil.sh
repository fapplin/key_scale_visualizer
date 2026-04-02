#!/bin/bash

cd /home/frank/anvildir
source bin/activate

echo **************************************
echo * Starting Anvil web server
echo **************************************
anvil-app-server --app M3_App_2 --dep-id dep_o8zvvm7m0g7a5m=anvil_extras 
