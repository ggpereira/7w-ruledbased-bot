#!/bin/bash

echo 'Digite o ID do bot:' 
read bot_id 

python3 main.py "$HOME/seven_wonders/Game/build/io" $bot_id


