#!/home/rjslater/anaconda3/bin/python

if __name__ == '__main__':
    with open('/sys/class/thermal/thermal_zone1/temp', 'r') as temp:
        print(temp.read()[:-4] + '\u00B0C')
