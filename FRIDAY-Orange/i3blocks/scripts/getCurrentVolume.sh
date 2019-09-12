#!/bin/bash

pacmd list-sinks | grep % > /home/rjslater/.config/i3blocks/scripts/.currentVolume
pacmd list-sinks | grep mute >> /home/rjslater/.config/i3blocks/scripts/.currentVolume
