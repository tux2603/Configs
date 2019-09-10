#!/home/rjslater/anaconda3/bin/python
import psutil as p


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

memTotal = p.virtual_memory().total
memUsed = p.virtual_memory().used
memPercent = int(100 * memUsed / memTotal)
memChar = '\uf2db'

print('{} {}%'.format(memChar, memPercent))
# print('{} {} / {} {}%'.format(memChar, sizeof_fmt(memUsed), sizeof_fmt(memTotal), memPercent))
