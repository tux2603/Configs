#!/home/rjslater/anaconda3/bin/python
from subprocess import Popen, PIPE
import os

if __name__ == '__main__':
    process = Popen(['nmcli', 'radio', 'wifi'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.decode('utf-8').strip()

    # Flipped because this runs before toggleWifi.py
    if 'enabled' not in stdout:
        process = Popen(['notify-send', '-t', '2000', '-i', 'network-wireless-disconnected', 'Wireless disabled', 'Your wireless adaptor has been disabled.'], stdout=PIPE, stderr=PIPE)
    else:
        process = Popen(['notify-send', '-t', '2000', '-i', 'network-wireless-full', 'Wireless enabled', 'Your wireless adaptor has been enabled.'], stdout=PIPE, stderr=PIPE)
