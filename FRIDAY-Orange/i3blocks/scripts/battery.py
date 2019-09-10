#!/home/rjslater/anaconda3/bin/python
import os

powerSupplyDirectory = '/sys/class/power_supply'


def getBatteryStats(batteryName):
    # Capacity
    capacity = 0
    for line in open(powerSupplyDirectory + '/' + batteryName + '/capacity', 'r'):
        capacity = int(float(line))

    # Current status
    status = ''
    for line in open(powerSupplyDirectory + '/' + batteryName + '/uevent', 'r'):
        if 'STATUS' in line:
            status = line[line.find('=') + 1:].strip()
            break
    if status == 'Full':
        status = '✓'
    elif status == 'Discharging':
        status = '▼'
    elif status == 'Charging':
        status = '▲'
    elif status == 'Unknown':
        status = '\uf0dc'

    if capacity < 20:
        batteryName = '\uf244'
    elif capacity < 40:
        batteryName = '\uf243'
    elif capacity < 60:
        batteryName = '\uf242'
    elif capacity < 80:
        batteryName = '\uf241'
    else:
        batteryName = '\uf240'

    return batteryName + ' ' + str(capacity) + '% ' + status


if __name__ == '__main__':
    powerSupplies = os.listdir(powerSupplyDirectory)
    powerSupplies = [psu for psu in powerSupplies if psu != 'AC']
    powerSupplies.sort()

    stats = [getBatteryStats(psu) for psu in powerSupplies]

    print('   '.join(stats))
