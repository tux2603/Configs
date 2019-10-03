#!/home/rjslater/anaconda3/bin/python

import os
import smtplib


def getIP():
    # Get network stats and save to a file
    os.system("ifconfig > /home/rjslater/.config/i3blocks/scripts/.ifconfigLog")

    # Read the file
    devices = []
    currentDevice = []
    for line in open('/home/rjslater/.config/i3blocks/scripts/.ifconfigLog', 'r'):
        if line.strip() == '':
            devices.append(currentDevice)
            currentDevice = []
        else:
            currentDevice.append(line.strip())

    # Remove the loopback device
    for i in range(len(devices)):
        if 'lo:' in devices[i][0]:
            devices.pop(i)
            break

    # Make the devices a bit easier to read and parse
    cleanedDevices = []
    for device in devices:
        currentDeviceInfo = {}
        currentDeviceInfo['name'] = device[0][:device[0].find(':')]
        currentDeviceInfo['type'] = '\uf0e8' if 'enp' in currentDeviceInfo['name'] else '\uf1eb'
        currentDeviceInfo['status'] = ', '.join([i for i in device[0][device[0].find('<') + 1:device[0].find('>')].lower().split(',') if i not in ['up', 'broadcast', 'multicast']])
        if 'inet' in device[1]:
            currentDeviceInfo['IP address'] = device[1][device[1].find('inet ') + 5:device[1].find('  netmask')]

        cleanedDevices.append(currentDeviceInfo)

    for device in cleanedDevices:
        if 'running' in device['status']:
            return device['IP address']


def writeIPFile(ip):
    with open('/home/rjslater/.config/i3/.previousIP', 'w') as f:
        f.write(ip)


def sendEmail(recipients, subject, content):
    username = 'slaterPython@gmail.com'
    password = '&v9*7OHxCc8n'

    emailText = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(username, ', '.join(recipients), subject, content)

    print(emailText)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(username, password)
        server.sendmail(username, recipients, emailText)
        server.close()

        return 'Email sent!'
    except:
        return 'Something went wrong...'


if __name__ == '__main__':
    ip = getIP()

    try:
        with open('/home/rjslater/.config/i3/.previousIP', 'r') as f:
            previousIP = f.readline().strip()
            if ip != previousIP:
                writeIPFile(ip)
                print(sendEmail(['ryan.j.slater.2@gmail.com'], 'F.R.I.D.A.Y. IP', ip))
    except FileNotFoundError:
        writeIPFile(ip)
        print(sendEmail(['ryan.j.slater.2@gmail.com'], 'F.R.I.D.A.Y. IP', ip))
