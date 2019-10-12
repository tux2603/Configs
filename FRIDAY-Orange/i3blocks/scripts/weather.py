#!/home/rjslater/anaconda3/bin/python
from subprocess import Popen, PIPE, STDOUT

cmd = 'curl wttr.in?format="%C+%t"'
ps = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
output = ps.communicate()[0].decode('utf-8').strip()

# Getting condition
condition = output[:output.rfind(' ')].strip()

# Getting temperature
farenheit = output[output.rfind(' '):].strip()
if farenheit[0] == '+':
    farenheit = farenheit[1:]
celsius = str(int((int(farenheit[:-2]) - 32) * 5.0/9.0)) + '°C'

# Weather icons
awesomeIcons = {'cloud':               '\uf0c2',
                'cloud-download-alt':  '\uf381',
                'cloud-meatball':      '\uf73b',
                'cloud-moon':          '\uf6c3',
                'cloud-moon-rain':     '\uf73c',
                'cloud-rain':          '\uf73d',
                'cloud-showers-heavy': '\uf740',
                'cloud-sun':           '\uf6c4',
                'cloud-sun-rain':      '\uf743',
                'cloud-upload-alt':    '\uf382',
                'sun':                 '\uf185',
                'moon':                '\uf186',
                'wind':                '\uf72e',
                'snowflake':           '\uf2dc'}

#for key in awesomeIcons.keys():
#    print(fa.icons[key])

icons = {'Cloudy': awesomeIcons['cloud'],
         'Partly cloudy': awesomeIcons['cloud-sun'],
         'Overcast': 'OVERCAST',
         'Clear': 'CLEAR',
         'Sunny': awesomeIcons['sun'],
         'Patchy rain possible': 'PATCHY RAIN POSSIBLE',
         'Moderate rain': 'MODERATE RAIN',
         'Light Rain, Mist': awesomeIcons['cloud-rain']}

if condition in icons.keys():
    print(icons[condition] + ' {} ({})'.format(celsius, farenheit))
else:
    print(condition + ' ICON NOT FOUND {} ({})'.format(celsius, farenheit))