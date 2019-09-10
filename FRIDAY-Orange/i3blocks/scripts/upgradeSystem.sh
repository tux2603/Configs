#!/bin/bash
sudo apt-get update;
sudo apt-get upgrade -y;
sudo apt-get autoremove -y;
sudo apt-get autoclean -y;
sudo updatedb;
notify-send "Update Complete"
exit