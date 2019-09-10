#!/bin/bash

amixer -D pulse get Master > /home/rjslater/.config/i3blocks/scripts/.currentVolume
pacmd list-sinks | grep mute >> /home/rjslater/.config/i3blocks/scripts/.currentVolume
