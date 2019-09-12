#!/home/rjslater/anaconda3/bin/python
import fontawesome as fa

with open('/sys/class/backlight/intel_backlight/brightness') as curBrightnessFile:
    currentBrightness = float(curBrightnessFile.readline().strip())
with open('/sys/class/backlight/intel_backlight/max_brightness') as maxBrightnessFile:
    maxBrightness = float(maxBrightnessFile.readline().strip())

print(fa.icons['lightbulb'] + ' ' + str(int(100 * currentBrightness // maxBrightness)) + '%')
