#!/home/rjslater/anaconda3/bin/python
import subprocess
from os import environ, system
environ['DISPLAY'] = ":0.0"
from time import sleep

import pyautogui as p


passwordCommand = 'lpass show 316585325245308485'
ps = subprocess.Popen(passwordCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ps.communicate()[0].decode('utf-8')

# If not logged in, ask the user to log in
if 'Error: Could not find decryption key. Perhaps you need to login with `lpass login`.' in output:
    loginCommand = 'konsole -e lpass login ryan.j.slater.2@gmail.com'
    ps = subprocess.Popen(loginCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=dict(environ, DISPLAY=":0.0", XAUTHORITY="/home/rjslater/.Xauthority"))
    output = ps.communicate()[0].decode('utf-8')

# Get username/password
ps = subprocess.Popen(passwordCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ps.communicate()[0].decode('utf-8')
lines = output.split('\n')[1:3]
username = lines[0][lines[0].find(':') + 1:].strip()
password = lines[1][lines[1].find(':') + 1:].strip()

# Open browser
browserCommand = 'qutebrowser https://pilot.wright.edu/d2l/home &'
system(browserCommand)
sleep(5)

# Login
p.click()
p.press('f')
sleep(0.5)
p.press('d')
sleep(3)
p.press('i')
p.typewrite(username)
p.press('tab')
p.typewrite(password)
p.press('return')
