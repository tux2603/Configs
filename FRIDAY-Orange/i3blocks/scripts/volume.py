#!/home/rjslater/anaconda3/bin/python
import subprocess

subprocess.call('/home/rjslater/.config/i3blocks/scripts/getCurrentVolume.sh')
volumeData = [i for i in open('/home/rjslater/.config/i3blocks/scripts/.currentVolume', 'r')]

volume = int(float(volumeData[0][volumeData[0].find('/') + 1:volumeData[0].find('%')].strip()))
muted = False
for i in range(len(volumeData)):
    if 'yes' in volumeData[i]:
        muted = True
        break

volLow = '\uf026'
volMid = '\uf027'
volHi = '\uf028'

if not muted:
    if volume < 33:
        print('{} {}%'.format(volLow, volume))
    elif volume < 66:
        print('{} {}%'.format(volMid, volume))
    else:
        print('{} {}%'.format(volHi, volume))
else:
    print('{} MUTE'.format(volLow))
