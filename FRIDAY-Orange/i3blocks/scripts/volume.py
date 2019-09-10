#!/home/rjslater/anaconda3/bin/python
import subprocess

subprocess.call('/home/rjslater/.config/i3blocks/scripts/getCurrentVolume.sh')
volumeData = [i for i in open('/home/rjslater/.config/i3blocks/scripts/.currentVolume', 'r')]

volume = int(float(volumeData[5][volumeData[5].find('[') + 1:volumeData[5].find(']') - 1].strip()))
muted = False
for i in range(4, 7):
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
