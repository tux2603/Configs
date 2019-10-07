#!/home/rjslater/anaconda3/bin/python
import subprocess
from os import system

# Get device list
listCommand = "pactl list short sinks"
ps = subprocess.Popen(listCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
devices = ps.communicate()[0].decode('utf-8').strip().split('\n')
for i, d in enumerate(devices):
    devices[i] = d[d.find('alsa'):d.find('module')].strip()

# Get current device
try:
    with open('.currentAudioOutput', 'r') as f:
        currentDevice = int(f.read())
except:
    currentDevice = 0

# Increment current device
currentDevice += 1
if currentDevice >= len(devices):
    currentDevice = 0

# Set new current device
setCommand = 'pactl set-default-sink "{}"'.format(devices[currentDevice])
system(setCommand)

# Notification for new device
if devices[currentDevice] == 'alsa_output.pci-0000_01_00.1.hdmi-stereo':
    system('notify-send -t 2000 "HDMI Stereo"')
elif devices[currentDevice] == 'alsa_output.pci-0000_00_1f.3.analog-stereo':
    system('notify-send -t 2000 "Analog Stereo"')
elif devices[currentDevice] == 'alsa_output.usb-Cooler_Master_Technology_Inc._MH752_00000000-00.analog-stereo':
    system('notify-send -t 2000 "CM MH752 Headset"')


# Write current device file
with open('.currentAudioOutput', 'w') as f:
    f.write(str(currentDevice))
