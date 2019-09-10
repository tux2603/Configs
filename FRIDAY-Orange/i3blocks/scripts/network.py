#!/home/rjslater/anaconda3/bin/python
import os
from subprocess import check_output, Popen, PIPE, STDOUT


def getIPAndType():
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
            return device['type'], device['IP address']


def getSSID():
    cmd = "nmcli dev wifi"
    ps = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output = ps.communicate()[0].decode('utf-8').strip()

    networks = []  # list of dicts of networks
    for line in output.split('\n'):
        # Add not in use placeholder
        if '*' not in line:
            line = '.' + line
        # Split output into list of properties
        properties = line.split('  ')
        i = 0
        while i < len(properties):
            if len(properties[i]) == 0 or properties[i] == ' ':
                properties.pop(i)
            else:
                properties[i] = properties[i].strip()
                i += 1

        network = {}
        network['inUse'] = True if properties[0] == '*' else False
        network['SSID'] = properties[1].strip()
        network['mode'] = properties[2].strip()
        network['channel'] = properties[3].strip()
        network['rate'] = properties[4].strip()
        network['signal'] = properties[5].strip()
        network['bars'] = properties[6].strip()
        network['security'] = properties[7].strip()

        networks.append(network)

    # Crop out title row
    networks.pop(0)

    # Find connected network
    for network in networks:
        if network['inUse']:
            return network['SSID'], network['bars']
    return ''


if __name__ == '__main__':
    ssid = getSSID()

    # Get IP
    ip = getIPAndType()

    # Final print
    print(ip[0] + ' ' + ssid[0] + ' ' + ip[1] + ' ' + ssid[1])
