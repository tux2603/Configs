#!/home/rjslater/anaconda3/bin/python
import psutil as p

cpuPercent = int(float(p.cpu_percent(interval=1)))
cpuChar = '\uf109'

print('{} {}%'.format(cpuChar, cpuPercent))
