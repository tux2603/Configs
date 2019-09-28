#!/home/rjslater/anaconda3/bin/python


if __name__ == '__main__':
    with open('/proc/cpuinfo', 'r') as cpuInfoFile:
        cpuInfo = cpuInfoFile.readlines()
        coreSpeeds = []
        for line in cpuInfo:
            if 'MHz' in line:
                coreSpeeds.append(round(int(float(line[line.find(':') + 1:].strip())) / 1000, 1))

        print(str(max(coreSpeeds)) + ' GHz')
