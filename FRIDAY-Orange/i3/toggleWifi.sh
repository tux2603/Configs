#!/bin/bash

if nmcli networking connectivity | grep -q "none" ; then
    nmcli networking on
    notify-send -t 2000 -i network-wireless-full "Wireless enabled" "Your wireless adaptor has been enabled."
else
    nmcli networking off
    notify-send -t 2000 -i network-wireless-disconnected "Wireless disabled" "Your wireless adaptor has been disabled."
fi
